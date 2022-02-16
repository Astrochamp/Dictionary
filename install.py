import platform
import sys
import os
import subprocess
def checkInstalled(pkg):
  import importlib.util
  if pkg in sys.modules:
    return True
  elif (spec := importlib.util.find_spec(pkg)) is not None:
    return True
  else:
    return False

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])
if not checkInstalled('wiktionaryparser'):
  install('wiktionaryparser')
from pathlib import Path
home = str(Path.home())
if platform.system() == "Windows":
  installLoc = os.path.join(home, 'dictionarylookup.bat')
  f = open(installLoc, "w")
  f.write(
          "@echo off\n"
    f"python \"{__file__.replace('install.py', 'cli.py')}\" %*"
          )
  f.close()
else:
  print("Unsupported OS :(")
  input()
  sys.exit()
input("Succesfully installed, run with dictionarylookup <word> -lang <language>\nPress enter to exit.")
sys.exit()
