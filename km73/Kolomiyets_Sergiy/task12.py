n = int(input("Введите кол-во клеток по горизонтали - "))
m = int(input("Введите кол-во клеток по вертикали - "))
k = int(input("Введите кол-во отрезаных клеток - "))
if k <= (m*n):
    if (k%n == 0) or (k%m == 0) :
         a = "YES"
    else:
         a = "NO"
else:
     a = "NO"
print(a)
input()
