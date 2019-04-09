import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np


class PSOClass:

    optionsGlobal = {'c1': 2.05, 'c2': 2.05, 'w':0.8}
    optionsLocal = {'c1': 2.05, 'c2': 2.05, 'w':0.8, 'k': 2, "p": 2}

    def __init__(self):
        #self.executarSphere()
        self.executarRastrigin()
        self.executarRosenbrock()

    def executarSphere(self):
        print("-> EXECUTANDO SPHERE")
        print("[Global Best]")
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=30, options=self.optionsGlobal)
        cost, pos = optimizer.optimize(fx.sphere, iters=10000)
        print("COST Global")
        print(cost)
        print("COST pos")
        print(pos)

        print("[Local Best]")
        optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=30, options=self.optionsLocal)
        cost, pos = optimizer.optimize(fx.sphere, iters=10000)
        print("COST Global")
        print(cost)
        print("COST pos")
        print(pos)

    """ print([Focal Best])
        optimizer = ps.single.FocalBestPSO(n_particles=30, dimensions=30, options=self.options)
        cost, pos = optimizer.optimize(fx.sphere, iters=10000)
        print("COST Global")
        print(cost)
        print("COST pos")
        print(pos)
        """
    def executarRastrigin(self):
        max_bound = 5.12 * np.ones(2)
        min_bound = - max_bound
        bounds = (min_bound, max_bound)
        options = {'c1': 2.05, 'c2': 2.05, 'w':0.8}

        # Call instance of PSO with bounds argument
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=2, options=options, bounds=bounds)

        # Perform optimization
        cost, pos = optimizer.optimize(fx.rastrigin, iters=10000)


        #print("[Local Best]")
        #optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=30, options=self.optionsLocal)
        #cost, pos = optimizer.optimize(fx.rastrigin, iters=10000)
        #print("COST Global")
        #print(cost)
        #print("COST pos")
        #print(pos)

    def executarRosenbrock(self):
        print("EXECUTANDO ROSENBROCK")