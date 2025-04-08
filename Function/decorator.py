""" 

burger - function
extra chees - extra feature
main function > function add
without changing the main function code 
like two factor authentication
"""
def my_decorator(func):
    def Wrapper():
        print("Somthing is happening before the function is called ")
        func()
        print("Something is happening after the function is called")
    return Wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()