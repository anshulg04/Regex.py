import re
str=r"please send your feedback at " + input()
pattern="\w+@\w+\.\w+\.\w+"    #//         "\S+@\S+"
x=re.findall(pattern,str)
print(x)
