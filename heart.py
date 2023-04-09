from lumicube.standard_library import *

# Enter the address or hostname of your lumicube

cube = None

if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube();
else:
    # connect to my remote cube if not running locally (eg from my Mac)
    cube = LumiCube("cube.local")

r = red;
heart = [
    [0,0,0,0,0,0,0,0],
    [0,r,r,0,0,r,r,0],
    [r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r],
    [0,r,r,r,r,r,r,0],
    [0,0,r,r,r,r,0,0],
    [0,0,0,r,r,0,0,0],
    [0,0,0,0,0,0,0,0],
];
cube.display.set_panel("left", heart);
cube.display.set_panel("right", heart);
cube.display.set_panel("top", heart);