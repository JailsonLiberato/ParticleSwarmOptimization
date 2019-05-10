import matplotlib.pyplot as plot
import numpy as np
from util.constants import Constants
from business.functions.sphere_function import SphereFunction
from business.functions.rastringin_function import RastringinFunction
from business.functions.rosenbrock_function import RosenbrockFunction
from business.pso_service import PSOService
from business.topology.global_topology import GlobalTopology
from business.topology.local_topology import LocalTopology
from business.topology.focal_topology import FocalTopology


class Main:

    __pso_service: PSOService

    def __init__(self):
        self.__focal_topology = FocalTopology()
        self.__local_topology = LocalTopology()
        self.__global_topology = GlobalTopology()

    def execute_main(self):
        self.__create_sphere()
        self.__create_rastringin()
        self.__create_rosenbrock()

    def __create_sphere(self):
        sphere_function = SphereFunction()
        self.__create_constant_weight(sphere_function)
        #self.__create_boxplot_constant_weight(sphere_function)
        #self.__create_linear_decay_weight(sphere_function)
        #self.__create_boxplot_linear_decay_weight(sphere_function)
        #self.__create_constriction_coeff_weight(sphere_function)
        #self.__create_boxplot_constriction_coeff_weight(sphere_function)

    def __create_rastringin(self):
        rastringin_function = RastringinFunction()
        #self.__create_constant_weight(rastringin_function)
        #self.__create_boxplot_constant_weight(rastringin_function)
        #self.__create_linear_decay_weight(rastringin_function)
        #self.__create_boxplot_linear_decay_weight(rastringin_function)
        #self.__create_constriction_coeff_weight(rastringin_function)
        #self.__create_boxplot_constriction_coeff_weight(rastringin_function)

    def __create_rosenbrock(self):
        rosenbrock_function = RosenbrockFunction()
        #self.__create_constant_weight(rosenbrock_function)
        #self.__create_boxplot_constant_weight(rosenbrock_function)
        #elf.__create_linear_decay_weight(rosenbrock_function)
        #self.__create_boxplot_linear_decay_weight(rosenbrock_function)
        #self.__create_constriction_coeff_weight(rosenbrock_function)
        #self.__create_boxplot_constriction_coeff_weight(rosenbrock_function)

    def __create_constant_weight(self, fitness_function):
        self.__pso_service = PSOService(fitness_function, self.__global_topology, False, False)
        globals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__local_topology, False, False)
        locals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__focal_topology, False, False)
        focals = self.__pso_service.fitness_values
        title = fitness_function.name + ' ' + Constants.CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_constant_weight(self, fitness_function):
        globals_array = []
        locals_array = []
        focals_array = []
        for _ in range(Constants.N_REPETITIONS):
            self.__pso_service = PSOService(fitness_function, self.__global_topology, False, False)
            globals = self.__pso_service.fitness_values
            globals_array.append(globals[len(globals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__local_topology, False, False)
            locals = self.__pso_service.fitness_values
            locals_array.append(locals[len(locals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__focal_topology, False, False)
            focals = self.__pso_service.fitness_values
            focals_array.append(focals[len(focals) - 1])

        title = fitness_function.name + ' ' + Constants.CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_boxplot_graph(globals_array, locals_array, focals_array, title, filename)

    def __create_linear_decay_weight(self, fitness_function):
        self.__pso_service = PSOService(fitness_function, self.__global_topology, True, False)
        globals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__local_topology, True, False)
        locals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__focal_topology, True, False)
        focals = self.__pso_service.fitness_values
        title = fitness_function.name + ' ' + Constants.LINEAR_DECAY_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_linear_decay_weight(self, fitness_function):
        globals_array = []
        locals_array = []
        focals_array = []
        for _ in range(Constants.N_REPETITIONS):
            self.__pso_service = PSOService(fitness_function, self.__global_topology, True, False)
            globals = self.__pso_service.fitness_values
            globals_array.append(globals[len(globals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__local_topology, True, False)
            locals = self.__pso_service.fitness_values
            locals_array.append(locals[len(locals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__focal_topology, True, False)
            focals = self.__pso_service.fitness_values
            focals_array.append(focals[len(focals) - 1])

            title = fitness_function.name + ' ' + Constants.LINEAR_DECAY_WEIGHT
            filename = title.lower().replace(' ', '_')
            self.__generate_boxplot_graph(globals_array, locals_array, focals_array, title, filename)

    def __create_constriction_coeff_weight(self, fitness_function):
        self.__pso_service = PSOService(fitness_function, self.__global_topology, False, True)
        globals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__local_topology, False, True)
        locals = self.__pso_service.fitness_values
        self.__pso_service = PSOService(fitness_function, self.__focal_topology, False, True)
        focals = self.__pso_service.fitness_values
        title = fitness_function.name + ' ' + Constants.CONSTRICT_COEFFICIENT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_constriction_coeff_weight(self, fitness_function):
        globals_array = []
        locals_array = []
        focals_array = []
        for _ in range(Constants.N_REPETITIONS):
            self.__pso_service = PSOService(fitness_function, self.__global_topology, False, True)
            globals = self.__pso_service.fitness_values
            globals_array.append(globals[len(globals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__local_topology, False, True)
            locals = self.__pso_service.fitness_values
            locals_array.append(locals[len(locals) - 1])

            self.__pso_service = PSOService(fitness_function, self.__focal_topology, False, True)
            focals = self.__pso_service.fitness_values
            focals_array.append(focals[len(focals) - 1])
            title = fitness_function.name + ' ' + Constants.CONSTRICT_COEFFICIENT_WEIGHT
            filename = title.lower().replace(' ', '_')
            self.__generate_boxplot_graph(globals_array, locals_array, focals_array, title, filename)

    @staticmethod
    def __generate_curve_line_graph(globals, locals, focals, title, filename):
        plot.plot(globals, label="Global Best")
        plot.plot(locals, label="Local Best")
        plot.plot(focals, label="Focal Best")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
        plot.yscale('log')
        plot.legend()
        plot.title("Curve Line: " + title)
        plot.savefig('..//file//curve_line_' + filename + '.png')
        plot.close()

    @staticmethod
    def __generate_boxplot_graph(globals, locals, focals, title, filename):
        fig = plot.figure(1, figsize=(9, 6))
        ax = fig.add_subplot(111)
        data_to_plot = [globals, locals, focals]
        bp = ax.boxplot(data_to_plot)
        ax.set_xticklabels(['Global', 'Local', 'Focal'])
        plot.title("Boxplot: " + title)
        fig.savefig('..//file//boxplot_' + filename + '.png', bbox_inches='tight')
        plot.close()


main = Main()
main.execute_main()
