#Write a program to ask the user to enter name of their 3 favourite movies and store them in a list.
while True:
    i=0
    name=input("Enter your Name: ")
    print("Enter the 3 favourite movie names: \n")
    list1=[]
    for i in range(0,3):
        mov=input("Enter here: ")
        list1.append(mov)
    print("The 3 favorite movies of",name," is:",list1)
    retry=input("Want to continue? (Y/N):").lower()
    if(retry!='y'):
        break