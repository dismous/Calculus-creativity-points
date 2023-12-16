"""
This module contains a function that calculates the nth Taylor series
for a given function and plots it using matplotlib.
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

# Define the symbol for sympy
symbol_x = symbols('x')


def calculate_and_plot(base_expr=cos(symbol_x),
                       development_point: float = 8,
                       grade: int = 4,
                       plot_range: int = 4,
                       draw_x_axis: bool = True):
    """Calculate the nth Taylor series and plot it."""
    min_x, max_x = development_point - plot_range, development_point + plot_range
    num_points = 1000
    taylor_expr = Float(lambdify(symbol_x, base_expr)(development_point))
    current_expr = base_expr
    for i in range(1, grade + 1):
        derivative = Derivative(current_expr, symbol_x).doit()
        derivative_at_point = lambdify(symbol_x, derivative)(development_point)
        taylor_expr += (derivative_at_point / math.factorial(i)) * ((symbol_x - development_point) ** i)
        current_expr = derivative

    print('f(x) = ' + str(base_expr))
    print(f'T({grade}, {development_point})(x) = ' + str(taylor_expr))
    base_func = lambdify(symbol_x, base_expr, modules=['numpy'])
    taylor_func = lambdify(symbol_x, taylor_expr, modules=['numpy'])
    x_values = np.linspace(min_x, max_x, num_points)
    y_values_base, y_values_taylor = base_func(x_values), taylor_func(x_values)
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values_base, label=str(base_expr))
    ax.plot(x_values, y_values_taylor, label=f'T({grade}, {development_point})(x)')
    ax.grid(True, which='both')
    if min_x < 0 < max_x:
        ax.axvline(x=0, color='k')
    if draw_x_axis:
        ax.axhline(y=0, color='k')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    calculate_and_plot()
