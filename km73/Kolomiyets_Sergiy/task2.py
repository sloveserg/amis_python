x = input().split()
b=[]
for i in range(len(x)):
    p = x.count(x[i])//2
    if x[i] not in b:
        for m in range( p):
            b.append(x[i])
print(len(b))
