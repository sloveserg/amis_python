x=(int(input('Введіть x:')))
y=(int(input('Введіть y:')))
x1=(int(input('Ввеідть x1:')))
y1=(int(input('Введіть y1:')))
n1=x+1
k1=y+1
n2=x-1
k2=y-1
if x1==n2 and y1==y:
                            a='Yes'
if x1==x and y1==k2:
                            a='Yes'
if x1==x and y1==k1:
                            a='Yes'
if x1==n1 and y1==y:
                             a='Yes'
else:
         a='No'
if k2==y1 and n2==x1:
                                  a='Yes'
if x1==n2 and y1==k1:
                                a='Yes'
if x1==n1 and y1==k1:
                                   a='Yes'
if  x1==n1 and y1==k2:
                                   a='Yes'

if (x<0 or x>9) or(x1<0 or x1>9) or(y<0 or y>9) or (y1<0 or y1>9):
                                                                   a='Error'
print('Відповідь:')
print(a)
