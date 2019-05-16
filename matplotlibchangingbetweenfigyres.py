import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(211)
a1=[1.0,2.0,3.0]
plt.plot(a1,[7,8,9],'ro',linewidth=5)
plt.subplot(212)
plt.plot([12,4],[5,7])

plt.figure(2)
plt.plot([3,4,5],[6,5,6],'g^',linewidth=9)
plt.show()
