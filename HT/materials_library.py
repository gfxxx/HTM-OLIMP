# -*- coding: utf-8 -*-

"""
Materials library
"""


import numpy as np
import numpy.typing as npt

from HT import library as lib


class MaterialTemplate:
    """
    Template for Material database
    """

    @staticmethod
    def rho() -> int:
        return 0

    @staticmethod
    def Cp(RH: npt.NDArray[np.float64]) -> int:
        return 0

    @staticmethod
    def k() -> float:
        return 0.0

    @staticmethod
    def w(RH: npt.NDArray[np.float64], w =None) -> npt.NDArray[np.float64]:
        RH_table = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        if w is None:
            w = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        else:
            w = np.array(w).astype(float)
        return np.interp(RH, RH_table, w), RH_table, w

    @staticmethod
    def mu() -> int:
        return 1

    @staticmethod
    def delta_p(T: npt.NDArray[np.float64], mu: None | float=None) -> npt.NDArray[np.float64]:
        if mu is None:
            mu = MaterialTemplate.mu()
        return lib.delta_a(T) / float(mu)

    @staticmethod
    def delta_l(RH: npt.NDArray[np.float64], RH_table=None, delta_l=None) -> npt.NDArray[np.float64]:
        if RH_table is None:
            RH_table = np.array([0, 0.85, 1])
        else:
            RH_table = np.array(RH_table).astype(float)

        if delta_l is None:
            delta_l = np.array([0, 0, 0])
        else:
            delta_l = np.array(delta_l).astype(float)
        return np.interp(RH, RH_table, delta_l), RH_table, delta_l


class Rammed_Earth(MaterialTemplate):
    """
    Rammed earth from Saint-Antoine de l'Abbaye
    The hygrothermal properties are given in Chabriac's thesis (2014)
    """
    @staticmethod
    def rho() -> int:
        """
        Density of the dry material [kg/m3]
        """
        return 1730

    @staticmethod
    def Cp(RH: npt.NDArray[np.float64]) -> int:
        """
        Heat capacity [J.kg-1.K-1]
        """
        return 648

    @staticmethod
    def k() -> float:
        """
        Thermal conductivity [W.m-1.K-1]
        With w in kgv/kg
        """
        return 1.15

    @staticmethod
    def w(RH: npt.NDArray[np.float64], w=None) -> npt.NDArray[np.float64]:
        """
        Water content [kg.m-3]
        """
        #RH_table = np.array([0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1])
        #w = np.array([0, 0.0004, 0.0012, 0.0020, 0.0026, 0.0031, 0.0036, 0.0041, 0.0046, 0.0067, 0.0088, 0.0108, 0.0131, 0.0146, 0.0164, 0.0187, 0.0218, 0.0265, 0.0298, 0.0341, 0.0399, 0.0480, 0.0594, 0.2011])
        RH_table = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        if w is None:
            w = np.array([0, 0.0026, 0.0046, 0.0067, 0.0088, 0.0108, 0.0131, 0.0164, 0.0218, 0.0341, 0.2011])
        else:
            w = np.array(w).astype(float)
        return np.interp(RH, RH_table, w), RH_table, w

    @staticmethod
    def mu() -> int:
        """
        Water vapour resistance factor [-]
        """
        return 10

    @staticmethod
    def delta_p(T: npt.NDArray[np.float64], mu: None | float=None) -> npt.NDArray[np.float64]:
        """
        Water vapour permeability [kg/(m.s.Pa)]
        """
        if mu is None:
            mu = Rammed_Earth.mu()
        return lib.delta_a(T) / float(mu)

    @staticmethod
    def Avalue() -> float:
        """
        Liquid absorption coefficient [kg/(m2.s1/2)]
        wf : water content at free saturation [kg/m3] (at the end of the absorption test)
        """
        return 0.37

    @staticmethod
    def wsat() -> float:
        """
        Liquid absorption coefficient [kg/(m2.s1/2)]
        wf : water content at free saturation [kg/m3] (at the end of the absorption test)
        """
        rhoG = 2700     # Grain density [kg/m3]
        return Rammed_Earth.rho() * lib.rhoL * (1./Rammed_Earth.rho() - 1./rhoG)

    @staticmethod
    def delta_l(RH: npt.NDArray[np.float64], RH_table=None, delta_l=None) -> npt.NDArray[np.float64]:
        """
        Liquid water permeability [kg/(m.s.Pa)]
        """

        if RH_table is None:
            RH_table = np.array([0, 0.85, 1])
        else:
            RH_table = np.array(RH_table).astype(float)
        if delta_l is None:
            delta_l = np.array([0, 1e-15, 1e-15])
        else:
            delta_l = np.array(delta_l).astype(float)
        #RH_table = np.array([0, 0.85, 1])
        #delta_l = np.array([0, 1e-15, 1e-15])
        return np.interp(RH, RH_table, delta_l), RH_table, delta_l


class Hempcrete(MaterialTemplate):

    @staticmethod
    def rho() -> int:
        """
        Density of the dry material [kg/m3]
        """
        return 440

    @staticmethod
    def Cp(RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Heat capacity [J.kg-1.K-1]
        with w in kgv/kg
        """
        return 1000 * (260 + 1848 * Hempcrete.w(RH)[0] / Hempcrete.rho()) / Hempcrete.rho()

    @staticmethod
    def k() -> float:
        """
        Thermal conductivity [W.m-1.K-1]
        with w in kgv/kg
        """
        return 0.13

    @staticmethod
    def w(RH: npt.NDArray[np.float64], w=None) -> npt.NDArray[np.float64]:
        """
        Water content [kg.m-3]
        """
        #RH_table = np.array([0, 0.18, 0.41, 0.52, 0.75, 0.83, 1])
        #w_array = np.array([0, 0.027, 0.0304, 0.0387, 0.0812, 0.093, 0.9])
        RH_table = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        if w is None:
            w_array = np.array([0, 0.015, 0.027, 0.028, 0.030, 0.037, 0.053, 0.071, 0.088, 0.425, 0.9])
        else:
            w_array = np.array(w)
        w = Hempcrete.rho()*w_array
        return np.interp(RH, RH_table, w), RH_table, w_array

    @staticmethod
    def mu() -> float:
        """
        Water vapour resistance factor [-]
        """
        return 3.4

    @staticmethod
    def delta_p(T: npt.NDArray[np.float64], mu: None | float=None) -> npt.NDArray[np.float64]:
        """
        Water vapour permeability [kg/(m.s.Pa)]
        """
        if mu is None:
            mu = Hempcrete.mu()
        return lib.delta_a(T)/float(mu)

    @staticmethod
    def delta_l(RH: npt.NDArray[np.float64], RH_table=None, delta_l=None) -> npt.NDArray[np.float64]:
        """
        Liquid water permeability [s] - Assumption
        """
        if RH_table is None:
            RH_table = np.array([0, 0.85, 1])
        else:
            RH_table = np.array(RH_table).astype(float)
        if delta_l is None:
            delta_l = np.array([0.0, 0.0, 0.0])
        else:
            delta_l = np.array(delta_l).astype(float)
        return np.interp(RH, RH_table, delta_l), RH_table, delta_l







