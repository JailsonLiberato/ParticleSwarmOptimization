from util.constants import Constants


class PSOService:

    def __init__(self):
        self.__particles = []
        
    def execute_pso(self):
        count_iterations: int = 0
        fitness_values = []
        #initialize_particles
        while count_iterations < Constants.N_ITERATIONS:
            self.calculate_fitness()
            self.update_gbest()
            #inertia
            #velocity by topology
            self.update_position()
            self.update_bound_adjustament()
            #fitness_values
            count_iterations += 1

    def calculate_fitness(self):
        pass

    def update_gbest(self):
        pass

    def update_position(self):
        pass

    def update_bound_adjustament(self):
        pass

    @property
    def particles(self):
        return self.__particles

    @particles.setter
    def particles(self, particles):
        self.__particles = particles



