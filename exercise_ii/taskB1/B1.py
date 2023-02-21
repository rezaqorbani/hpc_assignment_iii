import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import ctypes


def main():
    _libgauss_seidel = ctypes.CDLL('./gauss_seidel.so')
    _libgauss_seidel.gauss_seidel.argtypes = [ctypes.POINTER(ctypes.c_double),
                             ctypes.c_int,
                             ctypes.c_int]
    _libgauss_seidel.gauss_seidel.restype = None

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
        for _ in range(max_iter):
            _libgauss_seidel.gauss_seidel(f.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                             N,
                             N) 
        end = timer()
        times.append(end-start)
       

        
        

    plt.plot(Ns, times)
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.show()
    
if __name__ == '__main__':
    main()