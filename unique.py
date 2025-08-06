lst=[]
n=int(input("Enter number of elements:")) 
for i in range(n):
    value=int(input("Enter element:"))
    lst.append(value)
unique=[]
for item in lst:
    if item not in unique:
        unique.append(item)
print("Unique element: ",unique)