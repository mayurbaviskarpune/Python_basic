# function with yield keyword is called generators
# generater return value from function withoute terminating that function


# A generator in Python is a special type of function that returns an iterator and 
# allows you to iterate over values one at a time, on demand, using the yield keyword 
# instead of return.

# Unlike normal functions, generators do not store all values in memory, 
# making them efficient for handling large datasets.

def even_numbers(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i

even_num = even_numbers(10)

for j in even_num:
    print(j)


