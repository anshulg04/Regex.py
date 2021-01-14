import re
str=r"Hello!My name is " + input()+" and my DOJ is " + input() + " and have an experience of 1+ year"
s1="\d{2}/\d{2}/\d{4}"
s2="(\w+[and]$)"
x=re.findall(s1,str)
y=re.findall(s2,str)
print(y)
