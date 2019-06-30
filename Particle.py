from Vector import Vector


class Particle:

    BIG_G = 1

    def __init__(self, mass, position: Vector, velocity: Vector, label):
        self.__mass = mass
        self.__position = position
        self.__velocity = velocity
        self.__label = label

    def __repr__(self):
        return '{}: pos: {}  vel: {}'.format(self.label, self.position, self.velocity)

    @property
    def mass(self):
        return self.__mass

    @property
    def position(self):
        return self.__position

    @property
    def velocity(self):
        return self.__velocity

    @property
    def label(self):
        return self.__label

    @position.setter
    def position(self, position):
        self.__position = position

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    def kinetic_energy(self):
        return 0.5 * self.mass * (self.velocity.dot(self.velocity))

    def leap_position(self, dt):
        '''
        Time integration support: evolves the system according to
        dx = v * dt
        :param dt:
        :return: None
        '''
        self.__position = self.position * dt


