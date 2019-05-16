import matplotlib.pyplot as plt
x1=[1,2,3]
x2=[4,5,6]
y1=[5,6,7]
y2=[7,8,9]
lines=plt.plot(x1,y2,x2,y2)
plt.setp(lines[0],color='g',linewidth=5)
plt.setp(lines[1],color='r',linewidth=4)
plt.grid()
plt.show()
