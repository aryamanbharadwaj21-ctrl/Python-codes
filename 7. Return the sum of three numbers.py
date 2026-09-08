def Sum():
    add=0
    l=[]
    for i in range(3):
        y=float(input("Enter the value to be added: "))
        l.append(y)
    return sum(l)
def main():
    print("The sum of all the values is",Sum())
main()


