""" 
[expression for item in iterable]

e - x*2 /expression means which operation
item - element which include in list

iterable - range(1,11)
condition optional
"""
# square=[]
# for i in range (1,11):
#     square.append(i ** 2)
# print(square)

square = [i**2 for i in range(1,11) if i%2 == 0]
print(square)