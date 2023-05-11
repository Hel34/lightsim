from vector import vector
from circle import circle
import math
class waterdrop:
    perimeter = circle(vector(1,1),1)
    n = 1.33

    def __init__(self, x, y, radius):
        self.perimeter = circle(vector(x,y),radius)
    def __contains__(self, item):
        return item in self.perimeter

    def coarse_contains(self, other):
        return self.perimeter.coarse_contains(other)

    def n(self, wavelength):
        return 1.327 + 2070.78/(wavelength**2)

    def redirect(self, position, direction, wavelength):
        tangent = self.perimeter.tangent_on(position)
        normal  = self.perimeter.normal_on(position)
        cos1 = direction.dot(tangent)
        n = self.n(wavelength)
        cos2 = cos1/n
        sin2 = (1-cos2**2)**0.5
        return (tangent*cos2-normal*sin2).normalize()

    def revredirect(self, position, direction, wavelength):
        tangent = self.perimeter.tangent_on(position)
        normal  = self.perimeter.normal_on(position)
        cos1 = direction.dot(tangent)
        n = self.n(wavelength)
        if abs(cos1) < 1/n:
            cos2 = cos1*n
            sin2 = (1-cos2**2)**0.5
            return (tangent*cos2+normal*sin2).normalize(), tangent*cos1 - normal*(1-cos1**2)*0.5
        else:
            return tangent*cos1 - normal*(1-cos1**2)*0.5, tangent*cos1 - normal*(1-cos1**2)*0.5
