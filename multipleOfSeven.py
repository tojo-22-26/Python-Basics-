while True:
    num=int(input("Enter the number: "))
    if(num%7==0):
        print("Yes,",num," is a multiple of 7.")
    else:
        print("No,",num, " is not a multiple of 7.")
        
    retry=input("Want to continue? (Y/N): ").lower()
    if(retry!='y'):
        break