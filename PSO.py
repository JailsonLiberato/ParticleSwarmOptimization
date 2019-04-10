import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

class PSOClass:

    optionsGlobal = {'c1': 2.05, 'c2': 2.05, 'w':0.8}
    optionsLocal = {'c1': 2.05, 'c2': 2.05, 'w':0.8, 'k': 2, "p": 2}

    def __init__(self):
        #self.executarSphere()
        #self.executarRastrigin()
        self.executarRosenbrock()

    def executarSphere(self):
        print("-> EXECUTANDO SPHERE")
        print("[Global Best]")
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=30, options=self.optionsGlobal)
        cost, posGlobalBest = optimizer.optimize(fx.sphere, iters=10000)
        print(posGlobalBest)

        print("[Local Best]")
        optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=30, options=self.optionsLocal)
        cost, posLocalBest = optimizer.optimize(fx.sphere, iters=10000)
        print(posLocalBest)

        #plt.scatter(posGlobalBest, posLocalBest)
        plt.figure("Function Sphere")
        plt.plot(posGlobalBest,'-g', label='GPSO')
        plt.plot(posLocalBest, '-o', label='LPSO')
        plt.legend(loc='upper left')
        plt.ylabel('Fitness')
        plt.title("Function Sphere")
        plt.show()

    """ print([Focal Best])
        optimizer = ps.single.FocalBestPSO(n_particles=30, dimensions=30, options=self.options)
        cost, pos = optimizer.optimize(fx.sphere, iters=10000)
        """
    def executarRastrigin(self):
        max_bound = 5.12 * np.ones(2)
        min_bound = - max_bound
        bounds = (min_bound, max_bound)
        options = {'c1': 2.05, 'c2': 2.05, 'w':0.8}

        # Call instance of PSO with bounds argument
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=2, options=options, bounds=bounds)

        # Perform optimization
        cost, posGlobalBest = optimizer.optimize(fx.rastrigin, iters=10000)

       # print("[Local Best]")
       # optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=2, options=self.optionsLocal)
        #cost, posLocalBest = optimizer.optimize(fx.rastrigin, iters=10000)

        plt.figure("Function Rastrigin")
        plt.plot(posGlobalBest,'-g', label='GPSO')
        #plt.plot(posLocalBest, '-o', label='LPSO')
        plt.legend(loc='upper left')
        plt.ylabel('Fitness')
        plt.title("Function Rastrigin")
        plt.show()

    def executarRosenbrock(self):
        print("EXECUTANDO ROSENBROCK")
        x_max = 10 * np.ones(2)
        x_min = -1 * x_max
        bounds = (x_min, x_max)
        options = {'c1': 2.05, 'c2': 2.05, 'w': 0.8}
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=2, options=options, bounds=bounds)
        cost, posGlobalBest = optimizer.optimize(self.rosenbrock_with_args, 10000, a=1, b=100, c=0)

        optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=2, options=self.optionsLocal, bounds=bounds)
        cost, posLocalBest = optimizer.optimize(self.rosenbrock_with_args, 10000, a=1, b=100, c=0)


        plt.figure("Function Rastrigin")
        plt.plot(posGlobalBest,'-g', label='GPSO')
        plt.plot(posLocalBest, '-o', label='LPSO')
        plt.legend(loc='upper left')
        plt.ylabel('Fitness')
        plt.title("Function Rastrigin")
        plt.show()
        

    def rosenbrock_with_args(self, x, a, b, c=0):
        f = (a - x[:, 0]) ** 2 + b * (x[:, 1] - x[:, 0] ** 2) ** 2 + c
        return f