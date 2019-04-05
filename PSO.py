import pyswarms as ps

class PSOClass:

    options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

    def __init__(self):
        self.executarSphere()
        self.executarRastrigin()
        self.executarRosenbrock()

    def executarSphere(self):
        print("EXECUTANDO SPHERE")

    def executarRastrigin(self):
        print("EXECUTANDO RASTRIGIN")

    def executarRosenbrock(self):
        print("EXECUTANDO ROSENBROCK")