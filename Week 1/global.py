#To create a global variable inside a function

def func():
    global x
    x = "Global variable"
func()

print("This is a " + x)