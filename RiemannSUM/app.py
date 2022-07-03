import numpy as np
import matplotlib.pyplot as plt


f = lambda x: x**3 + 1
a = 0; b = 2; N = 4 
n = 4

x = np.linspace(a,b,N+1)
y=f(x)

X=np.linspace(a,b,n*N+1) 
Y=f(X)

plt.figure(figsize=(10,6))

# This is for left-end point
plt.subplot(1,3,1)
plt.plot(X,Y,'m')
x_left= x[:-1]
y_left= y[:-1]
plt.plot(x_left, y_left, 'm.', markersize= 11)
plt.bar(x_left,y_left, width=(b-a)/N, alpha=0.25, align='edge', edgecolor='m')# transparent
plt.title('left-end RiemanSUM, N={}'.format(N))

plt.show()