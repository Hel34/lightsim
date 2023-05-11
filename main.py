from world import world
from world import light
from vector import vector
from circle import circle
from waterdrop import waterdrop
import numpy as np
from matplotlib import pyplot as plt
from random import randint

ea = world([2000,1000])
straal = 200
angle = 20*np.pi/180
ea.lights += [light(vector(u,0),vector(np.cos(angle),np.sin(angle)), 700, vector(4,0,0)) for u in np.linspace(-1000,2000,150)]
ea.lights += [light(vector(u,0),vector(np.cos(angle),np.sin(angle)), 450, vector(0,0,4)) for u in np.linspace(-1000,2000,150)]
ea.lights += [light(vector(u,0),vector(np.cos(angle),np.sin(angle)), 535, vector(0,4,0)) for u in np.linspace(-1000,2000,150)]

ea.objects = [waterdrop(1000, 500 + 500*(i),straal) for i in range(1)]

ea.cast_light()
plt.imshow(ea.get_canvas(), cmap = "gist_gray")
nptheta = np.linspace(0, 2*np.pi, 500)
plt.show()