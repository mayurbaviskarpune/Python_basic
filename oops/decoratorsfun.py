# decorators are nothing but function that chage the existing 
# function defination without changing old function code
import time

def mydecore(fun):
    def wrapper():
        print("befor function",)
        fun()
        print("after fun")
    return wrapper
@mydecore
def demo_fun():
    print("this is demo functio") 

demo_fun()