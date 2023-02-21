import numpy as np
from cythonfn import gauss_seidel
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import h5py
# We solve Poisson's equation by it to convergence by a forward time-centered space differencing (FTCS) on a grid using the Gauss-Seidel Method:
# We discretize the function f on a square box of size 1.
# We use a uniform grid with N grid points in the x-direction and N grid points in the y-direction. 
# We impose the values at the boundary equal to zero.
# We have no source S
# We initialize the simulation with random numbers


def main():
    Ns = [10, 20, 40, 80, 160, 320, 640]
    times = []
    max_iter = 1000
    new_grids = h5py.File('new_grids.hdf5', 'w')
    # create an attribute for the number of iterations
    new_grids.attrs['max_iter'] = max_iter

    for N in Ns:
        f = np.random.rand(N,N)

        f[0,:] = 0
        f[-1,:] = 0
        f[:,0] = 0
        f[:,-1] = 0
        start = timer()
        for i in range(max_iter):
            f = gauss_seidel(f)
        end = timer()
        times.append(end-start)
        # save the grid to the hdf5 file
        new_grids.create_dataset(str(N), data=f)
        new_grids[str(N)].attrs["N"] = N
        


    plt.plot(Ns, times)
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.show()


if __name__ == '__main__':
    main()