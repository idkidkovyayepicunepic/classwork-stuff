import random
import time
def linear(lys,element):
    for i in range(len(lys)):
        if lys[i] == element:
            return 1
    return -1

def binary(lys,val):
    first=0
    last=len(lys)-1
    index=-1
    while (first<=last) and (index==-1):
        mid=(first+last)//2
        if lys[mid]==val:
            index=mid
        else:
            if val<lys[mid]:
                last=mid-1
            else:
                first=mid+1
    return index

r=[random.randint(1,10) for i in range(10)]
print("linear:")
start=time.perf_counter()
print(linear(r,1))
end=time.perf_counter()
print(end-start)
print("binary:")
start=time.perf_counter()
print(binary(r,2))
end=time.perf_counter()
print(end-start)
