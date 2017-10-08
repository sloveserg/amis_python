while True:
            n=(int(input(' введите минуты:')))
            a1=n//60
            a2=n%1440
            a3=n%60
            a4=a2//60
            a5=a2%60
            if n<=0:
                   print('время:','00',':','00')
            else:
                 if (0<n<60):
                   print('время:','00',':',n)
                 else:
                      if(60<n<1440):
                                    print('время:',a1,':',a3)
                      else:
                               if(1440<=n):
                                             print('время:',a4,':',a5)


                                             input()
