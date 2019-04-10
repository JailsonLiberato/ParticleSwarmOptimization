class ParticleClass:

    def __init__(self, position, velocity):
        print("Create a new Particle")
        self._position = position
        self._velocity = velocity

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    @property
    def pbest(self):
        return self._velocity

    @pbest.setter
    def pbest(self, pbest):
        self._pbest = pbest