b = float(input("Enter number: "))
n = int(input("Enter power of number:"))
def power(b, n):
    if n == 0:
        return 1
    else:
        return b*power(b, n-1)

