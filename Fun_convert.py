import sympy
import numpy

x = sympy.Symbol('x')
y = input("Введите функцию f(x): ")
y_f = input("Произвести дифференцирвание - 'd', интегрирование - 'i': ")
d = numpy.arange(-10, 10, 0.5)

if y_f == 'd':
    print(sympy.diff(y), x)
elif y_f == "i":
    print(sympy.integrate(y), x)
else:
    print("1")
