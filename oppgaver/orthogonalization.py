import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.cos( np.pi * x)

#Legendre polynomials
P0 = lambda x: x**0
P1 = lambda x: x
P2 = lambda x: 0.5 * (3*x**2 - 1)

def combine_coefficients_with_basis(new_coefficients, basis_polynomials):
    """
    new_coefficients: array of coefficients [c0, c1, ..., cn]
    basis_polynomials: list of polynomial objects [p0, p1, ..., pn]
    
    Returns: polynomial sum(c_i * p_i)
    """
    def combined_f(x):
        result = np.zeros_like(x)
        for coeff, poly in zip(new_coefficients, basis_polynomials):
            result += coeff * poly(x)
        return result
    return combined_f

def L_2norm(f, g, a, b, num_points=1000):
    """Calculating L2 norm on between f and g on [a, b]."""
    x = np.linspace(a, b, num_points)
    integrand = f(x) * g(x)
    return np.trapz(integrand, x)

def gram_schmidt(f, funcs, a, b, num_points=1000):
    p = []
    for i in range(len(funcs)):
        den = L_2norm(f, funcs[i], a, b, num_points)
        num = L_2norm(funcs[i], funcs[i], a, b, num_points)
        c = den / num
        p.append(c)
    return combine_coefficients_with_basis(p, funcs)

g = gram_schmidt(f, [P0, P1, P2], -1, 1)

x = np.linspace(-1, 1, 1000)
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='f(x) = cos(πx)', color='black', linewidth=2)
plt.plot(x, g(x), label='Approximation', color='red', linestyle='--')
plt.title('Approximation av cos(πx) med Legendre-polynomer')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()