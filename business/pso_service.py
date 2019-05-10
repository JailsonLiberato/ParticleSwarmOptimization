from typing import List

from util.constants import Constants
from business.particle_service import ParticleService
from business.functions.fitness_function import FitnessFunction
from business.topology.topology import Topology
import math
import numpy as np
from copy import copy


class PSOService:
    __particles:[]
    __particle_service: ParticleService

    def __init__(self, fitness_function: FitnessFunction, topology: Topology, linear_decay_weight: bool, constriction_coeff_weight: bool) -> object:
        self.__fitness_values = []
        self.__particle_service = ParticleService()
        self.__fitness_function = fitness_function
        self.__topology = topology
        self.__linear_decay_weight = linear_decay_weight
        self.__constriction_coeff_weight = constriction_coeff_weight
        self.__particles = self.__particle_service.initialize_particles(self.__fitness_function)
        self.__gbest = copy(self.__particles[0].pbest)
        self.__execute_pso()

    def __execute_pso(self):
        count_iterations: int = 0
        while count_iterations < Constants.N_ITERATIONS:
            self.calculate_fitness()
            self.update_gbest()
            inertia = self.generate_inertia(self.__linear_decay_weight, self.__constriction_coeff_weight,
                                            count_iterations)
            self.__particles = self.__topology.calculate_velocity(self.__particles, self.__gbest,
                                                                  self.__fitness_function, inertia)
            self.update_position()
            self.update_bound_adjustament()
            self.__fitness_values.append(self.__fitness_function.run(self.__gbest))
           # print("Count Iteration: ", count_iterations, " fitness: ", self.__fitness_values[count_iterations - 1])
            count_iterations += 1

    def calculate_fitness(self):
        for particle in self.__particles:
            if self.__fitness_function.run(particle.position) < self.__fitness_function.run(particle.pbest):
                particle.pbest = copy(particle.position)
                particle.fitness = self.__fitness_function.run(particle.pbest)

    def update_gbest(self):
        for particle in self.__particles:
            if (self.__fitness_function.run(particle.pbest) < self.__fitness_function.run(
                    self.__gbest)) and self.is_limit_exceeded(particle.pbest):
                self.__gbest = copy(particle.pbest)

    def is_limit_exceeded(self, pbest):
        return np.any(pbest >= self.__fitness_function.min_bound) and np.any(pbest <= self.__fitness_function.max_bound)

    def update_position(self):
        for particle in self.__particles:
            particle.position += particle.velocity

    def update_bound_adjustament(self):
        min_array = [self.__fitness_function.min_bound]
        max_array = [self.__fitness_function.max_bound]
        for particle in self.__particles:
            np.putmask(particle.position, particle.position > max_array, self.__fitness_function.max_bound)
            np.putmask(particle.position, particle.position < min_array, self.__fitness_function.min_bound)

    @staticmethod
    def generate_inertia(linear_decay_weight, constriction_coeff_weight, count_iterations):
        if linear_decay_weight:
            return Constants.INERTIA_MAX - count_iterations * (Constants.INERTIA_MAX - Constants.INERTIA_MIN) / \
                   Constants.N_ITERATIONS
        elif constriction_coeff_weight:
            t = Constants.COEFFICIENT1 + Constants.COEFFICIENT2
            a = 2.0 - t
            b = math.sqrt((t ** 2) - (4.0 * t))

            k: float = 2.0 / math.fabs(a - b)
            return k
        else:
            return Constants.INERTIA

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values
