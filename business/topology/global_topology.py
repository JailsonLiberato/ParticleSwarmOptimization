from business.topology.topology import Topology
from business.functions.fitness_function import FitnessFunction
from util.constants import Constants
import random


class GlobalTopology(Topology):

    def calculate_velocity(self, particles, gbest, fitness_function: FitnessFunction, inertia: float):
        for particle in particles:
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            particle.velocity = inertia * particle.velocity + Constants.COEFFICIENT1 * r1 * \
                                (particle.pbest - particle.position) + Constants.COEFFICIENT2 * r2 \
                                * (gbest - particle.position)
