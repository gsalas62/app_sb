import os, sys
sys.path.insert(0, os.path.abspath(".."))
from __init__ import app
from config import *

if __name__ == '__main__':
	app.run(host=Vars.IP, port=Vars.PORT)
