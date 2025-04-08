try:
    file = open('D:\Python Practical\Exception Handling\info.txt')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('file not found')
    
finally:
    file.close()
    print('file operation')