while True:
    num=int(input("Enter any Number:"))
    if(num%2==0):
        print(num,", is Even!!")
    else:
        print(num,", is Odd!!")
    
    retry=input("Want to continue? (Y/N): ").lower()
    if(retry!= 'y'):
        break