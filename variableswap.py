x = float(input('Enter the value of X:'))
y = float(input('Enter the value of Y:'))

temp = x
x = y
y = temp

print('The value of X after swapping is :{}'.format(x))
print('The value of Y after swapping is :{}'.format(y))