import numpy as np

#1D array
var=np.array([1,2,3,4,5])
print(var)
print("Dimension: ",var.ndim)
print()
for i in var:
    print(i)
print("---------------------------------")
print()
#2D array
var1=np.array([[1,2,3,4],[5,6,7,8]])
print(var1)
print("Dimension: ",var1.ndim)
print()
for j in var1:
    for k in j:
        print(k)
print("----------------------------------")
print()
        
#3D array
var2=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(var2)
print("Dimension: ",var2.ndim)
print()
for m in var2:
    for n in m:
        for o in n:
            print(o)
print("---------------------------------")
print()
#using np.nditer function
var3=np.array([[[1,2,3,4,5],[5,4,3,2,1],[5,6,7,8,9],[7,8,9,1,2]]])
print(var3)
print("Dimension: ",var3.ndim)
print()
for i in np.nditer(var3):
    print(i)
print("---------------------------")
print()
#changing the datatype while iterating
var4=np.array([[1,2,3,4],[2,3,4,5],[4,5,6,7]])
print(var4)
print("Dimension: ",var4.ndim)
print()
for i in np.nditer(var4, flags=['buffered'],op_dtypes=["S"]):
    print(i)
print("----------------------------")
#printing values along with the index nos.
var5=np.array([[[1,2,3,4],[9,8,7,6],[6,5,6,5]]])
print(var5)
print()
print("Dimension: ", var5.ndim)
print()
for i,d in np.ndenumerate(var5):
    print(i,d)
print("-----------------------")