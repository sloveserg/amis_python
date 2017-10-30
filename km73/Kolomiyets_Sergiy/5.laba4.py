N = int(input("Введіть кіл-ть кеглів: "))
posl = ["I"]*N
K = int(input("Введіть кіл-ть кидків: "))
for i in range (K):
    li = int(input("Введіть номер першої збитої кеглі: "))
    ri = int(input("Введіть номер останньої збитої кеглі:"))
    for k in range(li, ri+1):
        posl[k-1] = "."
for m in range(len(posl)):
    print(posl[m], end = "")
input()
