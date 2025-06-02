import re
head = open('AI.txt')
for line in head:
    line = line.rstrip()
    if re.search('^X-.*:',line):
        print(line)

# MATCH ANY NON-WHITESPACE CHARACTER
head1 = open('AI.txt')
for line in head1:
    line = line.rstrip()
    if re.search(r'^X-\S+:',line):
        print(line)