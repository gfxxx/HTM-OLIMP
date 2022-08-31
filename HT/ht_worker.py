# -*- coding: utf-8 -*-

"""
The simulation worker.
Run on another Thread and launch simulation algorithm on a new Process
"""

import multiprocessing
from PySide6.QtCore import Signal, QThread

from HT.algorithm import main
from HT.materials import Material
from HT.boundary import Boundary
from HT.mesh import Mesh


class Worker(QThread):
    """
        Create a Worker on a new thread, and run calculation on another process
    """
    finished = Signal(float)
    progress = Signal(float)
    results = Signal(object)

    def __init__(self, material: Material, bo: Boundary, mesh: Mesh) -> object:
        """
        Parameters
        ----------
        material:
            Material matrice
        bo:
            Boundary
        mesh:
            Mesh
        """
        super(Worker, self).__init__()

        # ----- Initialize values ----- #
        self.process: multiprocessing.Process | None = None
        self.running = False

        self._bo = bo
        self._material = material
        self._mesh = mesh

    def run(self) -> None:
        """
        Override of run QThread method
        Launch calculation on a new process and get result back.
        """
        self.running = True  # Set running state

        # ----- Create shared cross-processing variables ----- #
        manager = multiprocessing.Manager()
        p = multiprocessing.Value('d', 0.0)  # progression
        t = multiprocessing.Value('d', 0.0)  # time
        tsim = multiprocessing.Array('d', range(int(self._bo.t_tot / self._bo.dt) + 1)) # Cumulative time step matrice
        T_final = manager.dict()
        RH_final = manager.dict()
        pv_final = manager.dict()
        self.process = multiprocessing.Process(target=main,
                                               args=(p, t, tsim, T_final, RH_final, pv_final, self._material, self._bo,
                                                     self._mesh))  # Create simulation process
        self.process.start()  # Create simulation process
        while (p.value < 1.0) & self.running:  # Send new progress value whiles not finish
            self.progress.emit(p.value)
        if p.value >= 1:
            self.progress.emit(1)  # Send 1 to be sure to get 100% on progress bar
        self.process.join()  # Close process
        self.finished.emit(t.value)  # Send time value
        # Create df for values
        result = {
            "scatter": [RH_final["x"], RH_final["y"]],
            "T": T_final["stock"],
            "RH": RH_final["stock"],
            "pv": pv_final["stock"]
        }
        self.results.emit(result)  # Send result value
        self.running = False  # Set running state

    def stop(self) -> None:
        """
        Stop the calculation
        """
        if self.process is not None:
            self.process.kill()  # Kill process
            self.process.join()  # Close process
            self.running = False  # Set running state
            self.wait()  # Wait until everything's done
