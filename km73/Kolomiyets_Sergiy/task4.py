while True:
    N=(input('Введіть кількість студентів:'))
    K=(input('Введіть кількість яблук:'))
    if int(N)>0 and int(K)>0:
       W=int(N)//int(K)
       L=int(N)%int(K)
       if int(N)<0 and int(K)<0:
        W=Error
        L=Error
    print('Вивести кількість яблук, що дістались кожному студенту:',W)
    print('Вивести кількість яблук, що лишилиьс у кошику:',L)
    input()
