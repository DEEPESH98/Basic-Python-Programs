import numpy as np

a=np.array([[1,2,3],[4,5,6],[1,2,3]])
b=np.array([[1,2,3],[4,5,6],[1,2,3]])

#shape check ker ne ke liye
print(a.shape)
print(b.shape)

#printing part
print(a)
print(b)

#Airthematic operations
print(a*2)
print(a+2)
print(a/2)
print(a**5)
print(a+b)

#perticular value calling  [R,C]

print(a[0])
print(b[0])

print(a[0][0])


#other operations
print(a[0:2])

print("\n",a[0:])

#perticular colum ke liye
print("\n",a[0: ,0])

print("\n",a[0: 1,0])

print("\n",a[0: 2,0])

print("\n",a[0:,0:2])
      
print("\n",a[0:,[0,2]])

print("\n",a[[0,2]])
