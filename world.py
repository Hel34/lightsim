from vector import vector
from circle import circle
from waterdrop import waterdrop
import math

class light:
    source = None
    direction = None
    wavelength = 0
    colour = vector(255,255,255)
    def __init__(self, source, direction, wavelength, colour):
        assert type(source) == vector
        assert type(direction) == vector
        assert wavelength != 0
        self.source = source
        self.direction = direction.normalize()
        self.wavelength = wavelength
        self.colour = colour

class world:
    objects = None
    lights = None
    size = [500,500]

    def __init__(self, size):
        self.objects = []
        self.lights = []
        self.size = size
        self.canvas = [[vector()]*size[0] for i in range(size[1])]

    def any_object_containts(self, vector):
        for object in self.objects:
            if vector in object:
                return true
        return false

    def any_object_coarse_containts(self, vector):
        for object in self.objects:
            if object.coarse_contains(vector):
                return True
        return False

    def add_colour_canvas(self, vector, value):
        if round(vector.x) < self.size[0] and round(vector.y) < self.size[1]:
            if vector.x >0 and vector.y > 0:
                self.canvas[round(vector.y)][round(vector.x)] += value

    def  add_lights(self, lights):
        for licht in lights:
            assert type(licht) == light
            self.lights.append(licht)

    def cast_light(self):
        for licht in self.lights:
            currentpos = licht.source
            currentdir = licht.direction
            currentcolour = licht.colour
            inside = False
            currentinside = None
            for i in range(1,10000):
                if self.any_object_coarse_containts(currentpos):
                    currentpos += currentdir*0.1
                    if inside == False:
                        for object in self.objects:
                            if currentpos in object:
                                currentdir = object.redirect(currentpos, currentdir, licht.wavelength)
                                currentinside = object
                                inside = True
                    else:
                        if not currentpos in currentinside:
                            currentdir, dir2 = object.revredirect(currentpos, currentdir, licht.wavelength)
                            if licht.colour.length() > 1 and currentdir != dir2:
                                self.lights.append(light(currentpos, dir2, licht.wavelength, currentcolour*0.1))
                                currentcolour *= 0.9
                            inside = False
                else:
                    currentpos += currentdir
                self.add_colour_canvas(currentpos,currentcolour)

    def get_canvas(self):
        #return [[[self.canvas[i][j].length()]for j in range(len(self.canvas[0]))] for i in range(len(self.canvas))]

        return [[[self.canvas[i][j].x, self.canvas[i][j].y,self.canvas[i][j].z]for j in range(len(self.canvas[0]))] for i in range(len(self.canvas))]
