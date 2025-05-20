import re

with open('AI.txt','r') as f:
    text = f.read()
    # print(re.findall('AI',text))
for word in text:
    re.search('^Artificial',text)
    print(word)