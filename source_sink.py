import math
import numpy
from matplotlib import pyplot

N = 50                                       # number of points in each direction
x_start, x_end = -2.0, 2.0                   # boundaries in the x-direction
y_start, y_end = -1.0, 1.0                   # boundaries in the y-direction
x = numpy.linspace(x_start, x_end, N)        # creates a 1D-array with the x-coordinates
y = numpy.linspace(y_start, y_end, N)        # creates a 1D-array with the y-coordinates

X, Y = numpy.meshgrid(x, y)                  # generates a mesh grid

strength_source = 5.0                        # strength of source
x_source, y_source = -1.0, 0.0               # location of the source
strength_sink = -5.0                         # strength of sink
x_sink, y_sink = 1.0, 0.0                    # location of the sink

# compute the velocity field on the mesh grid
u_source = strength_source/(2*math.pi) * (X-x_source)/((X-x_source)**2 + (Y-y_source)**2)
v_source = strength_source/(2*math.pi) * (Y-y_source)/((X-x_source)**2 + (Y-y_source)**2)
u_sink = strength_sink/(2*math.pi) * (X-x_sink)/((X-x_sink)**2 + (Y-y_sink)**2)
v_sink = strength_sink/(2*math.pi) * (Y-y_sink)/((X-x_sink)**2 + (Y-y_sink)**2)

# compute the velocity of the pair source/sink by superposition
u_pair = u_source + u_sink
v_pair = v_source + v_sink

# plotting
size = 10
pyplot.figure(figsize =(size, (y_end-y_start)/(x_end-x_start)*size))
pyplot.xlabel('x', fontsize = 16)
pyplot.ylabel('y', fontsize = 16)
pyplot.xlim(x_start, x_end)
pyplot.ylim(y_start, y_end)
# plot the grid of points
# pyplot.scatter(X, Y, s=10, color='#CD2305', marker='o', linewidth=0)
# plot the streamlines
# pyplot.streamplot(X, Y, u_source, v_source, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
# pyplot.scatter(x_source, y_source, color='#CD2305', s=80, marker='o', linewidth=0)
# pyplot.streamplot(X, Y, u_sink, v_sink, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
# pyplot.scatter(x_sink, y_sink, color='#CD2305', s=80, marker='o', linewidth=0)
pyplot.streamplot(X, Y, u_pair, v_pair, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
pyplot.scatter([x_source, x_sink], [y_source, y_sink],
		 color='#CD2305', s=80, marker='o', linewidth=0)
pyplot.show()
