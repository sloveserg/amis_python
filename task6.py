x=(int(input('Введіть x:')))
y=(int(input('Введіть y:')))
x1=(int(input('Ввеідть x1:')))
y1=(int(input('Введіть y1:')))
if x==x1 or y==y1:       
                           a='Yes'
else:
         a='No'
if (x<0 or x>9) or(x1<0 or x1>9) or(y<0 or y>9) or (y1<0 or y1>9):
                                                                                                  a='Error'
print('Відповідь:')
print(a)
