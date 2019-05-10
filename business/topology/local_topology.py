from business.topology.topology import Topology
from business.functions.fitness_function import FitnessFunction
import random
from util.constants import Constants
from model.particle import Particle


class LocalTopology(Topology):

    def calculate_velocity(self, particles, gbest, fitness_function: FitnessFunction, inertia: float):
        self.calculate_lbest(particles, fitness_function)
        for particle in particles:
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            particle.velocity = (inertia * particle.velocity) + Constants.COEFFICIENT1 * r1 * \
                                (particle.pbest - particle.position) + Constants.COEFFICIENT2 * r2 \
                                * (particle.lbest - particle.position)
        return particles

    @staticmethod
    def calculate_lbest(particles, fitness_function):
        for i in range(len(particles)):
            if i == 0:
                before_particle = particles[len(particles) - 1]
                current_particle = particles[0]
                next_particle = particles[1]
            elif i == len(particles) - 1:
                before_particle = particles[len(particles) - 2]
                current_particle = particles[len(particles) - 1]
                next_particle = particles[0]
            else:
                before_particle = particles[i - 1]
                current_particle = particles[i]
                next_particle = particles[i + 1]

            before_particle.fitness = fitness_function.run(before_particle.pbest)
            current_particle.fitness = fitness_function.run(current_particle.pbest)
            next_particle.fitness = fitness_function.run(next_particle.pbest)

            local_list = [before_particle, current_particle, next_particle]
            local_list.sort(key=lambda x: x.fitness)
            particle: Particle = local_list[0]
            before_particle.lbest = particle.pbest
            current_particle.lbest = particle.pbest
            next_particle.lbest = particle.pbest



