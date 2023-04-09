# LumiCube

This code allows remote access to your AbstractFoundry LumiCube using the documented API without the need to enter your code into the Web Interface.

*Thanks to the AbstractFoundry team for creating a cool and funky device that sits nicely on my desk that beats any boring LCD clock*

## References

[Abstract Foundry Website](https://abstractfoundry.com/)

[LumiCube manual](https://abstractfoundry.com/lumicube/manual.pdf)

[LumiCube reference docs](https://github.com/abstractfoundry/lumicube)

## Purpose / Why?

I wanted to access the LumiCube without the need to access the web interface on the cube itself.  The intention of the LumiCube was to provide a device that provides students with a physical cube to allow them to explore learning Python and for that purpose the web UI is perfect.  But for larger projects or for other use cases this has some drawbacks which I wanted to avoid, including:

1. To access the web UI you need to go through a browser and then code in the UI and then execute.  This is great for learning and for scripting small pieces of code but not great for more complex code.  I want to be able to code in my own editor and then execurte the code on my cube at the push of a button.
2. The web UI is designed for smaller scripts and not for multi-file Python programming.
3. The web UI hides some of the Python code.  Yes, the code is in the github repo for those who can navigate it, but not that easy to locate without a non-trivial search.

Additional requirements for my cube were:

1. I want to be able to trigger activities on the cube based on external events.  For example, to alert to an email at a specific email address.  You can create a script to do this BUT it would be the only script that would execute on the cube and I want to be able to potentially have many different scripts running at once and to execute these potentially remotely.
2. I wanted to utilise any python library on the Internet for use in my code (see example lava lamp customisation below).

What I learned:

1. The cube daemon just executes commands and has no locking in place.  This means that you can have multiple actions firing from different programs at the same time.  This is actually a good thing.  It would be possible to execute a queuing mechanism on top of the daemon if this was a problem and maybe something I would look at if this is a problem.


## What's in the codebase

>To get the scripts to work you need to make a change to the files to point to your own cube. My cube is called "cube.local" on my network and so these are setup to look for a cube with that hostname.  Change this if yours is different.


* clock.py - example supplied from AbstractFoundry that can be run from your remote computer using the modified library file
* heart.py - example supplied from AbstractFoundry that can be run from your remote computer using the modified library file
* speaker.py - example supplied from AbstractFoundry that can be run from your remote computer using the modified library file
* lava.py - remote lava lamp code abstracted from AbstractFoundry that used pure python as opposed to making use of an embedded library in the daemon (see below).  This is the only reason you need the Pipfile* in the repo.  If not using the lava.py script then you shouldn't need to do a pipenv install (or equivalent for your virtualenv setup).
* lumicube/standard_library.py - this is a modified version of the standard_library.py that is used by the web UI to be able to be used remotely.  I've not tested every function but am reasobaly confident it will support all the main API calls as the cube was designed to control other cubes (which is why this works).
* Piplock* - for use with `pipenv` when wanting to 

### lava.py

The example lava lamp is one of my favourites but it relies on a "noise generation function" that is actually embedded into the LumiCube daemon.  I swapped out the use of that function which is inaccessible to a remote program (or one not running inside the daemon) to use the pure python opensimplex library.  This is only one line change in the code and not as complex as it seems.  It does however need the use of the `opensimplex` python library and you will need to add the library with `pip` or `pipenv`.  *This is another reason for executing your code outside of the cube as it allows you to use any of the myriad of python libraries accessible to you on the Internet into your codebase.*

The only reason the `Piplock` files are in the repo currently is to document / install the [opensimplex](https://pypi.org/project/opensimplex/) library needed for the `lava.py` script.

## How to use

1. Clone the repo.

2. Setup a virtual environment (eg Pipenv)

```
pipenv install
```

3. Make any changes to the scripts to point to your cube.

4. Then execute the script you wish to use, for example:

```
python clock.py
```

5. Make your own scripts based on the examples in the codebase ensuring that the "template" code is at the top of the main python file you call.


```
from lumicube.standard_library import *

cube = None

if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube();
else:
    # connect to my remote cube if not running locally (eg from my Mac)
    # PUT YOUR OWN HOSTNAME FOR YOUR CUBE HERE
    cube = LumiCube("cube.local")
```

### Additional notes

This file is taken directly from the LumiCube open source repo with a few modifications so that you can run commands using the LumiCube python API on a remote computer.  This is what I bought my LumiCube for - so that I could remotely control it based on things happening on my local computer.  I was frustrated that I needed to access the web API on the cube to code it and so this is my solution which works for my purposes and I supply here for anyone else wanting to do something similar.  *Be nice - I only dust off my Python skills about once per year!*

The original AbstractFoundry code can be found here so you can compare:

[Original standard_library.py](https://github.com/abstractfoundry/lumicube-daemon/blob/main/src/main/resources/META-INF/resources/python/foundry_api/standard_library.py)

The main changes made are simple and only prevent the default cube from being created as it is expecting to connect to a host machine with the LumiCube daemon installed which my local Mac will not have.  I have added code to throw an exception if you try to connect to the daemon if it does not exist (ie if you are trying to locally (localhost) connect to the LumiCube on your remote computer).

Removing this default cube creation means that in your code you *MUST* create your own cube instance using, for example:

```cube = LumiCube("cube-hostname")```

Where "cube-hostname" is the cube's IP address or hostname.  I've set the hostname for my cube to be "cube.local" and so that I can connect anywhere on my local network using the following and not needing to mess with remembering IP addresses or setting up a local DNS on my LAN:

```cube = LumiCube("cube.local")```

Or even better:

``` 
  cube = None

  if isRunningOnCube():
    # connect locally if running locally
    cube = LumiCube()
  else:
    # connect to my remote cube if not running locally (eg from my Mac)
    cube = LumiCube("cube.local")

  # my code here...
```

For those following the examples in the cube's manual you will need to make some changes to make them work as the default cube and its aliases are not available as a result of the above changes.  See the commented out section at the end of the file if you want to replicate these or just put `cube.` in front of your calls to the cube. I prefer the prefixing as I like the non-abstracting of the fact the cube API is actually a class. It was a small peev of mine from the manual as it hid something important from the coder I think.


