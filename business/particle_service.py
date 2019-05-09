import numpy as np
from util.constants import Constants
from business.functions.fitness_function import FitnessFunction
from model.particle import Particle


class ParticleService:

    def __init__(self):
        print("Particle Service")

    def initialize_particles(self, fitness_function: FitnessFunction):
        particles = []
        for i in range(Constants.N_PARTICLES):
            particle = Particle(i + 1, self.generate_initial_position(fitness_function))
            particles.append(particle)
        return particles

    @staticmethod
    def generate_initial_position(fitness_function: FitnessFunction):
        min_value = fitness_function.min_initialization
        max_value = fitness_function.max_initialization
        return np.random.uniform(min_value, max_value, size=(1, Constants.N_DIMENSIONS))

