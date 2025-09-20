import numpy as np
var1=np.array([1,2,3,4,5,6,7])
print(var1)
print()
#printing from no.1 to no. 5
print("From Starting to 5th position 5: ",var1[1:5])
#slicing : variable name[start:stop:steps/gap]
#ex: print(var[1(start):5(stop):2(step/gap)])
print("from starting to position 5: ", var1[:5])
#[:5] blank means from the starting
print("from position no. 1 till end: ", var1[1:])
#[2: ] means from position 1 till end


#for 2D arrays
var2=np.array([[1,2,3,4],[5,6,7,8],[11,12,13,14]])
print()
print(var2)
print()
print("From 1st position's array from 5 to 7: ", var2[1,:2])
