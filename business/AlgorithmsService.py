import numpy as np


""" Class used to execute fitness algorithms."""
class Algorithms:

    def __init__(self):
        print("Using Algorithms.")

    def execute_sphere(self, x):
        print("Sphere")
        return (x ** 2).sum()


    def execute_rastrigin(self, x):
        print("Rastringin")
        y = (x ** 2) - 10 * np.cos(2.0 * np.pi * x) + 10
        return y.sum()

    def execute_rosenbrock(self, a, b):
        print("Rosenbrock")
        y = 100 * (a ** 2) + (b ** 2)
        return y