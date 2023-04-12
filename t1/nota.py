import numpy as np
p1 = np.linspace(0.0,10.0,20)
p2 = np.linspace(0.0,10.0,20)
t = np.linspace(0.0,10.0,20)


print('P1 P2 Tra P A')
for n1 in p1:
    for n2 in p2:
        for tran in t:
                p = (4*n1+6*n2)/10
                a = (4*p*tran)/(p+3*tran)
                if 5<=a<=5.1 :
                     print(n1,n2,tran,p,a)
                     



