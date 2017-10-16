x=(int(input('Введіть x:')))
x1=x%4
x2=x%100
x3=x%400
if ((x1==0 and x2>0 ) or x3==0):
                                                 print('LEAP')
else:
                                                 print ('COMMON')

            
       
