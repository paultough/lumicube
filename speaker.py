from lumicube.standard_library import *


# needs to be imported now and into your pythin environment
import cffi

# Enter the address or hostname of your lumicube

cube = None

if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube();
else:
    # connect to my remote cube if not running locally (eg from my Mac)
    cube = LumiCube("cube.local")

# Play a randomly generated tune.

while True:
    # Play a rising piece
    for frequency in range(500, 2000, 100):
        cube.speaker.tone(frequency, 0.01)
    # Play a beat and then another beat
    time.sleep(0.02)
    cube.speaker.tone(500, 0.1, 0.1, function=white_noise)
    time.sleep(0.05)
    cube.speaker.tone(500, 0.1, 0.1, function=white_noise)
    # Play 3 different tones
    cube.speaker.tone(500 + 500 * random.random(), 0.1)
    cube.speaker.tone(500 + 500 * random.random(), 0.1)
    cube.speaker.tone(500 + 500 * random.random(), 0.1)
    # Play another rising piece
    for frequency in range(200, 1000, 10):
        cube.speaker.tone(frequency, 0.003)
