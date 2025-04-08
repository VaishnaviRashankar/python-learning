"""  
Generator behavior behave like iterator and genarator generate the ondemand value

yield keyword use
use for genarate sequence of value over time operate on one at a time did not consume whole memory
"""

def count_down(num):
    while num > 0:
        yield num #yield values one at a time
        num -= 1
for number in count_down(5):
    print(number)