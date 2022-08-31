# -*- coding: utf-8 -*-

"""
Initializing the model parameters and defining global variables
"""


import numpy as np


# Geographical parameters
Lon = 5.2167      # Longitude of Saint-Antoine l'Abbaye

# Wall configuration
beta = np.pi/180 * 90   # Inclination of the wall
gamma = np.pi/180 * 0   # Orientation of the wall against the South - positive in the West direction

# Wall composition
Nb_layer = 3            # Number of layers
#emat = np.array([0.5])  # Thickness of each layer [m]
emat = np.array([1, 1, 1])


# Property for liquid transfer => "liquid_permeability" or "liquid_diffusivity
liquid_transfer = "liquid_permeability"


# Boundary conditions data
file = "data_air.xlsx"
sheet = "Feuil1"

# Mesh option
    # 0 => uniform
    # 1 => refined
Mesh_Opt = 1

# Time step method
    # 0 => constant
    # 1 => adaptive
dt_method = 0
Tol = 1e-2  # Tolerance for the adaptive time stepping method














