"""
below function accept number and 
calculate number of digits in 
number and return its count
"""

def count_length_of_number(num):
    count = 0
    while num >0:
        count+=1
        num //= 10
    return count

"""
below function is use to reverse number by taking
one number as input
at it return the output as revese of 
that number
"""

def Reverse_string(num):
    num2=0
    while num > 0:
        digit = num % 10
        num2 = num2*10+digit
        num //= 10  
    return num2
