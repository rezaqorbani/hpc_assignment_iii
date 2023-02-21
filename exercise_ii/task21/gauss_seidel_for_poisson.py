import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

def gauss_seidel(f):
    newf = f.copy()
    
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    
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
        for _ in range(max_iter):
            f = gauss_seidel(f)
        end = timer()
        times.append(end-start)

    # export data so that we can plot it in task27.py
    np.savetxt("task21_times.txt", times)
    np.savetxt("Ns.txt", Ns)

    
if __name__ == '__main__':
    main()