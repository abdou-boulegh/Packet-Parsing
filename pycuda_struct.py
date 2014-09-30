import numpy
 
import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
from pycuda.gpuarray import to_gpu
 

#Definition of the Struct
#Cuda Kernel
mod = SourceModule("""
typedef struct _pair
{
int first;
int second;
} pair;
 
__global__ void get_second(int *dest, pair src)
{
const int i = threadIdx.x;
dest[i] = src.second;
}
""")
 
#Gettint the Kernel function
get_second = mod.get_function("get_second")

dtype = numpy.dtype([('first', numpy.int32), ('second', numpy.int32)])
pair_arr = numpy.empty(1, dtype)
pair_arr['first'][0] = 1
pair_arr['second'][0] = 2

pair = pair_arr[0:1]
dest = to_gpu(numpy.empty(400, numpy.int32))

get_second(dest, pair, block=(400,1,1), grid=(1,1))
print dest[0] 
assert dest.get()[0] == 2