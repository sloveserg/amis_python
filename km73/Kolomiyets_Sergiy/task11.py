x=(int(input('Введіть x:')))
y=(int(input('Введіть y:')))
x1=(int(input('Введіть x1:')))
y1=(int(input('Введіть y1:')))
n=x+1
n1=x-1
m=y-2
m1=y+2
k=x+2
k1=x-2
l=y+1
l1=y-1
if x1==n and y1==m:
                    a='Yes'
if x1==n and y1==m1:
                    a='Yes'
if x1==n1 and y1==m:
                    a='Yes'
if x1==n1 and y1==m1:
                                a='Yes'
if y1==l and x1==k:
                                 a='Yes'
if y1==l and x1==k1:
                                    a='Yes'
if y1==l1 and x1==k1:
                                           a='Yes'
if y1==l1 and x1==k:
                                               a='Yes'
else:
                      a='No'
if (x<0 or x>9) or(x1<0 or x1>9) or(y<0 or y>9) or (y1<0 or y1>9):
                                                                   a='Error'
print('Відповідь:')
print(a)
