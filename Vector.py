import math


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __repr__(self):
        return 'X: {} | Y: {} | Z: {}'.format(self.x, self.y, self.z)

    def __abs__(self):
        return math.sqrt(self.mag_squared())

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y, scalar * self.z)

    def __floordiv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def mag_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def scalar_divide(self, scalar):
        return Vector(self.x/scalar, self.y/scalar, self.z/scalar)

    def scalar_multiply(self, scalar):
        return Vector(self.x*scalar, self.y*scalar, self.z*scalar)

    def cross(self, other):
        x = self.y*other.z - other.y*self.z
        y = self.x*other.z - other.x*self.z
        z = self.x*other.y - other.x*self.y
        return Vector(x, y, z)

    def dot(self, other):
        return self.x+other.x + self.y+other.y + self.z+other.z

    def unit_hat(self):
        mag = abs(self)
        return Vector(self.x / mag, self.y/mag, self.z/mag)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z



vector = Vector(0, 0,1)
print(vector.unit_hat())