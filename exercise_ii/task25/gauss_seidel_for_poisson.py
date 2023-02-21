import torch
from timeit import default_timer as timer
from matplotlib import pyplot as plt
# We solve Poisson's equation by it to convergence by a forward time-centered space differencing (FTCS) on a grid using the Gauss-Seidel Method:
# We discretize the function f on a square box of size 1.
# We use a uniform grid with N grid points in the x-direction and N grid points in the y-direction. 
# We impose the values at the boundary equal to zero.
# We have no source S
# We initialize the simulation with random numbers

def gauss_seidel(f):
    newf = f.clone()
    
    # use torch.roll to shift the tensor
    newf = (torch.roll(newf, 1, 0) + torch.roll(newf, -1, 0) + torch.roll(newf, 1, 1) + torch.roll(newf, -1, 1))*0.25

    return newf

def main():
    Ns = [10, 20, 40, 80, 160, 320, 640]
    times = []
    max_iter = 1000
    for N in Ns:
        f = torch.rand(N, N).cuda()

        f[0,:] = 0
        f[-1,:] = 0
        f[:,0] = 0
        f[:,-1] = 0
        start = timer()
        for i in range(max_iter):
            f = gauss_seidel(f)
        end = timer()
        times.append(end-start)

    # export data so that we can plot it in task27.py with matplotlib
    torch.save(torch.tensor(times), "times.pt")
    torch.save(torch.tensor(Ns), "Ns.pt")

    


if __name__ == '__main__':
    main()