from sys import argv
import re

pattern = r''

def replacementFunction(match):
  pass

# Redefine pattern and replacementFunction(match) below

pattern = '([A-Z]+)\s*([í\w\-\']+(\s+[í\w\-\']+)*)\s+(\d+\.\d+)\s+(\d+\.\d+)'

def replacementFunction(match):
  return "{} = {}".format(match.group(2), round(float(match.group(4)), 4))

  # Redefine pattern and replacementFunction(match) above
with open(argv[1]) as infile:
  for line in infile:
    print(re.sub(pattern, replacementFunction, line).strip())