import numpy as np
a=np.tile(np.array([0,10,20]),(3,1)) #copies are created 
print(a)
a=a.T #transpose of a
print("Transpose of a")
print(a)

b=np.arange(3)
print("matrix b:")
print(b)
print("sum of a and b") #we created just 1 row from b but still adding with the a
print(a+b)

#now lets

a=np.arange(0,40,10)
print("size in 1d",a.shape)
a=a[:,np.newaxis] #adds a new axis
print("Size of ain 2d",a.shape)
print("A matrix")
print(a)
print(a+b)
