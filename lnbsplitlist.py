#adding elements in list
q=[]
for i in range(20):
    a=int(input('enter number = '))
    q.append(a)
print(q)
#slicing the list
l2=q[0:5]
l3=q[15:20]
l4=l2+l3
print(l4)
#squaring the elements of list
square=[i**2 for i in l4 ]
print(square) 
#splitting the list
length = len(l4)

middle_index = length // 2

first_half = l4[:2]
second_half = l4[2:middle_index]
third_half=l4[middle_index:]

print(first_half)
print(second_half)
print(third_half)
        