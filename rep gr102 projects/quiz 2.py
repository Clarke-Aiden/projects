'''
x = 40
if x >= 20:
     print('1',end=' ')
print('2', end=' ')


def magic_increaser(x):
    x = x * 5
    return x

x = 5
x = magic_increaser(x)
print("x = ", x)

def magic_increaser(x):
    x = x * 5

x = 5
magic_increaser(x)
print("x = ", x)

x=10
import random
while x==10 :
    p = random.randrange(0, 101)
    print(p)
'''
def add_my_stuff(a,b,c):
    my_total = a + b + c
    return my_total
    print("My total was ", my_total)

my_total = add_my_stuff(4, 5, 6)
print("Thank you and good bye!")