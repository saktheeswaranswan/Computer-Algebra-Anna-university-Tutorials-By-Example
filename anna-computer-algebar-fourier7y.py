import numpy as np
from scipy.integrate import quad

def fourier_coefficients(a, b, c, d, g, h, k, s):
    # Define the even part of the polynomial
    def f_even(x):
        return a*x**6 + c*x**4 + g*x**2 + k
    
    # Define the odd part of the polynomial
    def f_odd(x):
        return b*x**5 + d*x**3 + h*x

    # Calculate a_0
    a_0, _ = quad(lambda x: a*x**6 + b*x**5 + c*x**4 + d*x**3 + g*x**2 + h*x + k, -s, s)
    a_0 /= (2 * s)

    # Calculate a_n
    def a_n_func(n):
        return quad(lambda x: a*x**6 + c*x**4 + g*x**2 + k * np.cos(n * np.pi * x / s), -s, s)[0] / s

    # Calculate b_n
    def b_n_func(n):
        return quad(lambda x: b*x**5 + d*x**3 + h*x * np.sin(n * np.pi * x / s), -s, s)[0] / s

    # Coefficients
    coefficients = {
        'a_0': a_0,
        'a_n': [a_n_func(n) for n in range(1, 6)],  # Calculating a_n for n = 1 to 5
        'b_n': [b_n_func(n) for n in range(1, 6)]   # Calculating b_n for n = 1 to 5
    }
    
    return coefficients

# Example usage
a, b, c, d, g, h, k = 1, 1, 1, 1, 1, 1, 1  # Coefficients for the polynomial
s = 1  # Limit for the integration
coeffs = fourier_coefficients(a, b, c, d, g, h, k, s)

print("Fourier Coefficients:")
print(f"a_0: {coeffs['a_0']}")
print(f"a_n: {coeffs['a_n']}")
print(f"b_n: {coeffs['b_n']}")
