"""
contains the function which will calculate the nth taylor series
for a given function and plot it with matplotlib.
"""

import math as m

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = symbols('x')


def calculate_and_plot(development_point: float = 8,
                       grade: int = 4,
                       base_expr=cos(x),
                       plot_range: int = 4,
                       draw_x_axis: bool = True):
    plot_min_x, plot_max_x = development_point - plot_range, development_point + plot_range
    plot_points = 1000
    base_taylor_expr = Float(lambdify(x, base_expr)(development_point))
    current_function = base_expr

    for k in range(1, grade + 1):
        derivative_k = Derivative(current_function, x).doit()
        derivative_k_solved = lambdify(x, derivative_k)(development_point)

        base_taylor_expr += (derivative_k_solved / m.factorial(k)) * ((x - development_point) ** k)

        current_function = derivative_k

    print('f(x) = ' + str(base_expr))
    print(f'T({grade}, {development_point})(x) = ' + str(base_taylor_expr))

    lam_base_expr = lambdify(x, base_expr, modules=['numpy'])
    lam_taylor_expr = lambdify(x, base_taylor_expr, modules=['numpy'])

    x_vals = np.linspace(plot_min_x, plot_max_x, plot_points)
    y_vals_base_expr, y_vals_taylor_expr = lam_base_expr(x_vals), lam_taylor_expr(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals_base_expr, label=str(base_expr))
    ax.plot(x_vals, y_vals_taylor_expr, label=f'T({grade}, {development_point})(x)')
    ax.grid(True, which='both')

    if plot_min_x < 0 < plot_max_x:
        ax.axvline(x=0, color='k')
    if draw_x_axis:
        ax.axhline(y=0, color='k')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    calculate_and_plot()
