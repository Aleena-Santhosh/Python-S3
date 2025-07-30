even_numbers = []
list=[]
n = int(input("Number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    list.append(num)
for i in list:
    if i%2==0:
        even_numbers.append(i)
print(list)
print("Even numbers:", even_numbers)
