
def palindrome(list_1):
    list_copy=list_1.copy()
    list_copy.reverse()
    if(list_copy==list_1):
        print("The List is a palindrome List.")
        
    else:
        print("The List is not a palindrome List.")
    return 0

while True:
    len=int(input("Enter the number of elements: "))
    list_1=[]
    for i in range(len):
        num=input("Enter the value:")
        list_1.append(num)
    check=palindrome(list_1)
    retry=input("Want to continue? (Y/N): ").lower()
    if(retry!='y'):
        break