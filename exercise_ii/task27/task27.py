import matplotlib.pyplot as plt
import numpy as np
import torch

# load data
task21_times = np.loadtxt("./task21_times.txt")
task24_times = np.loadtxt("./task24_times.txt")
task25_times = torch.load("./task25_times.pt")
task26_times = np.loadtxt("./task26_times.txt")
Ns = np.loadtxt("Ns.txt")

# plot the plot in the same figure with different colors, legend and labels
plt.plot(Ns, task21_times, label="Numpy (for loop)", color="red")
plt.plot(Ns, task24_times, label="Cythonized Numpy (for loop)", color="blue")
plt.plot(Ns, task25_times, label="PyTorch (.roll())", color="green")
plt.plot(Ns, task26_times, label="CuPy (.roll())", color="orange")
plt.legend()
plt.xlabel("Grid width (N)")
plt.ylabel("time (s)")
plt.show()