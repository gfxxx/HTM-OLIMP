# -*- coding: utf-8 -*-

"""
Creation of the mesh grid
"""


import numpy as np


def Mesh(Mesh_Opt, emat, nb_layer):

    if Mesh_Opt == 0:
        """
        Creation of an uniform mesh grid
        """
        # Setting the meshes size [m]
        size = 1e-2

        # Number of nodes
        N_nodes = np.zeros([len(emat),1])
        for i in range(len(emat)):
           N_nodes[i] = emat[i]/size

        # Total number of nodes
        N_tot = int(sum(N_nodes[:]))

        # Creation of the mesh grid
        dx = np.zeros([N_tot,1])
        dx[:] = size
        dx_surf = 0
        dx = np.vstack((dx_surf, dx))

        # Updating the parameters
        N_nodes = np.zeros([len(emat),1])
        N_nodes[:] = len(dx)
        N_tot = len(dx)

        # Cumulative meshes size vector
        N_sum = np.zeros([nb_layer+1,1])
        N_sum[0] = 0
        for i in range(0,nb_layer):
            N_sum[i+1] = N_nodes[i] + N_sum[i]


    if Mesh_Opt == 1:
        """
        Creation of a refined mesh grid at the surface of the wall
        """
        # Refined mesh grid parameters
        u0 = 5e-4       # Meshes thickness at the interface [m] = first term of the geometrical serie
        q = 1.10        # Common ratio of the geometrical serie
        Tol = 2         # Tolerance factor for the mesh in the middle

        # Number of nodes in each layer
        N_nodes = np.zeros([nb_layer,1])

        for i in range(0, nb_layer):
            N_nodes[i] = 2*int(np.log(1-emat[i]/(2*u0)*(1-q))/np.log(q)-1)

            j = 1           # Initialization of the counter for the additional meshes
            m = 2           # Initialization of the parameter for the meshes thickness in the middle of the layer
            test = False    # Test 'True'/'False' for the number of nodes

            while test == False:

                dx = np.zeros([int(N_nodes[i]),1])  # Initialization
                dx[0] = u0                          # First mesh

                for k in range(0, int(N_nodes[i]/2)-j-1):
                    dx[k+1] = q*dx[k]                       # Creation of the successive meshes in the first half of the layer's thickness
                res = (emat[i] - sum(2*dx[:]))     # Calculation of the residual thickness

                for l in range(1,j+1):
                    dx[int(N_nodes[i]/2)-l] = res/m    # Adding the residual thickness to the mesh in the middle of the layer

                if dx[int(N_nodes[i]/2)-j] >= Tol*dx[int(N_nodes[i]/2)-j-1]:
                    test = False                # The condition is not respected, the grid is created with more meshes
                    N_nodes[i] = N_nodes[i]+2   # The number of nodes in the layer is increased by 2
                    j += 1
                    m = 2*m
                else:
                    test = True     # The condition is respected, the mesh grid is kept

                dx_flip = np.flipud(dx)     # Reversing the dx vector (second half of the layer's thickness)
                dx = dx + dx_flip           # Creation of the final mesh grid vector in the layer i

            # Storing the mesh grid in each layer
            if i == 0:
                dx_list = dx
            else:
                dx_list = np.vstack((dx_list, dx))

        dxsurf = 0  # The first node is at the surface of the wall

        # Updating the mesh grid parameters
        N_nodes[0] = N_nodes[0] + 1  # +1 to consider 'dxsurf'
        N_tot = len(dx_list) + 1

        dx = np.vstack((dxsurf, dx_list))

        # Cumulative meshes size vector
        N_sum = np.zeros([nb_layer+1,1])
        N_sum[0] = 0
        for i in range(0,nb_layer):
            N_sum[i+1] = N_nodes[i] + N_sum[i]

    # Defining the cumulative meshes vector
    dx_sum = np.zeros([int(N_tot), 1])
    dx_sum[0] = dx[0]
    for i in range(len(dx)):
        dx_sum[i] = dx_sum[i - 1] + dx[i]

    return dx, N_nodes, N_tot, N_sum, dx_sum


# Extracting the parameters from the Mesh function
# dx = Mesh(Mesh_Opt)[0]
# N_nodes = Mesh(Mesh_Opt)[1]
# N_tot = Mesh(Mesh_Opt)[2]
# N_sum = Mesh(Mesh_Opt)[3]












