import re

s = 'We just received $56.69 fro cookies.'
p = re.findall(r'\$[0-9.]+',s)
print(p)