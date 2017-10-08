while True:
            x=int(input('Iклас:'))
            y=int(input('IIклас:'))
            z=int(input('IIIклас:'))
            x1=((int(x)//2)+(int(x)%2))
            y1=((int(y)//2)+int(y)%2)
            z1=((int(z)//2)+int(z)%2)
            s=int(x1)+int(y1)+int(z1)
            if x<0 or y<0 or z<0:
                                   s=Error
            print('Мінімальна кількість парт',s)                                                      
            input()
