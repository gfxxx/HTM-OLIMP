# -*- coding: utf-8 -*-

"""
Constants and functions
"""

import numpy as np
import numpy.typing as npt
from typing import Callable
from scipy.misc import derivative  # type: ignore


def partial_derivative(func: Callable, var: int = 0, point: list=[]):
    """
    Partial derivative function
    """
    args = point[:]

    def wraps(x):
        args[var] = x
        return func(*args)

    d = derivative(wraps, point[var], dx=1e-6)
    return d


# Constants
T_ref = 273.15  # Reference temperature [K] => 0°C
R = 8.314  # Ideal gas constant [J.kg-1.K-1]
Patm = 101325.  # Atmospheric pressure [Pa]

# Properties of air
Ra = 287.1  # Ideal gas consant of dry air [J.kg-1.K-1]
CpA = 1004.  # Heat capacity of air [J.kg-1.K-1]

# Properties of liquid water
rhoL = 1000.  # Density of liquid water [kg.m-3]
CpL = 4180.  # Heat capacity of liquid water [J.kg-1.K-1]
Mw = 18e-3  # Molar mass of water [kg.mol-1]
eta = 1e-3  # Dynamic viscosity of water [Pa.s]

# Properties of water vapour
# Vapour pressure is defined as a function of both T and RH at the end of this file
CpV = 1850.  # Heat capacity of water vapour [J.kg-1.K-1]
Lv = 2.5e6  # Latent heat of evaporation at 0°C [J.kg-1]
Rv = 461.5  # Ideal gas consant of water vapour [J.kg-1.K-1]

# Constants regarding the radiative heat transfer
epsilon = 0.9  # Emissivity
kappa = 0.55  # Absorptivity
sigma = 5.67e-8  # Stefan-Boltzmann constant [W/(m2.K4)]


def pc(T: npt.NDArray[np.float64], RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Capillary pressure [Pa] (choosen positive)
    Calculated with Gibbs' law
    """
    return -np.log(RH) * rhoL * Rv * T


def psat(T: npt.NDArray[np.float64]) -> npt.NDArray[np.int64]:
    """
    Water vapour saturation pressure  [Pa]
    ISO 7730
    """
    return 1000 * np.exp(16.6536 - 4030.183 / (T - T_ref + 235))


def dpsat(T: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Derivative of the water vapour saturation pressure over the temperature
    """
    return derivative(psat, T, dx=1.0)


def pv(T: npt.NDArray[np.float64], RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Vapour pressure [Pa]
    """
    return RH * psat(T)


def rhoV(T: npt.NDArray[np.float64], RH: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Density of vapour pressure [kg.m-3]
    """
    return pv(T, RH) / (Rv * T)


def rhoA(T: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Density of air [kg.m-3]
    """
    print(Patm / (Ra * T))
    return Patm / (Ra * T)


def delta_a(T: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Air diffusion coefficient [kg/(m.s.Pa)]
    Expression from Kunzel's thesis 1995
    """
    return 2e-7 * T ** 0.81 / Patm
