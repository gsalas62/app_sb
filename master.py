import os, sys
sys.path.insert(0, os.path.abspath(".."))
from app_sb import app

if __name__ == '__main__':
	app.run(host="10.50.20.92", port="5000")
