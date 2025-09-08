def sum(n):
    if n==0:
        return 0
    else:
        val=(n + sum(n-1))
        return val
    
while True:
    num=int(input("Enter the value: "))
    res=sum(num)
    print("Result: ",res)
    n=input("Want to Continue? (Y/N): ").lower()
    if(n!='y'):
        break
    