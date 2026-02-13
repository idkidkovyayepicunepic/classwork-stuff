import random
n=10
randomnumbers=[[random.randint(1,10) for i in range(n)] for j in range(2)]
newtable=[]
for i in randomnumbers:
    i.sort()
    for j in i:
        newtable.append(j)
for i in range(n*2):
    for j in range(n*2):
        smallest=1
        try:
            if newtable[j]>newtable[j+1]:
                newtable[j+1], newtable[j] = newtable[j], newtable[j+1]
        except:
            pass

print(newtable)
