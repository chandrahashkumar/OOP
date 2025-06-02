import re

with open('AI.txt','r') as file:
    for line in file:
        host = re.findall('^From: .*@([^ ]*)',line)
    print(host)