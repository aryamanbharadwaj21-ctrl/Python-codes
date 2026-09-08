def binarysearch(l,element):
    l=sorted(l)
    low=0
    high=len(l)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if l[mid]<element:
            low=mid+1
        elif l[mid]>element:
            high=mid-1
        else:
            return(mid)
    if element not in l:
        return(False)
l=[]
n=int(input("Enter the number of elements to be entered: "))
for i in range(n):
    y=input("Enter the element: ")
    l.append(y)
print("Sorted list:",sorted(l))
element=input("Enter the element to be searched for: ")
if not binarysearch(l,element):
    print(element,"not found in list. ")
else:
    print(element,"found at index",binarysearch(l,element))
    
