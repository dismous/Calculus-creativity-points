import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
import sympy as sp


# Define a few functions to use
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

# Taylor series function
def taylor_series(function, a, n, x):
    taylor_sum = np.zeros_like(x)
    for i in range(n):
        term = derivative(function, a, dx=1e-6, n=i, order=2*i+1) / np.math.factorial(i) * (x - a)**i
        taylor_sum += term
    return taylor_sum

# Function to plot the Taylor series
def plot_taylor_series(func, a, n):
    x = np.linspace(-2, 2, 400)
    taylor_approx = taylor_series(func, a, n, x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, func(x), label=f"{func.__name__}")
    plt.plot(x, taylor_approx, label=f"Taylor Series - {n} terms")
    plt.title(f"Taylor Series Approximation of {func.__name__}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Create a new window
window = tk.Tk()
window.title("Equation Solver")

# Create a StringVar to hold the equation
equation = tk.StringVar()

# Create an entry field for the equation
equation_entry = tk.Entry(window, textvariable=equation)
equation_entry.pack()

# Function to solve the equation
def solve_equation():
    func_str = equation.get().replace('e^', 'exp(').replace('e**', 'exp(').replace('ln', 'log')
    if func_str.endswith(')') is False and 'exp(' in func_str:
        func_str += ')'
    x = sp.symbols('x')
    func = sp.lambdify(x, sp.sympify(func_str), 'numpy')
    window.destroy()
    plot_taylor_series(func, 0, 5)

# Create a button to solve the equation
solve_button = tk.Button(window, text="Solve", command=solve_equation)
solve_button.pack()

# Run the GUI
window.mainloop()