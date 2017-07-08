import numpy
import math
from matplotlib import pyplot

N = 200                               # Number of points in each direction
x_start, x_end = -4.0, 4.0            # x-direction boundaries
y_start, y_end = -2.0, 2.0            # y-direction boundaries
x = numpy.linspace(x_start, x_end, N) # 1D-array for x
y = numpy.linspace(y_start, y_end, N) # 1D-array for y
X, Y = numpy.meshgrid(x,y)            # generates a mesh grid

u_inf = 1.0                           # freestream speed

# compute the freestream velocity field
u_freestream = u_inf * numpy.ones((N,N), dtype=float)
v_freestream = numpy.zeros((N,N), dtype=float)

# compute the stream-function
psi_freestream = u_inf * Y


