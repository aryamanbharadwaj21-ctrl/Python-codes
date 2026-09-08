def perfect(n):
    Sum=0
    for i in range(1,n):
        if n%i==0:
            Sum+=i
    if Sum==n:
        return True
    else:
        return False
n=int(input("Enter a number: "))
if perfect(n):
    print("The number is perfect. ")
else:
    print("The number is not perfect.")
    
