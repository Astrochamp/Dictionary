try:
  from wiktionaryparser import WiktionaryParser
  parser = WiktionaryParser()
  import ast
  import textwrap
  import os
  import sys
  columns = str(os.get_terminal_size())
  columns = columns[columns.find("=")+1:columns.find(",")]
  clear = lambda: os.system('clear')
  slines = lambda: print('\n'+"-"*int(columns))
  elines = lambda: print("-"*int(columns)+'\n')
  wrapper = textwrap.TextWrapper(initial_indent='   ', width=int(columns), subsequent_indent='   ')
  import argparse
  argparser = argparse.ArgumentParser(description='Look up the definition of (most) Latin words')
  argparser.add_argument('word', metavar='word', type=str, help='the word to define')
  args = argparser.parse_args()
  
  word = args.word
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
except:
  print("Error, something went wrong! Have you run the installer yet?")
  input()
  sys.exit()