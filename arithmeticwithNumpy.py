import numpy as np
#addition
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd=var1+var2
print(varadd)
print()
#subtraction
var3=np.array([2,4,6,8])
var4=np.array([1,2,3,4])
varsub=var3-var4
print(varsub)
print()
#multiplication
var5=np.array([2,4,6,8])
var6=np.array([1,2,3,4])
varmul=var3*var4
print(varmul)
print()
#division
var7=np.array([3,6,9,12])
vardiv=var7/3
print(vardiv)
print()
#Modulus
var8=([2,4,6,8])
var9=([2,2,2,2])
varmod=np.mod(var8,var9)
print(varmod)
print()
#maximum and minimum
var10=([1,2,3,4,5,6])
print("Max: ",np.max(var10),"Position: ",np.argmax(var10))
print("Min: ",np.min(var10), "Position: ",np.argmin(var10))
print()
#sin and cos
var11=np.array([1,2,3,4,5])
print("Sin: ",np.sin(var11))
print("Cos: ", np.cos(var11))
print()
#cumsum
var12=np.array([1,2,3])
print("CumSum: ",np.cumsum(var12))
print()