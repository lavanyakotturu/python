#factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=5
result=fact(x)
print(result)


#recursion

def greet():                
    print("hello")            #limit 1000
    greet()
greet()




import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("hello", i)
    greet()

greet()

