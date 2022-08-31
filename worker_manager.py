# -*- coding: utf-8 -*-

"""
The worker manager.
Run and stop worker, handle instances the worker needs (Boundary, Mesh)
"""

import numpy as np
from typing import Callable
import numpy.typing as npt

from HT.ht_worker import Worker
from HT.materials import Material
from functions import material_factory, check_modified
from HT.mesh import Mesh
from HT.boundary import Boundary


class WorkerManager:
    def __init__(self):

        # ----- Initialize values ----- #
        self.thread: Worker | None = None  # Worker
        self.material = None  # Material
        self.bo = None  # boundary
        self.mesh = None  # mesh
        self.sizes = []  # All material sizes
        self.materials = []  # All material

    def build_mesh(self, nb_layer: int) -> None:
        """
        Build mesh

        Parameters
        ----------
        nb_layer:
            Number of layers
        """
        self.mesh = Mesh(1, self.sizes, nb_layer)

    def build_boundary(self, climate_data: npt.NDArray[np.float64], rad_data) -> None:
        """
        Build boundary

        Parameters
        ----------
        climate_data:
            Meteo data
        rad_data:
            Radiation data
        """
        self.bo = Boundary(climate_data=climate_data, rad_data=rad_data)

    def build_worker(self, progress: Callable, results: Callable, finished: Callable) -> None:
        """
        Build the worker

        Parameters
        ----------
        progress:
            Function which update progress bar
        results:
            Function which create results table and plot
        finished:
            Function launch when worker will be finish
        """
        self.thread = Worker(self.material, self.bo, self.mesh)  # Create worker
        if self.thread is not None:
            self.thread.progress.connect(progress)  # Connect progress shared variable with progress bar updating method
            self.thread.finished.connect(
                lambda time: self.finished(time, finished))  # Connect finished shared variable with method
            self.thread.results.connect(
                results)  # Connect results shared variable with create result table and plotting method

    def build_material(self, pages) -> None:
        """
        Build Material instance for the model

        Parameters
        ----------
        pages:
            Material tabs (GUI)
        """

        rho = []
        cp = []
        k = []
        dp = []
        dl = []
        w_array = []
        w = []
        mu = []
        RH_table = []
        dl_array = []

        for mat in self.materials:
            material = material_factory(mat)
            ui = pages[mat]

            # Check if value is modified in UI, and add to tha array of material
            # check_modified(ui.rho, material.rho, rho)
            # check_modified(ui.cp, material.Cp, cp)
            # check_modified(ui.k_2, material.k, k)
            rho.append(ui.rho.text())
            cp.append(ui.cp.text())
            k.append(ui.k_2.text())
            dp.append(material.delta_p)
            dl.append(material.delta_l)
            dl_array.append([ui.dl_1.text(), ui.dl_2.text(), ui.dl_3.text()])
            RH_table.append([ui.rh_1.text(), ui.rh_2.text(), ui.rh_3.text()])
            mu.append(ui.mu.text())
            w.append(material.w)

            w0 = 0.0
            w10 = float(ui.w10.text())
            w20 = float(ui.w20.text())
            w30 = float(ui.w30.text())
            w40 = float(ui.w40.text())
            w50 = float(ui.w50.text())
            w60 = float(ui.w60.text())
            w70 = float(ui.w70.text())
            w80 = float(ui.w80.text())
            w90 = float(ui.w90.text())
            w100 = float(ui.w100.text())
            w_array.append([w0, w10, w20, w30, w40, w50, w60, w70, w80, w90, w100])

        self.material = Material(rho=rho, cp=cp, k=k, dp=dp, dl=dl, w=w, w_array=w_array, mu=mu, RH_table=RH_table, dl_array=dl_array, mesh=self.mesh)

    def run_ht(self, pages, progress, results, finished) -> None:
        """
        Run the worker

        Parameters
        ----------
        pages:
            Material tabs (GUI)
        progress:
            Function which update progress bar
        results:
            Function which create results table and plot
        finished:
            Function launch when worker will be finish
        """
        self.build_material(pages)
        self.build_worker(progress, results, finished)
        if self.thread is not None:
            self.thread.start()

    def stop(self) -> None:
        """
            Stop the worker
        """
        if self.thread is not None:
            self.thread.stop()

    def finished(self, time: float, finished: Callable) -> None:
        """
        Once worker's done, stop the thread and show result

        Parameters
        ----------
        time:
            Time simulation take
        finished:
            Function launch when worker will be finish
        """
        if self.thread is not None:
            self.thread.quit()
            if time > 0.0:
                finished(time)
