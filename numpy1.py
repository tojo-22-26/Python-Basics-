import numpy as np
x=[1,2,3,4]
#creating an array in numpy
y=np.array(x)
#print the array
print(y)
#type of the array
print(type(y))
#array with only zeroes
ar_zero=np.zeros(4)
#printing that array
print(ar_zero)
#In case of 2 dimension
ar_zero1=np.zeros((4,3))
#printing the 2-dimensional array
print()
print(ar_zero1)
#array with only ones
ar_one=np.ones(4)
#printing the array
print()
print(ar_one)
#in case of 2 dimension
ar_one1=np.ones((4,6))
#printing the array
print()
print(ar_one1)
#for diagonal array
ar_dia=np.eye(3)
#printing the array
print()
print(ar_dia)
#for empty array
ar_emp=np.empty(3)
#printing the array, by default it will print the previous value
print()
print(ar_emp)
#for creating an array with a gap
ar_lin=np.linspace(1,20, num=4)
#printing the value
print()
print(ar_lin)



#creating NumPy Arrays with random numbers
#functions:
#rand()- the function is used to generate a random value between 0 to 1.
#randn() - the function is used to generate a random value close to zero. This may return positive or negative numbers as well.
#ranf() - the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half open interval [0.0, 1.0).
#randint() - the function is used to generate a random number between a given range.


var1 =np.random.rand(3)
#printing the random value
print()
print(var1)


var2=np.random.randn(3) #can print numbers close to 0 to 1 and can be negative or positive
#printing it
print()
print(var2)


var3=np.random.ranf(3)
#printing it
print()
print(var3)


var4=np.random.randint(0,15,5) #(0, 15 is the range and 5 is the no. of elements to occur within the range)
#printing it
print()
print(var4)