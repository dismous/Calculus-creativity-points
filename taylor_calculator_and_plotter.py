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
    # calc ranges for plotting
    plot_min_x, plot_max_x = development_point - plot_range, development_point + plot_range
    plot_points = 1000

    # calculate the nth taylor series for the function (BASE_EXPR)
    base_taylor_expr = Float(lambdify(x, base_expr)(development_point))
    current_function = base_expr

    for k in range(1, grade + 1):
        derivative_k = Derivative(current_function, x).doit()
        derivative_k_solved = lambdify(x, derivative_k)(development_point)

        base_taylor_expr += (derivative_k_solved / m.factorial(k)) * ((x - development_point) ** k)

        current_function = derivative_k

    # print resulting taylor expression
    print('f(x) = ' + str(base_expr))
    print(f'T({grade}, {development_point})(x) = ' + str(base_taylor_expr))

    # and plot both expressions (base_expr and base_taylor_expr)
    # by first making functions out of the two expressions,
    # then calculating in an linear space N points and plotting those points with matplotlib
    lam_base_expr = lambdify(x, base_expr, modules=['numpy'])
    lam_taylor_expr = lambdify(x, base_taylor_expr, modules=['numpy'])

    x_vals = np.linspace(plot_min_x, plot_max_x, plot_points)
    y_vals_base_expr, y_vals_taylor_expr = lam_base_expr(x_vals), lam_taylor_expr(x_vals)

    # create subplot
    fig, ax = plt.subplots()
    # plot graphs
    ax.plot(x_vals, y_vals_base_expr, label=str(base_expr))
    ax.plot(x_vals, y_vals_taylor_expr, label=f'T({grade}, {development_point})(x)')
    # styling (x and y axis, etc.)
    ax.grid(True, which='both')

    if plot_min_x < 0 < plot_max_x:
        ax.axvline(x=0, color='k')
    if draw_x_axis:
        ax.axhline(y=0, color='k')
    # set labels, enable legend and show
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    # save in a png file
    fig.savefig('plot.png')


if __name__ == '__main__':
    calculate_and_plot()
