import numpy as np
from scipy.integrate import quad, simpson, trapezoid

a, b = 0, 1
n = 1000

x = np.linspace(a, b, n + 1)
y = np.exp(x**2)

trap_result = trapezoid(y, x)
print(f"Trapezoidal Rule: {trap_result:.15f}")

simp_result = simpson(y, x)
print(f"Simpson's Rule:   {simp_result:.15f}")

gauss_result, error = quad(lambda x: np.exp(x**2), a, b)
print(f"Gaussian Quad:    {gauss_result:.15f}")
