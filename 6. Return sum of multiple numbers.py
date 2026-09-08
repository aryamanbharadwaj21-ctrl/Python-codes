def Sum():
    add=0
    l=[]
    n=int(input("How many values do you want to add?: "))
    for i in range(n):
        y=float(input("Enter the value to be added: "))
        l.append(y)
    return sum(l)
def main():
    print("The sum of all the values is",Sum())
main()


