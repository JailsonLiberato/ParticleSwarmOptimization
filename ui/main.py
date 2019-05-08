import matplotlib.pyplot as plot
class Main:

    def executeMain(self):
        self.createSphere()
        self.createRastringin()
        self.createRosenbrock()

    def createSphere(self):
        self.createConstantWeight('Sphere')
        self.createBoxplotConstantWeight()
        self.createLinearDecayWeight('Sphere')
        self.createBoxplotLinearDecayWeight()
        self.createConstrictionCoeffWeight('Sphere')
    
    def createRastringin(self):
        self.createConstantWeight('Rastringin')
        self.createBoxplotConstantWeight()
        self.createLinearDecayWeight('Rastringin')
        self.createBoxplotLinearDecayWeight()
        self.createConstrictionCoeffWeight('Rastringin')

    def createRosenbrock(self):
        self.createConstantWeight('Rosenbrock')
        self.createBoxplotConstantWeight()
        self.createLinearDecayWeight('Rosenbrock')
        self.createBoxplotLinearDecayWeight()
        self.createConstrictionCoeffWeight('Rosenbrock')


    def createConstantWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' Constant Weight'
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)

    def createBoxplotConstantWeight(self):
        print("")
        
    def createLinearDecayWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' Linear Decay Weight'
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)
        
    def createBoxplotLinearDecayWeight(self):
        print("")

    def createConstrictionCoeffWeight(self, function):
        globals = [5, 6]
        locals = [7,8]
        focals = [9, 10]
        title = function + ' Constrict Coeff Weight'
        filename = title.lower().replace(' ', '_')
        self.generateCurveLineGraph(globals, locals, focals, title, filename)
    
    def generateCurveLineGraph(self, globals, locals, focals, title, filename):
        plot.plot(globals, label="Global Best")
        plot.plot(locals, label="Local Best")
        plot.plot(focals, label="Focal Best")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
        plot.legend()
        plot.title("Curve Line: " + title)
        plot.savefig('..//file//' + filename +'.png')
        plot.close()

main = Main()
main.executeMain()