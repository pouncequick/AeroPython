import numpy
import matplotlib.pyplot as plt

x = 5
y = 5.0
z = 'five'

a = numpy.array([1,2,3])
b = a
b[1] = 7
print(a)
print(b)

a = numpy.array([1,2,3])
b = a.copy()
b[1] = 7
print(a)
print(b)

print(type(x))
print(type(y))
print(type(z))

my_array = numpy.linspace(0,5,10)
print(my_array)

x = my_array
y = x**2

plt.plot(x,y)
plt.show()

