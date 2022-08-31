# -*- coding: utf-8 -*-


import numpy as np

from HT import settings
from HT import library as lib


class Mass_Coeffs(object):
    """
    The Mass_Coeffs class creates the coefficients of the mass conservation equation
    """
    def __init__(self, T, RH, material):

        # Initialization: temperature and relative humidity are given here
        self.T = T
        self.RH = RH
        self.mat = material

    def C11(self):
        """
        Coefficients in front of (dpc/dt)
        """
        return self.mat.Xi(self.T, self.RH)

    def R11(self):
        """
        Coefficient in front of (d²pc/self.dx²)
        """
        if settings.liquid_transfer == "liquid_permeability":
            R11 = -(self.mat.delta_l(self.RH) + self.mat.delta_p(self.T) * lib.rhoV(self.T, self.RH) / lib.rhoL)

        if settings.liquid_transfer == "liquid_diffusivity":
            R11 = -(-self.mat.Dw() * self.mat.Xi(self.T, self.RH) * self.RH / (lib.rhoL * lib.Rv * self.T) + self.mat.delta_p(self.T) * lib.rhoV(self.T, self.RH) / lib.rhoL)

        return R11


    def R12(self):
        """
        Coefficient in front of (d²T/self.dx²)
        """
        if settings.liquid_transfer == "liquid_permeability":
            R12 = self.mat.delta_p(self.T) * (self.RH * lib.dpsat(self.T) - lib.pv(self.T, self.RH) * np.log(self.RH) / self.T)

        if settings.liquid_transfer == "liquid_diffusivity":
            R12 = self.mat.delta_p(self.T) * (self.RH * lib.dpsat(self.T) - lib.pv(self.T, self.RH) * np.log(self.RH) / self.T - self.mat.Dw() * self.mat.Xi(self.T, self.RH) * self.RH * np.log(self.RH) / self.T)

        return R12


    ###########################################################################

class Energy_Coeffs(object):
    """
    The Energy_Coeffs class creates the coefficients of the energy conservation equation
    """
    def __init__(self, T, RH, material):
        self.T = T
        self.RH = RH
        self.mat = material

    def C22(self):
        """
        Coefficient in front of (dT/dt)
        """
        return self.mat.rho() * (self.mat.Cp(self.RH) + self.mat.w(self.RH) * lib.CpL)

    def R22(self):
        """
        Coefficient un front of (d²T/self.dx²)
        """
        return self.mat.k() + (lib.CpV * (self.T - 273.15) + lib.Lv) * self.mat.delta_p(self.T) * (self.RH * lib.dpsat(self.T) - lib.pv(self.T, self.RH) * np.log(self.RH) / self.T)

    def R21(self):
        """
        Coefficient in front of (d²pc/self.dx²)²
        """
        return self.mat.delta_l(self.RH) * lib.CpL * self.T - (lib.CpV * (self.T - 273.15) + lib.Lv) * self.mat.delta_p(self.RH) * lib.rhoV(self.T, self.RH) / lib.rhoL


    ###########################################################################

class Boundary_Coeffs(object):
    """
    The Boundary_Coeffs class creates the coefficients for the boundary conditions
    """
    def __init__(self, T, RH):
        self.T = T
        self.RH = RH

    def k0(self):
        """
        Coefficient coming from the linearization of the mass flux
        """
        return -lib.psat(self.T) / (lib.rhoL * lib.Rv *self.T) * np.exp(- lib.pc(self.T, self.RH) / (lib.rhoL * lib.Rv * self.T))

    def k1(self):
        """
        Coefficient coming from the linearization of the mass flux
        """
        return lib.psat(self.T) * np.exp(-lib.pc(self.T, self.RH) / (lib.rhoL * lib.Rv * self.T)) * (1 + lib.pc(self.T, self.RH) / (lib.rhoL * lib.Rv * self.T))

    def h_rad_gro(self, Tgro, Fgro):
        """
        Linearized radiative heat transfer coefficient with the ground
        """
        return Fgro * lib.sigma * lib.epsilon * (self.T[0]**4 - Tgro**4)/(self.T[0] - Tgro)

    def h_rad_sky(self, Tsky, Fsky):
        """
        Linearized radiative heat transfer coefficient with the sky
        """
        return Fsky * lib.sigma * lib.epsilon * (self.T[0]**4 - Tsky**4)/(self.T[0] - Tsky)


        ###########################################################################

class Matrices(object):
    """
    The matrices class creates the matrices to solve the coupled equations
    """
    def __init__(self, T, RH, bo, mesh):
        self.T = T
        self.RH = RH
        self.bo = bo
        self.N_tot = mesh[2]
        self.dx = mesh[0]

    def Res(self, dt, C11, R11, R12, C22, R22, R21, k0, h_rad_gro, h_rad_sky):
        """
        Matrix containing the coefficients associated to the driving potential at the instant "j+1"
        """
        # Initialisation
        Res1 = np.zeros([self.N_tot,self.N_tot])  # 1st quarter: Mass conservation
        Res2 = np.zeros([self.N_tot,self.N_tot])  # 2nd quarter: Influence of heat on water transport
        Res3 = np.zeros([self.N_tot,self.N_tot])  # 3rd quarter: Influence of water on heat transfer
        Res4 = np.zeros([self.N_tot,self.N_tot])  # 4th quarter: Energy conservation

        # General case
        for i in range(1,self.N_tot-1):
            # 1st quarter - Mass conservation
            Res1[i,i+1] = -(R11[i]+R11[i+1])/(self.dx[i+1]*(self.dx[i]+self.dx[i+1]))  # diag +1
            Res1[i,i] = (1./(self.dx[i]+self.dx[i+1])*((R11[i+1]+R11[i])/self.dx[i+1] + (R11[i-1]+R11[i])/self.dx[i])) + C11[i]/dt  # diag
            Res1[i,i-1] = -(R11[i]+R11[i-1])/(self.dx[i]*(self.dx[i]+self.dx[i+1]))    # diag -1

            # 2nd quarter - Influence of heat on water transport
            Res2[i,i+1] = -(R12[i]+R12[i+1])/(self.dx[i+1]*(self.dx[i]+self.dx[i+1]))  # diag +1
            Res2[i,i] = (1./(self.dx[i]+self.dx[i+1])*((R12[i+1]+R12[i])/self.dx[i+1] + (R12[i-1]+R12[i])/self.dx[i]))    # diag
            Res2[i,i-1] = -(R12[i]+R12[i-1])/(self.dx[i]*(self.dx[i]+self.dx[i+1]))    # diag -1

            # 3rd quarter - Influence of water transport on energy conservation
            Res3[i,i+1] = -(R21[i]+R21[i+1])/(self.dx[i+1]*(self.dx[i]+self.dx[i+1]))  # diag +1
            Res3[i,i] = (1./(self.dx[i]+self.dx[i+1])*((R21[i+1]+R21[i])/self.dx[i+1] + (R21[i-1]+R21[i])/self.dx[i]))  # diag
            Res3[i,i-1] = -(R21[i]+R21[i-1])/(self.dx[i]*(self.dx[i]+self.dx[i+1]))    # diag -1

            # 4th quarter - Energy conservation
            Res4[i,i+1] = -(R22[i]+R22[i+1])/(self.dx[i+1]*(self.dx[i]+self.dx[i+1]))  # diag +1
            Res4[i,i] = (1./(self.dx[i]+self.dx[i+1])*((R22[i+1]+R22[i])/self.dx[i+1] + (R22[i-1]+R22[i])/self.dx[i])) + C22[i]/dt  # diag
            Res4[i,i-1] = -(R22[i]+R22[i-1])/(self.dx[i]*(self.dx[i]+self.dx[i+1]))    # diag -1

        # Neuman boundary conditions

        # 1st quarter - Mass conservation
        # Exterior surface
        Res1[0,1] = -2*R11[0]/self.dx[1]**2  # diag +1
        Res1[0,0] = 2*R11[0]/self.dx[1]**2 + C11[0]/dt + 2*self.bo.hm_ext*k0[0]/self.dx[1]   # diag
        # Interior surface
        Res1[self.N_tot-1,self.N_tot-2] = -2*R11[self.N_tot-1]/self.dx[self.N_tot-1]**2  # diag -1
        Res1[self.N_tot-1,self.N_tot-1] = 2*R11[self.N_tot-1]/self.dx[self.N_tot-1]**2 + C11[self.N_tot-1]/dt+ 2*self.bo.hm_int*k0[self.N_tot-1]/self.dx[self.N_tot-1]    # diag

        # 2nd quarter - Influence of heat on water transport
        # Exterior surface
        Res2[0,1] = -2*R12[0]/self.dx[1]**2     # diag +1
        Res2[0,0] = 2*R12[0]/self.dx[1]**2      # diag
        # Interior surface
        Res2[self.N_tot-1,self.N_tot-2] = -2*R12[self.N_tot-1]/self.dx[self.N_tot-1]**2     # diag +1
        Res2[self.N_tot-1,self.N_tot-1] = 2*R12[self.N_tot-1]/self.dx[self.N_tot-1]**2      # diag

        # 3rd quarter - Influence of water on heat transfer
        # Exterior surface
        Res3[0,1] = -2*R21[0]/self.dx[1]**2     # diag +1
        Res3[0,0] = 2*R21[0]/self.dx[1]**2 + 2*(lib.CpV*(self.T[0]-273.15)+lib.Lv)*self.bo.hm_ext*k0[0]/self.dx[1]      # diag
        # Interior surface
        Res3[self.N_tot-1,self.N_tot-2] = -2*R21[self.N_tot-1]/self.dx[self.N_tot-1]**2   # diag -1
        Res3[self.N_tot-1,self.N_tot-1] = 2*R21[self.N_tot-1]/self.dx[self.N_tot-1]**2 + 2*(lib.CpV*(self.T[self.N_tot-1]-273.15)+lib.Lv)*self.bo.hm_int*k0[self.N_tot-1]/self.dx[self.N_tot-1]    # diag

        # 4th quarter - Energy conservation
        # Exterior surface
        Res4[0,1] = -2*R22[0]/self.dx[1]**2   # diag +1
        Res4[0,0] = 2*R22[0]/self.dx[1]**2 + C22[0]/dt + 2*(self.bo.h_ext+h_rad_gro+h_rad_sky)/self.dx[1]   # diag
        # Interior surface
        Res4[self.N_tot-1,self.N_tot-2] = -2*R22[self.N_tot-1]/self.dx[self.N_tot-1]**2   # diag -1
        Res4[self.N_tot-1,self.N_tot-1] = 2*R22[self.N_tot-1]/self.dx[self.N_tot-1]**2 + C22[self.N_tot-1]/dt + 2*self.bo.h_int/self.dx[self.N_tot-1]  # diag

        # Intermediate concatenation
        Res13 = np.vstack((Res1,Res3))
        Res24 = np.vstack((Res2,Res4))

        return np.hstack((Res13,Res24))

    def Capa(self, dt, C11, C22):
        """
        Matrix contaning the coefficients associated to the driving potential at the instant "i"
        """
        # Initialisation of each quarter
        Capa1 = np.zeros([self.N_tot,self.N_tot])     # 1st quarter: Mass conservation
        Capa2 = np.zeros([self.N_tot,self.N_tot])     # 2nd quarter: Influence of heat on water transport
        Capa3 = np.zeros([self.N_tot,self.N_tot])     # 3rd quarter: Influence of water on heat transfer
        Capa4 = np.zeros([self.N_tot,self.N_tot])     # 4th quarter: Energy conservation

        # Writing
        # 1st quarter - Mass conservation
        Capa1 = C11/dt * np.diag(np.ones(self.N_tot),0)

        # 4th quarter - Energy conservation
        Capa4 = C22/dt * np.diag(np.ones(self.N_tot),0)

        # Intermediate concatenation
        Capa13 = np.vstack((Capa1,Capa3))
        Capa24 = np.vstack((Capa2,Capa4))

        return np.hstack((Capa13,Capa24))

    def B(self):
        """
        Matrix associated with the boundary conditions
        """
        # Intialization
        B = np.zeros([2*self.N_tot,4])

        # Writing
        # 1st quarter - Mass conservation boundary condition
        B[0,0] = 2 * self.bo.hm_ext / self.dx[1]                  # Exterior surface
        B[self.N_tot-1,1] = 2 * self.bo.hm_int / self.dx[self.N_tot-1]      # Interior surface

        # 3rd quarter - Influence of water on heat transfer
        B[self.N_tot,0] = 2 * (lib.CpV * (self.T[0] - 273.15) + lib.Lv) * self.bo.hm_ext / self.dx[1]                   # Exterior surface
        B[2*self.N_tot-1,1] = 2 * (lib.CpV * (self.T[self.N_tot-1] - 273.15) + lib.Lv) * self.bo.hm_int / self.dx[self.N_tot-1]   # Interior surface

        # 4th quarter - Energy conservation boundary condition
        B[self.N_tot,2] = 2 * self.bo.h_ext / self.dx[1]               # Exterior surface
        B[2*self.N_tot-1,3] = 2 * self.bo.h_int / self.dx[self.N_tot-1]     # Interior surface


        return B

    def K(self, k1):
        """
        Vector coming from the linearization of the boundary conditions
        """
        # Initialization
        K = np.zeros([2*self.N_tot,1])
        """
        Exterior wall 
        """
        # Writing
        # 1st quarter - Mass conservation boundary conditions linearisation
        K[0] = -2 * self.bo.hm_ext * k1[0] / self.dx[1]                      # Exterior surface
        K[self.N_tot-1] = -2 * self.bo.hm_int * k1[self.N_tot-1] / self.dx[self.N_tot-1]    # Interior surface

        # 3rd quarter - Energy conservation boundary conditions linearisation (latent)
        K[self.N_tot] = -2 * (lib.CpV * (self.T[0] - 273.15) + lib.Lv) * self.bo.hm_ext * k1[0] / self.dx[1]                        # Exterior surface
        K[2*self.N_tot-1] = -2 * (lib.CpV * (self.T[self.N_tot-1] - 273.15) + lib.Lv) * self.bo.hm_int * k1[self.N_tot-1] / self.dx[self.N_tot-1]  # Interior surface

        return K

    def Rad(self, Tgro, Tsky, h_rad_gro, h_rad_sky, Dir, Dif, Ref):
        """
        Vector coming from the linearization of the boundary conditions
        """
        # Initialization
        Rad = np.zeros([2*self.N_tot, 1])

        # Writing
        Rad[self.N_tot] = 2 * h_rad_gro / self.dx[1] * Tgro + 2 * h_rad_sky / self.dx[1] * Tsky + 2*lib.kappa*(Dir + Dif + Ref)/self.dx[1]

        return Rad




