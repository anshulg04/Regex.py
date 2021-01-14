import re
n=int(input())
if n>=2 and n<=15:
    for i in range(0,n):
        str1=input("Enter string")
        str2="[789]\d{9}"
        if re.search(str2,str1):
            print("Yes")
        else:
            print("No")
