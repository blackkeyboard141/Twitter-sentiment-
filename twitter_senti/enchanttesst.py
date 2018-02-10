import sys
import re

line = "my name is khan, and i am not sadasaas"
line = line.lower()
line = re.sub(r"[^A-Za-z]", " ", line.strip())
words = line.split()
print words
print type(words)