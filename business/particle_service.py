import numpy as np
from util.constants import Constants


class ParticleService:

    def __init__(self):
        print("Particle Service")

    def initialize_particles(self, fitness_function):
        min_value = fitness_function.min_value
        max_value = fitness_function.max_value
        particles = np.random.uniform(min_value, max_value, size=(1, Constants.N_DIMENSIONS))
        return particles
