# -*- coding: utf-8 -*-

"""
Boundary conditions reading and treatment
"""
import numpy as np
import numpy.typing as npt

from HT import settings
import HT.library as lib


# Reading the boundary conditions data file
# df_ext = pd.read_excel('HT/' + settings.file, sheet_name=settings.sheet)
# climate_data = df_ext.values

class Boundary:
    def __init__(self, climate_data: npt.NDArray[np.float64], rad_data: npt.NDArray[np.float64] = None):
        # Reading each columns separately
        self.time = climate_data[:, 0]  # Time [s]
        self.Text = climate_data[:, 1] + 273.15  # Exterior temperature [K]
        self.Tint = climate_data[:, 2] + 273.15  # Interior temperature [K]
        self.RHext = climate_data[:, 3] / 100  # Exterior relative humidity [-]
        self.RHint = climate_data[:, 4] / 100  # Interior relative humidity [-]

        # Conversion in vapour pressuere
        self.pvext = lib.pv(self.Text, self.RHext)
        self.pvint = lib.pv(self.Tint, self.RHint)

        # Creation of a matrice which contains the time, the exterior and interior temperature and vapour pressure
        self.boundary = np.transpose(np.vstack((self.time, self.Text, self.Tint, self.pvext, self.pvint)))

        self.t_tot = int(max(self.boundary[:, 0]))  # Total time of the data file
        self.dt = int(self.boundary[1, 0] - self.boundary[0, 0])  # Time step

        # Updating the total time of the data file
        self.t_tot = int(max(self.boundary[:, 0]))

        # Convective heat and mass transfer coefficients
        """
        Convective heat and mass transfer coefficients
        The mass transfer coefficients are calculated with Lewis' analogy
        """
        self.h_ext = 16  # Exterior convective heat transfer coefficient [W.m-2.K-1]
        self.h_int = 6.5  # Interior convective heat transfer coefficient [W.m-2.K-1]
        self.hm_ext = 25e-9  # Exterior convective mass transfer coefficient [kg.m-2.s-1.Pa-1]
        self.hm_int = 25e-9  # Interior convective mass transfer coefficient [kg.m-2.s-1.Pa-1]

        if rad_data is not None:
            self.rad = BoundaryRad(rad_data, self.t_tot, self.Text, self.time)

    def boundary_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the boundary conditions for the adaptative time steping method
        """
        Text = np.interp(dt, self.boundary[:, 0], self.boundary[:, 1])
        Tint = np.interp(dt, self.boundary[:, 0], self.boundary[:, 2])
        pvext = np.interp(dt, self.boundary[:, 0], self.boundary[:, 3])
        pvint = np.interp(dt, self.boundary[:, 0], self.boundary[:, 4])

        return np.vstack((pvext, pvint, Text, Tint))


###############################################################################
# df_rad = pd.read_excel('HT/' + "data_radiation.xlsx", "Feuil1")
# rad_data = df_rad.values
class BoundaryRad:
    def __init__(self, rad_data: npt.NDArray[np.float64], t_tot: int, Text: npt.NDArray[np.float64], time: npt.NDArray[np.float64]):

        self.Text = Text
        self.time = time
        # Reading each columns separately
        self.h = rad_data[:, 1]  # Sun elevation [°]
        self.Az = rad_data[:, 2]  # Sun azimuth (orientation against the North) [°]
        self.DirH = rad_data[:, 3]  # Direct horizontal radiation [W/m2]
        self.DifH = rad_data[:, 4]  # Diffuse horizontal radiation [W/m2]

        # Calculation of the solar time
        """
        Note: the last day of the simulation ends at 0:00 pm
        """

        # Hour numbering over the total simulation time
        self.hour_day = np.linspace(0, 23, 24)  # Creating a vector with the hour numbering for one day
        self.numb_of_day = round(
            t_tot / (3600 * 24))  # Calculating the total number of day in the weather data (start at day 0)
        self.hour_vector = np.tile(self.hour_day,
                                   self.numb_of_day)  # Day's hour vector: "numb_of_day" times concatenation of "hour_day"
        self.hour_vector = np.hstack(self.hour_vector)  # Adding midnight for the last day
        ###############################################################################

        # Day numbering over the total simulation time
        self.day_of_year = np.zeros([24])
        self.day_of_year[:] = 1
        self.day = np.zeros([24])
        self.count_day = 2  # Counter
        while self.count_day <= self.numb_of_day:
            self.day[:] = self.count_day
            self.day_of_year = np.hstack((self.day_of_year, self.day))
            self.count_day += 1

        # Fractional year [rad]
        self.gamma = np.zeros([len(self.hour_vector)])
        for i in range(0, len(self.hour_vector)):
            self.gamma[i] = 2 * np.pi / 365 * (self.day_of_year[i] - 1 + (self.hour_vector[i] - 12) / 24)

        # Equation of time in [s]
        self.eq_time = 60 * 229.18 * (
                0.000075 + 0.001868 * np.cos(self.gamma) - 0.032077 * np.sin(self.gamma) - 0.014615 * np.cos(
            2 * self.gamma) - 0.040849 * np.sin(2 * self.gamma))

        # Apparent solar time in [s]
        self.solar_time = self.time - self.eq_time - 4 * settings.Lon / 60

        ###############################################################################

        # Short-wave radiation parameters
        self.Alb = 0.25  # Albedo of the environment
        self.h = np.pi / 180 * self.h  # Sun zenith (elevation) [rad]
        self.Az = np.pi / 180 * (self.Az - 180)  # Sun azimuth [rad] =>
        self.theta_z = np.pi / 2 - self.h  # Zenith angle [rad]

        # Incident angle on the wall
        self.cos_theta_i = np.cos(self.theta_z) * np.cos(settings.beta) + np.sin(self.theta_z) * np.sin(
            settings.beta) * np.cos(
            self.Az - settings.gamma)

        self.Dir = self.cos_theta_i / np.cos(self.theta_z) * self.DirH  # Direct radiation [W/m2]
        self.Dif = (1 + np.cos(settings.beta)) / 2 * self.DifH  # Diffuse radiation [W/m2]
        self.Ref = (1 - np.cos(settings.beta)) / 2 * self.Alb * (self.DirH + self.DifH)  # Reflected tadiation [W/m2]

        # Safety to keep the irradiation positive
        for i in range(0, len(self.Dir)):
            if self.Dir[i] <= 0:
                self.Dir[i] = 0
            if self.Dif[i] <= 0:
                self.Dif[i] = 0
            if self.Ref[i] <= 0:
                self.Ref[i] = 0
        ###############################################################################

        # Long-wave radiation parameters

        # View factors [-]
        self.Fgro = 0.5  # Ground
        self.Fsky = 0.5  # Sky

        self.Tgro = self.Text  # Ground temperature [K]
        self.Tsky = self.Text - 6  # Sky temperature [K]

    def Dir_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the direct irradiance
        """
        return np.interp(dt, self.solar_time, self.Dir)

    def Dif_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the diffuse irradiance
        """
        return np.interp(dt, self.solar_time, self.Dif)

    def Ref_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the reflected irradiance
        """
        return np.interp(dt, self.solar_time, self.Ref)

    def Tgro_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the ground temperature
        """
        return np.interp(dt, self.time, self.Tgro)

    def Tsky_interp(self, dt: int) -> npt.NDArray[np.float64]:
        """
        Linear interpolation of the sky temperature
        """
        return np.interp(dt, self.time, self.Tsky)

# Reading the radiation data file
