import numpy as np
from business.functions.fitness_function import FitnessFunction


class RastringinFunction(FitnessFunction):

    def __init__(self):
        super(RastringinFunction, self).__init__('Rastringin', (-5.12, 5.12))

    def run(self, x):
        y = (x ** 2) - 10 * np.cos(2.0 * np.pi * x) + 10
        return y.sum()
