# -*- coding: utf-8 -*-

"""
Algorithm

Coupled heat and moisture transfer solved with finite differences method

Rammed earth wall
"""

###############################################################################
################################### Import ####################################
###############################################################################

# Main libraries
import numpy as np
import numpy.typing as npt
import pandas as pd
import timeit
import ctypes
from typing import Tuple

# Model related imports
from HT import settings
from HT import library as lib
from HT.method import Mass_Coeffs as mc
from HT.method import Energy_Coeffs as ec
from HT.method import Boundary_Coeffs as bc
from HT.method import Matrices as mt
from HT.boundary import Boundary
from HT.materials import Material


def init(bo: Boundary, mesh) -> Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]:

    dx_sum = mesh[4]

    # Exterior surface
    T_ext = bo.Text[0]
    RH_ext = bo.RHext[0]
    pc_ext = lib.pc(T_ext, RH_ext)

    # Interior surface
    T_int = bo.Tint[0]
    RH_int = bo.RHint[0]
    pc_int = lib.pc(T_int, RH_int)

    # Nodes position: exterior, middle of the wall, 10 cm from the interior surface, interior
    dx_wall = np.array([0, 0.5])

    # Initial relative humidities and temperatures
    T_wall = np.array([T_ext, T_int])
    RH_wall = np.array([RH_ext, RH_int])
    pc_wall = np.array([pc_ext, pc_int])

    # Linear interpolation to initialized the fields at each node
    Tini = np.interp(dx_sum, dx_wall, T_wall)
    RHini = np.interp(dx_sum, dx_wall, RH_wall)
    pcini = np.interp(dx_sum, dx_wall, pc_wall)

    # # Initializing the vectors
    T = Tini
    RH = RHini
    pc = pcini

    return T, RH, pc


###############################################################################
############################### Initialization ################################
###############################################################################
# Definition of the initial temperature and relative humidity
def main(p: ctypes.c_double,
         t: ctypes.c_double,
         tsim: npt.NDArray[np.float64],
         T_final: dict,
         RH_final: dict,
         pv_final: dict,
         material: Material,
         bo: Boundary,
         mesh) -> None:
    (T, RH, pc) = init(bo, mesh)
    N_tot = mesh[2]
    # Storing the fiels in [U] containing pc (from 0 to N_tot) and T (from N_tot to 2*N_tot-1)
    U = np.zeros([2 * N_tot, 1])
    U[0:N_tot, 0] = pc[:, 0]
    U[N_tot:2 * N_tot, 0] = T[:, 0]

    # Creating storage lists
    StockT = [T]
    StockRH = [RH]
    Stockpc = [pc]
    Stockw = [material.w(RH)]
    #
    #
    # Initialization of time related parameters
    t_sim = 0  # Simulation time
    dt_sim = bo.dt  # Simulation time step (equal to the boundary conditions time step)
    step_count = 1  # Counter for the time step
    nb_iter = 0  # Number of iteration
    Stockdt = [0]  # Storage of the time step
    #
    #

    #
    #
    # ###############################################################################
    # ################################# Resolution ##################################
    # ###############################################################################
    # """
    # This is where the calculation is done
    # """
    #
    # # Starting the chronometer
    start = timeit.default_timer()
    #
    #
    # # Solving the coupled equations
    if settings.dt_method == 0:
        """
        Constant time stepping method
        """
        while t_sim <= bo.t_tot:
            # Boundary conditions vector
            L = bo.boundary_interp(t_sim + dt_sim)  # T and RH matrice
            Tgro = bo.rad.Tgro_interp(t_sim + dt_sim)  # Ground temperature [K]
            Tsky = bo.rad.Tsky_interp(t_sim + dt_sim)  # Sky temperature [K]
            Dir = bo.rad.Dir_interp(t_sim + dt_sim)  # Direct radiation [W/m2]
            Dif = bo.rad.Dif_interp(t_sim + dt_sim)  # Diffuse radiation [W/m2]
            Ref = bo.rad.Ref_interp(t_sim + dt_sim)  # Reflected radiation [W/m2]

            MC = mc(T, RH, material)
            EC = ec(T, RH, material)
            BC = bc(T, RH)
            MT = mt(T, RH, bo, mesh)
            # Creating matrices M and N
            M = MT.Res(dt_sim, MC.C11(), MC.R11(), MC.R12(), EC.C22(), EC.R22(), EC.R21(),
                       BC.k0(), BC.h_rad_gro(Tgro, bo.rad.Fgro), BC.h_rad_gro(Tgro, bo.rad.Fgro))
            N = (np.dot(MT.Capa(dt_sim, MC.C11(), EC.C22()), U) + np.dot(MT.B(), L)
                 + MT.K(BC.k1())
                 + MT.Rad(Tgro, Tsky, BC.h_rad_gro(Tgro, bo.rad.Fgro), BC.h_rad_sky(Tsky, bo.rad.Fsky), Dir, Dif, Ref))
            #
            # # Solving with LU decomposition
            U = np.linalg.solve(M, N)
            # Solution

            pc = U[0:N_tot]  # Updating vector pc
            T = U[N_tot:2 * N_tot]  # Updating vector T
            RH = np.exp(-pc / (lib.rhoL * lib.Rv * T))  # Calculating the relative humidity
            w = material.w(RH)  # Calculating the water content

            # Safety to keep the relative humidity below 100%
            for i in range(len(RH)):
                if RH[i] > 1.0:
                    RH[i] = 1.0

            # Storing the results
            StockT.append(T)
            StockRH.append(RH)
            Stockpc.append(pc)
            Stockw.append(w)
            Stockdt.append(dt_sim)

            # Updating the simulation time step
            t_sim = t_sim + dt_sim

            # Updating the progress bar
            p.value = step_count / int(bo.t_tot / bo.dt)
            step_count += 1

            if t_sim >= bo.t_tot:
                """
                Safety in case the simulation exceed the total time
                """
                break

    if settings.dt_method == 1:
        """
        Adaptive time stepping method
        """

        while t_sim <= bo.t_tot:

            # Step 1: Coarse calculation from t to t+dt_sim
            # Boundary conditions vector
            L = bo.boundary_interp(t_sim + dt_sim)  # T and RH matrice
            Tgro = bo.rad.Tgro_interp(t_sim + dt_sim)  # Ground temperature [K]
            Tsky = bo.rad.Tsky_interp(t_sim + dt_sim)  # Sky temperature [K]
            Dir = bo.rad.Dir_interp(t_sim + dt_sim)  # Direct radiation [W/m2]
            Dif = bo.rad.Dif_interp(t_sim + dt_sim)  # Diffuse radiation [W/m2]
            Ref = bo.rad.Ref_interp(t_sim + dt_sim)  # Reflected radiation [W/m2]

            MC = mc(T, RH, material)
            EC = ec(T, RH, material)
            BC = bc(T, RH)
            MT = mt(T, RH, bo, mesh)
            # Creating matrices M and N
            M = MT.Res(dt_sim, MC.C11(), MC.R11(), MC.R12(), EC.C22(), EC.R22(), EC.R21(),
                       BC.k0(), BC.h_rad_gro(Tgro, bo.rad.Fgro), BC.h_rad_gro(Tgro, bo.rad.Fgro))
            N = np.dot(MT.Capa(dt_sim, MC.C11(), EC.C22()), U) + np.dot(MT.B(), L) + MT.K(BC.k1())

            # Solving with LU decomposition
            U1 = np.linalg.solve(M, N)  # Solution of the coarse calculation

            pc1 = U1[0:N_tot]  # Extracting vector pc1
            T1 = U1[N_tot:2 * N_tot]  # Extracting vector T1
            RH1 = np.exp(-pc1 / (lib.rhoL * lib.Rv * T1))  # Calculating the relative humidity

            # Safety to keep the relative humidity below 100%
            for i in range(len(RH1)):
                if RH1[i] > 1.0:
                    RH1[i] = 1.0

            # Step 2: Refined calculation => the simulation time step is divided by 2
            dt_sim_div = dt_sim / 2

            # Calculation from t to t + dt_sim/2
            # Boundary conditions vector
            L = bo.boundary_interp(t_sim + dt_sim_div)  # T and RH matrice
            Tgro = bo.rad.Tgro_interp(t_sim + dt_sim_div)  # Ground temperature [K]
            Tsky = bo.rad.Tsky_interp(t_sim + dt_sim_div)  # Sky temperature [K]
            Dir = bo.rad.Dir_interp(t_sim + dt_sim_div)  # Direct radiation [W/m2]
            Dif = bo.rad.Dif_interp(t_sim + dt_sim_div)  # Diffuse radiation [W/m2]
            Ref = bo.rad.Ref_interp(t_sim + dt_sim_div)  # Reflected radiation [W/m2]

            # Creating matrices M and N
            M = MT.Res(dt_sim_div, MC.C11(), MC.R11(), MC.R12(), EC.C22(), EC.R22(), EC.R21(),
                       BC.k0(), BC.h_rad_gro(Tgro, bo.rad.Fgro), BC.h_rad_gro(Tgro, bo.rad.Fgro))
            N = np.dot(MT.Capa(dt_sim_div, MC.C11(), EC.C22()), U) + np.dot(MT.B(), L) + MT.K(BC.k1())

            # Solving with LU decompositon
            Uinterm = np.linalg.solve(M, N)  # Intermediate solution of the refined calculation

            pcinterm = Uinterm[0:N_tot]  # Extracting vector pcinterm
            Tinterm = Uinterm[N_tot:2 * N_tot]  # Extracting vector Tinterm
            RHinterm = np.exp(-pcinterm / (lib.rhoL * lib.Rv * Tinterm))  # Calculating the relative humidity

            # Safety to keep the relative humidity below 100%
            for i in range(len(RHinterm)):
                if RHinterm[i] > 1.0:
                    RHinterm[i] = 1.0

            # Calculation from t + dt_sim/2 to t + dt_sim using Uinterm
            L = bo.boundary_interp(t_sim + 2 * dt_sim_div)  # T and RH matrice
            Tgro = bo.rad.Tgro_interp(t_sim + 2 * dt_sim_div)  # Ground temperature [K]
            Tsky = bo.rad.Tsky_interp(t_sim + 2 * dt_sim_div)  # Sky temperature [K]
            Dir = bo.rad.Dir_interp(t_sim + 2 * dt_sim_div)  # Direct radiation [W/m2]
            Dif = bo.rad.Dif_interp(t_sim + 2 * dt_sim_div)  # Diffuse radiation [W/m2]
            Ref = bo.rad.Ref_interp(t_sim + 2 * dt_sim_div)  # Reflected radiation [W/m2]

            MTinterm = mt(Tinterm, RHinterm, bo, mesh)
            MCinterm = mc(Tinterm, RHinterm, material)
            ECinterm = ec(Tinterm, RHinterm, material)
            BCinterm = bc(Tinterm, RHinterm)

            # Creating matrices M and N
            M = MTinterm.Res(dt_sim_div, MCinterm.C11(), MCinterm.R11(), MCinterm.R12(), ECinterm.C22(),
                       ECinterm.R22(), ECinterm.R21(), BCinterm.k0(), BCinterm.h_rad_gro(Tgro, bo.rad.Fgro),
                       BCinterm.h_rad_gro(Tgro, bo.rad.Fgro))
            N = (np.dot(MTinterm.Capa(dt_sim_div, MCinterm.C11(), ECinterm.C22()), U) + np.dot(MTinterm.B(), L)
                 + MTinterm.K(BCinterm.k1()))

            # Solving with LU decomposition
            U2 = np.linalg.solve(M, N)  # Solution of the refined calculation

            pc2 = U2[0:N_tot]  # Extracting vector pc2
            T2 = U2[N_tot:2 * N_tot]  # Extracting vector T2
            RH2 = np.exp(-pc2 / (lib.rhoL * lib.Rv * T2))  # Calculating the relative humidity
            w2 = material.w(RH2)  # Calculating the water content

            # Safety to keep the relative humidity below 100%
            for i in range(len(RH2)):
                if RH2[i] > 1.0:
                    RH2[i] = 1.0

            # Step 3: Error calculation between U1 and U2
            """
            Errors on the temperature and capillary pressure fields are calculated independently
            The maximum error is selected
            """
            Errpc = max(abs((pc1 - pc2) / pc2))
            ErrT = max(abs((T1 - T2) / T2))
            Err = max(ErrT, Errpc)

            # Step 4: Updating the time step
            if Err > settings.Tol:
                """
                The error is too big
                """
                dt_sim = dt_sim_div
                nb_iter += 1

            else:
                """
                The tolerance criterion is respected => the optimal time step is used
                """
                # Updating the parameters
                U = U2
                T = T2
                RH = RH2
                pc = pc2
                w = w2

                # Updating the simulation time
                t_sim = t_sim + dt_sim
                nb_iter += 1

                if t_sim >= bo.t_tot:
                    """
                    Safety in case the simulation exceed the total time
                    """
                    break

                # Calculation of the optimal time step for the next time step
                dt_opt = dt_sim * (settings.Tol / Err) ** (0.5)

                if dt_opt >= 600:
                    """
                    Maximum time step allowed
                    """
                    dt_opt = 600
                print(t_sim, bo.dt, dt_opt, step_count, dt_sim, Err)
                if (t_sim - bo.dt) + dt_opt >= step_count * bo.dt:
                    """
                    Adjusting the optimal time step to not exceed the boundary data
                    time step, and storing the results
                    """
                    # Adjusting dt_opt and updating the simulation time step
                    dt_opt = step_count * bo.dt - (t_sim - bo.dt)
                    dt_sim = dt_opt

                    # Storing the results
                    StockT.append(T)
                    StockRH.append(RH)
                    Stockpc.append(pc)
                    Stockw.append(w)
                    Stockdt.append(dt_sim)

                    # Updating the time step counter

                    # Updating the progress bar
                    p.value = step_count / int(bo.t_tot / bo.dt)
                    step_count += 1

                else:
                    """
                    Updating the simulation time step
                    """
                    dt_sim = dt_opt

    # Stopping the chronometer
    elapsed = (timeit.default_timer() - start) / 60
    t.value = elapsed

    # Verification of the total simulation time
    t_sim_tot = sum(Stockdt[:])

    # Cumulative time step matrice
    Stocktsim = [0]
    for i in range(0, len(Stockdt) - 1):
        Stocktsim.append(Stocktsim[i] + Stockdt[i + 1])

    Stocktsimd = [x / (24 * 3600) for x in Stocktsim]

    ###############################################################################
    ############################### Post-treatment ################################
    ###############################################################################

    # Conversion in array
    StockTarray = np.asarray(StockT)
    StockRHarray = np.asarray(StockRH)
    Stockpsat = lib.psat(StockTarray)
    Stockpv = StockRH * Stockpsat

    # Calculated temperature, relative humidity and vapour pressure
    x = []
    y = []

    tsim[:] = Stocktsimd

    dx = np.around(mesh[4].flatten(), 4)



    for i in range(len(StockRHarray)):
        for j in range(len(StockRHarray[i])):
            if StockRHarray[i][j][0] >= 1:
                x.append(i)
                y.append(dx[j])

    RH_final["x"] = (np.array(x) * dt_sim) / (24 * 3600)
    RH_final["y"] = y

    df_T = pd.DataFrame(np.reshape(StockTarray, (step_count, N_tot)), columns=dx)
    df_T["Time (day)"] = (df_T.index * dt_sim) / (24 * 3600)
    df_T["Time (day)"] = df_T["Time (day)"].round(2)
    df_T.set_index("Time (day)", inplace=True, drop=True)
    T_final["stock"] = df_T - 273.15

    df_RH = pd.DataFrame(np.reshape(StockRHarray, (step_count, N_tot)), columns=dx)
    df_RH["Time (day)"] = (df_RH.index * dt_sim) / (24 * 3600)
    df_RH["Time (day)"] = df_RH["Time (day)"].round(2)
    df_RH.set_index("Time (day)", inplace=True, drop=True)
    RH_final["stock"] = df_RH * 100

    df_pv = pd.DataFrame(np.reshape(Stockpv, (step_count, N_tot)), columns=dx)
    df_pv["Time (day)"] = (df_pv.index * dt_sim) / (24 * 3600)
    df_pv["Time (day)"] = df_pv["Time (day)"].round(2)
    df_pv.set_index("Time (day)", inplace=True, drop=True)
    pv_final["stock"] = df_pv


