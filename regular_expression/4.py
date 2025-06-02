import re
# Greedy
s = 'From: using the : i pics of none'
f = re.findall('^F.+:',s)
print(f) # ['From: using the :']


# Non-Greedy
f1 = re.findall('^F.+?:',s)
print(f1) # ['From:']