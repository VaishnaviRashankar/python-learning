""" 
identity : To determine if two variable point to the same object in memory
is -> True
is nto -> True
 
"""
a = [1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)