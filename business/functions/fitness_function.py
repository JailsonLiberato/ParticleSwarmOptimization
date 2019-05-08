class FitnessFunction(object):

    def __init__(self, name, bounds):
        self.__name = name
        self.__min_bound = bounds[0]
        self.__max_bound = bounds[1]

    @property
    def name(self):
        return self.__name

    @property
    def min_bound(self):
        return self.__min_bound

    @property
    def max_bound(self):
        return self.__max_bound

