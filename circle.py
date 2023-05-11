from vector import vector

#immutable
class circle:
    center = vector(0,0,0)
    radius = vector(0,0)

    def __init__(self, center, radius):
        assert type(center) == vector
        assert radius > 0
        self.center = center
        self.radius = radius

    def __contains__(self, other):
        assert type(other) == vector
        return (other-self.center).length() <= self.radius

    def with_center(self, radius):
        return circle(self.center, radius)

    def coarse_contains(self, other):
        return other in self.with_center(self.radius*1.1)

    def tangent_on(self, other):
        assert type(other) == vector
        return (other-self.center).cross(vector(0,0,1)).normalize()
    def normal_on(self, other):
        return  (other  - self.center).normalize()