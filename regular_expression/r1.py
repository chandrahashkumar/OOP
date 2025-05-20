import re

file = open('AI.txt',)

for line in file:
    line = line.rstrip()
    if re.search('^Artificial', line):
        print(line)
