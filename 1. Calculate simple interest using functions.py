def si(p,t=2,r=10):
    i=(p*t*r)/100
    return(i)
p=float(input("Enter the principle amount: "))
choice_="n"
choice=input("Is the rate of interest 10%? (Enter y/n): ")
if choice=="y":
    choice_=input("Is the time 2 years? (Enter y/n): ")
if choice=="y" and choice_=="y":
    print("The simple interest to be paid is Rs. ",si(p))
elif choice=="y" and choice_=="n":
    t=int(input("Enter the number of years: "))
    print("The simple interest to be paid is Rs. ",si(p,t,r=10))
elif choice=="n" and choice_=="n":
    r=float(input("Enter the rate of interest: "))
    t=int(input("Enter the number of years: "))
    print("The simple interest to be paid is Rs.",si(p,t,r))
else:
    print("Invalid input")

    
