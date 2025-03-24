x = 100

def fun():
    global y 
    y = 200
    print(x)

fun()
print(x)
try:
    print(y)
except:
    print("y we cant access it is local variable")