start = int(input("Enter start :"))
stop = int(input("Enter stop :"))
skip = int(input("Enter Skip :"))

for i in range(start, stop):
    if start < stop :
        
        
        if i == skip:
            continue
        print(i)
    else:
        print("Invalid Choice")
