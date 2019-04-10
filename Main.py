""" Main class of execution."""
class Main:
    def executar(self):
        option = ' '
        while option != '0':
            print("\n\n")
            print("#"*40)
            print("\tPARTICLE SWARM OPTIMIZATION")
            print("#"*40)
            print("\n\n")
            print("[1] - PSO using Sphere.")
            print("[2] - PSO using Rastringin.")
            print("[3] - PSO using Rosenbrock.")
            print("[0] - Exit")
            option = input("Choose your option: ")

main = Main()
main.executar()