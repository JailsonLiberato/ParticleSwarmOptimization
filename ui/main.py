import matplotlib.pyplot as plot
import numpy as np
from util.constants import Constants


class Main:

    def execute_main(self):
        self.__create_sphere()
        self.__create_rastringin()
        self.__create_rosenbrock()

    def __create_sphere(self):
        self.__create_constant_weight(Constants.SPHERE)
        self.__create_boxplot_constant_weight(Constants.SPHERE)
        self.__create_linear_decay_weight(Constants.SPHERE)
        self.__create_boxplot_linear_decay_weight(Constants.SPHERE)
        self.__create_constriction_coeff_weight(Constants.SPHERE)
        self.__create_boxplot_constriction_coeff_weight(Constants.SPHERE)

    def __create_rastringin(self):
        self.__create_constant_weight(Constants.RASTRINGIN)
        self.__create_boxplot_constant_weight(Constants.RASTRINGIN)
        self.__create_linear_decay_weight(Constants.RASTRINGIN)
        self.__create_boxplot_linear_decay_weight(Constants.RASTRINGIN)
        self.__create_constriction_coeff_weight(Constants.RASTRINGIN)
        self.__create_boxplot_constriction_coeff_weight(Constants.RASTRINGIN)

    def __create_rosenbrock(self):
        self.__create_constant_weight(Constants.ROSENBROCK)
        self.__create_boxplot_constant_weight(Constants.ROSENBROCK)
        self.__create_linear_decay_weight(Constants.ROSENBROCK)
        self.__create_boxplot_linear_decay_weight(Constants.ROSENBROCK)
        self.__create_constriction_coeff_weight(Constants.ROSENBROCK)
        self.__create_boxplot_constriction_coeff_weight(Constants.ROSENBROCK)

    def __create_constant_weight(self, function):
        globals = [5, 6]
        locals = [7, 8]
        focals = [9, 10]
        title = function + ' ' + Constants.CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_constant_weight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + Constants.CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_boxplot_graph(globals, locals, focals, title, filename)

    def __create_linear_decay_weight(self, function):
        globals = [5, 6]
        locals = [7, 8]
        focals = [9, 10]
        title = function + ' ' + Constants.LINEAR_DECAY_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_linear_decay_weight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + Constants.LINEAR_DECAY_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_boxplot_graph(globals, locals, focals, title, filename)

    def __create_constriction_coeff_weight(self, function):
        globals = [5, 6]
        locals = [7, 8]
        focals = [9, 10]
        title = function + ' ' + Constants.CONSTRICT_COEFFICIENT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_curve_line_graph(globals, locals, focals, title, filename)

    def __create_boxplot_constriction_coeff_weight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + Constants.CONSTRICT_COEFFICIENT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.__generate_boxplot_graph(globals, locals, focals, title, filename)

    @staticmethod
    def __generate_curve_line_graph(globals, locals, focals, title, filename):
        plot.plot(globals, label="Global Best")
        plot.plot(locals, label="Local Best")
        plot.plot(focals, label="Focal Best")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
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
