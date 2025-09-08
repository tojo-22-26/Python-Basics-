def factorial(val):
    prod=1
    while val>=1:
        prod*=val
        val-=1
    return prod
while True:
    val=int(input("Enter the number: "))
    res=factorial(val)
    print("The Result is: ", res)
    retry=input("Want to continue? (Y/N): ").lower()
    if(retry!='y'):
        break