import math

#immutable
class vector:
    x = 0
    y = 0
    z = 0
    d = 3


    def __init__(self,x=0 ,y=0 ,z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        assert type(other) == vector
        return vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __mul__(self, other):
        assert type(other) != vector
        return vector(self.x*other, self.y*other, self.z*other)

    def __sub__(self, other):
        assert type(other) == vector
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        assert type(other) == vector
        return self.x * other.x + self.y * other.y + self.z * other.z

    def lensq(self):
        return self.dot(self)

    def length(self):
        return (self.lensq())**0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def cos_of_angle_with(self, other):
        assert other != vector()
        assert type(other) == vector
        return self.dot(other)/(self.length()*other.length())

    def angle_with(self, other):
        assert other != vector()
        assert type(other) == vector
        return sp.acos(self.cos_of_angle_with(other))

    def cross(self, other):
        assert type(other) == vector
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y
        z1 = self.z
        z2 = other.z
        return vector(y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2)

    def normalize(self):
        return self* (1/self.length())
