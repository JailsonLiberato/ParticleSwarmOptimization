import matplotlib.pyplot as plot
import matplotlib as mpl
import numpy as np 

SPHERE = 'Sphere'
RASTRINGIN = 'Rastringin'
ROSENBROCK = 'Rosenbrock'
CONSTANT_WEIGHT = 'Constant Weight'
LINEAR_DECAY_WEIGHT = ' Linear Decay Weight'
CONSTRICT_COEFF_WEIGHT = 'Constrict Coeff Weight'

class Main:

    def executeMain(self):
        self.createSphere()
        self.createRastringin()
        self.createRosenbrock()

    def createSphere(self):
        self.createConstantWeight(SPHERE)
        self.createBoxplotConstantWeight(SPHERE)
        self.createLinearDecayWeight(SPHERE)
        self.createBoxplotLinearDecayWeight(SPHERE)
        self.createConstrictionCoeffWeight(SPHERE)
        self.createBoxplotConstrictionCoeffWeight(SPHERE)
    
    def createRastringin(self):
        self.createConstantWeight(RASTRINGIN)
        self.createBoxplotConstantWeight(RASTRINGIN)
        self.createLinearDecayWeight(RASTRINGIN)
        self.createBoxplotLinearDecayWeight(RASTRINGIN)
        self.createConstrictionCoeffWeight(RASTRINGIN)
        self.createBoxplotConstrictionCoeffWeight(RASTRINGIN)

    def createRosenbrock(self):
        self.createConstantWeight(ROSENBROCK)
        self.createBoxplotConstantWeight(ROSENBROCK)
        self.createLinearDecayWeight(ROSENBROCK)
        self.createBoxplotLinearDecayWeight(ROSENBROCK)
        self.createConstrictionCoeffWeight(ROSENBROCK)
        self.createBoxplotConstrictionCoeffWeight(ROSENBROCK)


    def createConstantWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' ' + CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)

    def createBoxplotConstantWeight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + CONSTANT_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateBoxplotGraph(globals, locals, focals, title, filename)
        
    def createLinearDecayWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' ' + LINEAR_DECAY_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)
        
    def createBoxplotLinearDecayWeight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + LINEAR_DECAY_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateBoxplotGraph(globals, locals, focals, title, filename)

    def createConstrictionCoeffWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' ' + CONSTRICT_COEFF_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)

    def createBoxplotConstrictionCoeffWeight(self, function):
        np.random.seed(10)
        globals = np.random.normal(100, 10, 200)
        locals = np.random.normal(80, 30, 200)
        focals = np.random.normal(90, 20, 200)
        title = function + ' ' + CONSTRICT_COEFF_WEIGHT
        filename = title.lower().replace(' ', '_')
        self.generateBoxplotGraph(globals, locals, focals, title, filename)
    
    def generateCurveLineGraph(self, globals, locals, focals, title, filename):
        plot.plot(globals, label="Global Best")
        plot.plot(locals, label="Local Best")
        plot.plot(focals, label="Focal Best")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
        plot.legend()
        plot.title("Curve Line: " + title)
        plot.savefig('..//file//curve_line_' + filename +'.png')
        plot.close()

    def generateBoxplotGraph(self, globals, locals, focals, title, filename):
        fig = plot.figure(1, figsize=(9, 6))
        ax = fig.add_subplot(111)
        data_to_plot = [globals, locals, focals]
        bp = ax.boxplot(data_to_plot)
        ax.set_xticklabels(['Global', 'Local', 'Focal'])
        plot.title("Boxplot: " + title)
        fig.savefig('..//file//boxplot_' + filename +'.png', bbox_inches='tight')
        plot.close()

main = Main()
main.executeMain()
