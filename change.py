
n = int(input())

a = [input() for i in range(n)]

ans = ""
for i in a:
    if i[-2:] == "sh" or i[-2:] == "ch":
        ans = i[:-2] + "es"
        print(ans)
        ans = ""
    elif i[-1:] == "s" or i[-1:] == "o" or i[-1:] == "x":
        ans = i[:-1] + "es"
        print(ans)
    elif i[-2:] == "fe":
        ans = i[:-2] + "ves"
        print(ans)
    elif i[-1:] == "f":
        ans = i[:-1] + "ves"
        print(ans)
    elif i[-1:] == "y" and (i[-2] != "a" or i[-2] != "i" or i[-2] != "u" or i[-2] != "e" or i[-2] != "o"):
        ans = i[:-1] + "ies"
        print(ans)
    else:
        ans = i + "s"
        print(ans)
        
    #print(i[-2:])


"""
L = ["boy","girl", "pen","book","dish","watch","box","xman"]
for i in L  :
    if i[-1]=="h":
        a=i+"es"
    elif i[-1]=="x":
        a=i+"es"
    else:
        a=i+"s"   
    print(i)
    print(i[-1])
print(a)
print(L[1])
"""


