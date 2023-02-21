``import numpy as np
cimport numpy as np
import array
from timeit import default_timer as timer
import sys



def cal_bw_numpy(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE):


    cdef double[:] a = np.empty(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    cdef double[:] b = np.empty(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    cdef double[:] c = np.empty(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    cdef double scalar = 2.0
    cdef double[:] times = np.zeros(4, dtype=np.float64)

    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0

    # copy
    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = timer() - times[1]

    #sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]

    # calculate the bandwidth
    copy_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    scale_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    sum_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    triad_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)

    copy_bw = copy_bytes/times[0]/1e9
    scale_bw = scale_bytes/times[1]/1e9
    sum_bw = sum_bytes/times[2]/1e9
    triad_bw = triad_bytes/times[3]/1e9

    return copy_bw, scale_bw, sum_bw, triad_bw


def cal_bw_array(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE):


    a = [0.0]*STREAM_ARRAY_SIZE
    b = [0.0]*STREAM_ARRAY_SIZE
    c = [0.0]*STREAM_ARRAY_SIZE
    cdef double scalar = 2.0
    cdef double[:] times = np.zeros(4, dtype=np.float64)

    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    scalar = 2.0

    times = np.zeros(4, dtype=np.float64)

    # copy
    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = timer() - times[1]

    #sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]

    # calculate the bandwidth
    copy_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    scale_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    sum_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    triad_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)

    copy_bw = copy_bytes/times[0]/1e9
    scale_bw = scale_bytes/times[1]/1e9
    sum_bw = sum_bytes/times[2]/1e9
    triad_bw = triad_bytes/times[3]/1e9

    return copy_bw, scale_bw, sum_bw, triad_bw

def cal_bw_list( STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE):

    a = [0.0]*STREAM_ARRAY_SIZE
    b = [0.0]*STREAM_ARRAY_SIZE
    c = [0.0]*STREAM_ARRAY_SIZE
    cdef double scalar = 2.0
    cdef double[:] times = np.zeros(4, dtype=np.float64)

    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0

    # copy
    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = timer() - times[1]

    #sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]

    # calculate the bandwidth
    copy_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    scale_bytes = 2*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    sum_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)
    triad_bytes = 3*STREAM_ARRAY_SIZE*sys.getsizeof(STREAM_ARRAY_TYPE)

    copy_bw = copy_bytes/times[0]/1e9
    scale_bw = scale_bytes/times[1]/1e9
    sum_bw = sum_bytes/times[2]/1e9
    triad_bw = triad_bytes/times[3]/1e9

    return copy_bw, scale_bw, sum_bw, triad_bw

def cal_bw(array_type, STREAM_ARRAY_SIZES, STREAM_ARRAY_TYPE):
    copy_bw_list = [0.0] * len(STREAM_ARRAY_SIZES)
    scale_bw_list = [0.0] * len(STREAM_ARRAY_SIZES)
    sum_bw_list =   [0.0] * len(STREAM_ARRAY_SIZES)
    triad_bw_list = [0.0] * len(STREAM_ARRAY_SIZES)


    for i, size in enumerate(STREAM_ARRAY_SIZES):
        if array_type == 'numpy':
            copy_bw, scale_bw, sum_bw, triad_bw = cal_bw_numpy(size, STREAM_ARRAY_TYPE)
        elif array_type == 'array':
            copy_bw, scale_bw, sum_bw, triad_bw = cal_bw_array(size, STREAM_ARRAY_TYPE)
        elif array_type == 'list':
            copy_bw, scale_bw, sum_bw, triad_bw = cal_bw_list(size, STREAM_ARRAY_TYPE)
        else:
            print('wrong array type')
            return
        copy_bw_list[i] = copy_bw
        scale_bw_list[i] = scale_bw
        sum_bw_list[i] = sum_bw
        triad_bw_list[i] = triad_bw

    return copy_bw_list, scale_bw_list, sum_bw_list, triad_bw_list

