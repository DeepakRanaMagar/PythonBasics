#to change the value of global variable by using global keyword

x = "First value"

def func():
    global x 
    x="Second value"
func()

print("The value of global variable is "+x)