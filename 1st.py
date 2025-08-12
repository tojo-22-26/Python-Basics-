#recalling python basics


print("Hello World")
#this is a single line comment 
'''
this is a comment on multiline
print("Hello")

'''
name=input("Enter your name: ")
print("Hello", name)
x=5
print(x)
x="This is a string"
print(x)
x=10

print(bool(x))

number=int(input("Enter any number:"))
print("The number is:",number)

print("Sum:",x+number)
print("Diff:",x-number)
print("Prod:", x*number)
print("rem:", x/number)
for i in range(x,0, -1):
    print("* " *i)