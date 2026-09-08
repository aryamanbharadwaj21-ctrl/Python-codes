def fibonacci(n):
    if n<=1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the number of terms: "))
if n<0:
    print("Invalid input, number of terms cannot be negative. ")
else:
    print("Fibonacci series:",end=" ")
    for i in range(n):
        print(fibonacci(i),end=" ")
