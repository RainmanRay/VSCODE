"""
age=28
name="Ray"
print("{0} was {1} age this year!".format(age,name))


print("{a} is named as {b}".format(a="Math",b="Morden Math"))
print("{0:_^11}".format("hello"),end=' ')
print("{0:.5f}".format(1.0/3))
print(r"\n")


number = 23
guess = int(input("Enter an integer :"))
if guess==number:
    print("Equal!")
else:
    print('Null')
"""
"""for i in range(1,5):
    print(i)
"""



'''
while True:
    s=input("Enter sthing :")
    if s=='quit':
        break
    print("Re-input...")    
'''
'''
def say_hello(name):
    print("greatings from {0}".format(name))

say_hello('ray')    '''


'''def func():
    global x
    print("x is ",x)
    x=2
    print("change globle x to ",x)

func()
print("x now is ",x)'''
'''
def func(a=5,*b,**c):
    print('a',a)

    for x in b:
        print('one of x',x)
    for x,y in c.items():
        print(x,y)

func(19,2,4,5,b=12,c=34,f=54)     '''

'''
def print_max(x,y):
    
    x=int(x)
    y=int(y)

    if x>y:
        print(x,'is max')
    else:
        print(y,'is max')
print_max(3,5)
print(print_max.__doc__)      
'''
'''
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)


print('\n\nThe PYTHONPATH is :',sys.path,'\n')'''
st='new string'
num=10000
print(st+str(num))