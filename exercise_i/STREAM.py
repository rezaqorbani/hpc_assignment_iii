import numpy as np
import array
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
from cythonfn import cal_bw
# this script is meant to test STREAM Benchmark in Python to Measure the Memory Bandwidth
# of the system using three different methods: numpy, array and list



def main():
    STREAM_ARRAY_SIZES = [100, 1000, 10000, 100000, 1000000, 10000000]
    STREAM_ARRAY_TYPE = np.float64
    figure, ax = plt.subplots(3, 1, figsize=(10, 10))
    # calculate the bandwidth using all three types of lists and plot the results with log scale

    # numpy
    copy_bw, scale_bw, sum_bw, triad_bw = cal_bw('numpy', STREAM_ARRAY_SIZES, STREAM_ARRAY_TYPE)
    ax[0].plot(STREAM_ARRAY_SIZES, copy_bw, label='copy')
    ax[0].plot(STREAM_ARRAY_SIZES, scale_bw, label='scale')
    ax[0].plot(STREAM_ARRAY_SIZES, sum_bw, label='sum')
    ax[0].plot(STREAM_ARRAY_SIZES, triad_bw, label='triad')
    ax[0].set_title('numpy')
    ax[0].set_xlabel('Array Size')
    ax[0].set_ylabel('Bandwidth (GB/s)')
    ax[0].legend()

    # array
    copy_bw, scale_bw, sum_bw, triad_bw = cal_bw('array', STREAM_ARRAY_SIZES, STREAM_ARRAY_TYPE)
    ax[1].plot(STREAM_ARRAY_SIZES, copy_bw, label='copy')
    ax[1].plot(STREAM_ARRAY_SIZES, scale_bw, label='scale')
    ax[1].plot(STREAM_ARRAY_SIZES, sum_bw, label='sum')
    ax[1].plot(STREAM_ARRAY_SIZES, triad_bw, label='triad')
    ax[1].set_title('array')
    ax[1].set_xlabel('Array Size')
    ax[1].set_ylabel('Bandwidth (GB/s)')
    ax[1].legend()

    # list
    copy_bw, scale_bw, sum_bw, triad_bw = cal_bw('list', STREAM_ARRAY_SIZES, STREAM_ARRAY_TYPE)
    ax[2].plot(STREAM_ARRAY_SIZES, copy_bw, label='copy')
    ax[2].plot(STREAM_ARRAY_SIZES, scale_bw, label='scale')
    ax[2].plot(STREAM_ARRAY_SIZES, sum_bw, label='sum')
    ax[2].plot(STREAM_ARRAY_SIZES, triad_bw, label='triad')
    ax[2].set_title('list')
    ax[2].set_xlabel('Array Size')
    ax[2].set_ylabel('Bandwidth (GB/s)')
    ax[2].legend()

    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    main()
    