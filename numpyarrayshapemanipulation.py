import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
print("After ravel operation")
print(a.ravel())
print(a.flatten())

print("transpose")
print(a.T)
print("transpose and ravel together")
print(a.T.ravel())
a=a.ravel()
b=a.T.reshape(2,3)
print("reshaping b")
print(b.reshape((2,3)))
#b=b.reshape((2,3))
print(b)
print("modifying values of b")
b[0,0]=1000
print("a matrix")
print(a)
print("we got a values changed")

#lets do in some exception were referneces wont work

a=np.arange(0,6).reshape((3,2))
print("A matrix")
print(a)
b=a.T.reshape(3*2) #this step making the not change
print("modifying values of b")
print(b)
b[0]=12
print(b)
print("a matrix")
print(a)
print("We dint got same ")





