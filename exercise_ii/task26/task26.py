import numpy as np
import cupy as cp
from timeit import default_timer as timer
from matplotlib import pyplot as plt

def gauss_seidel(f):
    newf = f.copy()
    # use nump.roll to shift the array
    newf = (np.roll(newf, 1, axis=0) + np.roll(newf, -1, axis=0) + np.roll(newf, 1, axis=1) + np.roll(newf, -1, axis=1))*0.25
    return newf

def main():
    Ns = [10, 20, 40, 80, 160, 320, 640]
    times = []
    max_iter = 1000
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

    # export data so that we can plot it in task27.py
    np.savetxt("times.txt", times)
    np.savetxt("Ns.txt", Ns)


main()