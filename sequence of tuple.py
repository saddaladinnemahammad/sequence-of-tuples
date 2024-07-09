def Test(s,e):
    tuple_list=[(i,i**2) for i in range(s,e+1)]
    return tuple(tuple_list)
s=int(input())
e=int(input())
result=Test(s,e)
print(result)

SLICING

n = int(input())
numTuple = tuple(map(int, input().split()[:n]))

a, b = list(map(int, input().split()))
c = int(input())
d = int(input())
slice1 = numTuple[a:b]
print(*slice1)
slice2 = numTuple[c:]
print(*slice2)
slice3 = numTuple[:d]
print(*slice3)
slice4 = numTuple[:]
print(*slice4)



INDEXING

n=int(input())
numTuple = tuple(map(int, input().split()))

index1 = numTuple.index(int(input()))

index2 = numTuple.index(int(input()))

index3 =numTuple.index(int(input()))

index4 =numTuple.index(int(input()))
print(numTuple)
print(index1)
print(index2)
print(index3)
print(index4)


YEAR-MONTH-DATE

t=int(input())
years=(t//365)
months=((t-years*365)//30)
days=((t-years*365)-months*30)
print(days,months,years,sep="/")
