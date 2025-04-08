with open('D:\Python Practical\Exception Handling\data.txt','a')as file:
    content = input('enter data to append = ')
    file.write(content)
    print('appened datas')