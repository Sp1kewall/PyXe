import requests, os, sys, zipfile
import shutil
from os import path
import jwd


zipfile = zipfile.ZipFile('main.zip')

zipfile.extractall()

shutil.rmtree('!terminal')

shutil.move("Space-Terminal-main/!terminal", '.')

shutil.rmtree('Space-Terminal-main')

zipfile.close()

jwd.jwd()
