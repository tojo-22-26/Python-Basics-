def converter(val):
    money=val*87.98
    return money

while True:
    amount=float(input("Enter the value(in $): "))
    res=converter(amount)
    print("The Amount in INR is: Rs.",res)
    retry=input("Want to continue? (Y/N): ").lower()
    if(retry!='y'):
        break
