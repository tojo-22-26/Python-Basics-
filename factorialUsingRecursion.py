def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * fact(n-1)
    
while True:
    num=int(input("Enter the value:"))
    fac=fact(num)
    print("The Result is: ", fac)
    retry=input("Want to continue?(Y/N): ").lower()
    if(retry!='y'):
        break