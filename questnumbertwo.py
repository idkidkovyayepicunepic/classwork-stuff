import random
n=10
r=[random.randint(1,n) for i in range(n)]
print(r)
count=0
for i in r:
    for a in r:
        if (i+a)%2!=0:
            count+=1
print(f"нечётных чисел было обнаружено {count}")
