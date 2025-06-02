import re

head = open('AI.txt',)

for line in head:
    line = line.rstrip()
    if re.search('Artificial', line):
        print(line)


head1 = open("AI.txt")
for line in head1:
    line =line.rstrip()
    if re.search('^human',line):
        print(line)

head2 = open('AI.txt')
for line in head2:
    line = line.rstrip()
    if re.search('^FROM:',line):
        print(line)
