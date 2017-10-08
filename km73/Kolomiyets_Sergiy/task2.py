while True:
    x=(input('Катет1:'))
    y=(input('Катет2:'))
    if float(x)>0 and float(y)>0:
         S=(float(x)*float(y))/2
    if float(x)<0 and float(y)<0:
         S=Error
    print('Ploscha:',S)
input()
