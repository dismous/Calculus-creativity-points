import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

def exp(x):
    return np.exp(x)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def ln(x):
    return np.log(x)

def tg(x):
    return np.tan(x)

def ctg(x):
    return 1 / np.tan(x)

def taylor_series(function, a, n):
    x = sp.symbols('x')
    taylor_sum = 0
    for i in range(n):
        term = function.diff(x, i).subs(x, a) / np.math.factorial(i) * (x - a)**i
        taylor_sum += term
    return sp.lambdify(x, taylor_sum, 'numpy')

window = tk.Tk()
window.title("Equation Solver")
equation = tk.StringVar()
a_value = tk.StringVar()
n_value = tk.StringVar()
equation_label = tk.Label(window, text="Enter equation:")
equation_label.pack()
equation_entry = tk.Entry(window, textvariable=equation)
equation_entry.pack()

a_label = tk.Label(window, text="Enter the point around which the series is expanded:")
a_label.pack()
a_entry = tk.Entry(window, textvariable=a_value)
a_entry.pack()

n_label = tk.Label(window, text="Enter the number of terms in the series:")
n_label.pack()
n_entry = tk.Entry(window, textvariable=n_value)
n_entry.pack()



def plot_taylor_series(func, a, n):
    x = sp.symbols('x')
    taylor_approx = taylor_series(func, a, n)
    x_values = np.linspace(a - 5, a + 5, 500)
    func_values = np.array([func.evalf(subs={x: val}) for val in x_values])
    taylor_values = taylor_approx(x_values)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, func_values, label='Function')
    plt.plot(x_values, taylor_values, label='Taylor series approximation')
    plt.scatter([a], [func.evalf(subs={x: a})], color='red')  # point of expansion
    plt.legend()
    plt.grid(True)
    plt.show()

def solve_equation():
    func_str = equation.get().replace('e^', 'exp(').replace('e**', 'exp(').replace('ln', 'log')
    if func_str.endswith(')') is False and 'exp(' in func_str:
        func_str += ')'
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    
    # Get the point around which the series is expanded and the number of terms from the user
    a = float(a_value.get())
    n = int(n_value.get())
    
    window.destroy()
    plot_taylor_series(func, a, n)

solve_button = tk.Button(window, text="Solve", command=solve_equation)
solve_button.pack()
window.mainloop()