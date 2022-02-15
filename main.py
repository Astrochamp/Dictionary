def checkInstalled(pkg):
  import importlib.util
  import sys
  if pkg in sys.modules:
    return True
  elif (spec := importlib.util.find_spec(pkg)) is not None:
    return True
  else:
    return False

def install(package):
  import sys, subprocess
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if not checkInstalled('wiktionaryparser'):
  install('wiktionaryparser')
from pathlib import Path
home = str(Path.home())
from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
import ast
import os
import textwrap
columns = str(os.get_terminal_size())
columns = columns[columns.find("=")+1:columns.find(",")]
clear = lambda: os.system('clear')
slines = lambda: print('\n'+"-"*int(columns))
elines = lambda: print("-"*int(columns)+'\n')
wrapper = textwrap.TextWrapper(initial_indent='   ', width=int(columns), subsequent_indent='   ')

while True:
  word = str(input("Enter your word: \n"))
  try:
    rawText = str(parser.fetch(word, "latin"))
    dicted = ast.literal_eval(rawText)[0]
    defs = dicted["definitions"][0]
    slines()
    print(f'{defs["text"][0]}:')
    for part in defs["text"][1:]:
      print(wrapper.fill(part))
    elines()
  except:
    slines()
    print(f"{'Word not found!'.center(int(columns))}")
    elines()