# -*- coding: utf-8 -*-

"""
Hygrothermal properties of materials
"""

import numpy as np
import numpy.typing as npt

from HT import library as lib
from HT.materials_library import Rammed_Earth
from functions import create_array_material, check_callable


class Material:

    def __init__(self, **kwargs):
        self._rho = kwargs["rho"]
        self._cp = kwargs["cp"]
        self._k = kwargs["k"]
        self._delta_l = kwargs["dl"]
        self._delta_p = kwargs["dp"]
        self._w = kwargs["w"]
        self._w_array = kwargs["w_array"]
        self._mu = kwargs["mu"]
        self._delta_l_array = kwargs["dl_array"]
        self._RH_table = kwargs["RH_table"]
        self.N_nodes = kwargs["mesh"][1]
        self.N_tot = kwargs["mesh"][2]

    def rho(self) -> npt.NDArray[np.float64]:
        """
        Density of the dry material [kg.m-3]
        """
        rho = create_array_material(self.N_nodes, self.N_tot, self._rho)
        return rho

    def Cp(self, RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Heat capacity of the materials [J.kg-1.K-1]
        """
        Cp = create_array_material(self.N_nodes, self.N_tot, self._cp, [RH])
        return Cp

    def k(self) -> npt.NDArray[np.float64]:
        """
        Thermal conductivity [W.m-1.K-1]
        """
        k = create_array_material(self.N_nodes, self.N_tot, self._k)
        return k

    def w(self, RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Water content [kg.m-3]
        """
        w = create_array_material(self.N_nodes, self.N_tot, self._w, [RH], [self._w_array])
        return w

    def delta_p(self, T: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Water vapour permeability [kg/(m.s.Pa)]
        """
        delta_p = create_array_material(self.N_nodes, self.N_tot, self._delta_p, [T], [self._mu])
        return delta_p

    def delta_l(self, RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Liquid water permeability [kg/(m.s.Pa)]
        """
        delta_l = create_array_material(self.N_nodes, self.N_tot, self._delta_l, [RH],  [self._RH_table, self._delta_l_array])
        return delta_l

    def Dw(self) -> npt.NDArray[np.float64]:
        """
        Liquid diffusion coefficient [m2/s]
        """
        dw = np.zeros([self.N_tot, 1])
        n_tot = 0  # keep track of where we are
        for i, node in enumerate(self.N_nodes):
            n = int(node[0])
            if i == 0:
                dw[:n] = np.pi * (Rammed_Earth.Avalue() / (2 * Rammed_Earth.wsat() * check_callable(self._rho[i])))
            else:
                dw[n_tot: n_tot + n] = (Rammed_Earth.Avalue() / (2 * Rammed_Earth.wsat() * check_callable(self._rho[i])))
            n_tot += n

        return dw

    def Xi(self, T: npt.NDArray[np.float64], RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Hygric capacity (pc) (dw/dpc) = (dw/dRH*dRH/dpc)
        """
        xi = np.zeros([self.N_tot, 1])
        n_tot = 0  # keep track of where we are
        for i, node in enumerate(self.N_nodes):
            n = int(node[0])
            if i == 0:
                xi[:n] = self.rho()[:n] * lib.partial_derivative(self.w, 0, [RH])[:n] * (
                        np.exp(-lib.pc(T[:n], RH[:n]) / (lib.rhoL * lib.Rv * T[:n])) / (-lib.rhoL * lib.Rv * T[:n]))

            else:
                xi[n_tot: n_tot + n] = self.rho()[n_tot : n_tot + n] * lib.partial_derivative(self.w, 0, [RH])[n_tot : n_tot + n] * (
                            np.exp(-lib.pc(T[n_tot : n_tot + n], RH[n_tot : n_tot + n]) / (lib.rhoL * lib.Rv * T[n_tot : n_tot + n])) / (-lib.rhoL * lib.Rv * T[n_tot : n_tot + n]))
            n_tot += n
        return xi
