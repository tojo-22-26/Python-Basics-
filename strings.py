#slicing string in python
#both start and end points are assigned
b=(input("Enter any string: "))
print(b[2:5]) #here slicing starts from the starting no itself but ends at n-1th position like(for 5 its 5-1=4)

#slice from start
c=(input("Enter another String: "))
print(c[:5]) #it will slice the string from start to position 4

#Slice to the end
print(c[2:]) #It will slice from a position till the end


#Modify Strings
a="Hello, World"
print(a.upper()) #It will print the string in Upper case
print(a.lower()) #It will print the string in lower case
print(a.strip()) #Removes the white spaces from both ends but not from in-between the words
print(a.replace("H","G"))#replaces the string with another string
print(a.split(",")) #splits returns a list where the text between the specified separator becomes the list items.


#Concatenation
p="Hello"
o="World"
i=p+o
print(i)

#using format string "f-string"
age = 21
txt = f"My name is Tojo, I am {age:.2f}"
print(txt)


#Python Booleans
print(10>9)
print(10==9)
print(bool("hello"))
print(bool(15))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#Python Operators
print(10+5)
print(10-5)
print(10/5)
print(10*5)

#Python Lists
myList=["Tojo", True, 55, "Jojo", "Srijo"]
print(myList)#prints the entire list
print(myList[0])#prints the first element of the list
print(myList[1])#prints the second element of the list
print(myList[2])#prints the third element of the list
print(len(myList))
print(type(myList))#returns the type of the list
print(myList[:4]) #returns elements from the list within a certain range
#checking if a specified item is present in the list
if "Tojo" in myList:
    print("Present")

#changing data in List
myList[1]="Ashanka"
print(myList)
#insert data into list
myList.insert(2,"Atandra")
print(myList)
#append is same as insert.... by default it inserts at the end if no such position is mentioned