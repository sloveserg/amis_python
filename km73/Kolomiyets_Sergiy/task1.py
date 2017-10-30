x=input('Vvedit poslidovnist:').split()
y=int(input('Rist Petra:'))
q=0
for i in range(len(x)):
             n=int(x[i])
             if n >= y:
                    q=i+1
print('Nomer:',q+1)
