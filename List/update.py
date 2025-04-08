lst = [1,2,3,4]
print(f'Before{lst}')
# using indexing
lst[0]='python'
print(f'After{lst}')
# using slicing
lst[0:3]=10,20,30
print(lst)