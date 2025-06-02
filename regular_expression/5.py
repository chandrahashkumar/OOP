import re
email_r = 'From: chandrahash@gmail.com Mon June 2 6:8:45 2025'
email = re.findall(r'\S+@\S+',email_r)
print(email) # ['chandrahash@gmail.com']


em = re.findall(r'^From: (\S+@\S+)',email_r)
print(em)