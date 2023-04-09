from lumicube.standard_library import *

# Enter the address or hostname of your lumicube

cube = None

if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube();
else:
    # connect to my remote cube if not running locally (eg from my Mac)
    cube = LumiCube("cube.local")


import datetime
cube.display.set_all(black)
while True:
    time_text = datetime.datetime.now().strftime("%H:%M")
    cube.display.scroll_text(time_text, orange)
    time.sleep(5)