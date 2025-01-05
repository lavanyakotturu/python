#block of code


def func():               #function definition
    print("hey guys")    #function body
func()                    #function call





def func(*a):            # *- arbitary arguments
    print("hey guys",a)
func(1,2,3)




def add(x,y):
    z=x+y
    print("hello",z)
add(3,4)



def add(x,y):
    z=x+y
    return z
result=add(3,4)
print(result)





def add_sub(x,y):
    z=x+y
    p=x-y
    return z,p
result=add_sub(5,8)
print(result)




#types of arguments arguments:

def add(x,y):          #x,y-formal arguments
    z=x+y
    print(z)
add(2,8)               #2,8-actual arguments
    
'''
actual arguments:
1)position
2)keyword
3)default
4)visible length
'''


def my_func(name,age,gender):
    print(name,age,gender)
my_func("lavanya",21,"f")




def update(x):
    x=8
    print(x)
update(10)



def my_function(*a):
    print("younger child is",a[2])
my_function("prasanna","yamuna","lavanya")




def person(name,*data):
       
        print(name)

        print(*data)

person("lavanya",21,"srklm",532218)





def person(name,**data):       #kwargs(keyword arguments)
       
        print(name)

        print(data)

person(name="lavanya",age=21,city="srklm",pin=532218)




def person(name,**data):       
       
        print(name)
        for i,j in data.items():
          print(i,j)

person(name="lavanya",age=21,city="srklm",pin=532218)





#global keyword:

a=10
def something():         #local variable
     a=15
     
     print(a)


print(a)




a=10
def something():         #local variable
     global a
     a=15
     
     print("in function:",a)

something()
print("out function:",a)





def count(list):
     even=0
     odd=0
     for i in list:
          if i%2==0:
             even+=1
     else:
          odd+=1
     return even,odd
list=[10,15,20,25,30,35]
even,odd=count(list)
print(even)
print(odd)


















