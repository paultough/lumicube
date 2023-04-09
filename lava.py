from lumicube.standard_library import *
import opensimplex

# Enter the address or hostname of your lumicube

cube = None

if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube();
else:
    # connect to my remote cube if not running locally (eg from my Mac)
    cube = LumiCube("cube.local")


# Generate a lava lamp effect using OpenSimplex noise.

opensimplex.random_seed()


def lava_colour(x, y, z, t):
    scale = 0.10
    speed = 0.05
#    hue = noise_4d(scale * x, scale * y, scale * z, speed * t)

    # Replaced the above noise_4d call which needs to make use of customisation in the supplied
    # daemon to make this work.  The version below is pure python code and uses the opensimplex library.
    hue = opensimplex.noise4(scale * x, scale * y, scale * z, speed * t)

    return hsv_colour(hue, 1, 1)

def paint_cube(t):
    colours = {}
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x == 8 or y == 8 or z == 8:
                    colour = lava_colour(x, y, z, t)
                    colours[x,y,z] = colour
    cube.display.set_3d(colours)

t = 0
while True:
    paint_cube(t)
    time.sleep(1/30)
    t += 1



