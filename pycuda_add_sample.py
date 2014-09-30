import numpy
import pycuda.autoinit
import pycuda.driver as drv


from pycuda.compiler import SourceModule
mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(1024).astype(numpy.float32)
b = numpy.random.randn(1024).astype(numpy.float32)

dest = numpy.zeros_like(a)
multiply_them(
        drv.Out(dest), drv.In(a), drv.In(b),
        block=(1024,1,1), grid=(1,1))

print a*b
print dest
print dest-a*b

