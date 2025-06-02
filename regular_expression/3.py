import re
s = "My 2 favorite numbers is 45 and 63"
n = re.findall('[0-9]+',s)
print(n) # ['2', '45', '63']

s1 = "This is a beautiful pen"
st = re.findall('[AISC]+',s1)
print(st) # []

s1 = "This is a beautiful pen"
st = re.findall('[AISCTp]+',s1)
print(st) # ['T', 'p']
