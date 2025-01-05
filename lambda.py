
x=lambda a:a+a
print(x(1000))  



x=lambda a,b,c:a*(b/c)
print(x(10,20,30))





def fun(n):
    return lambda a : a * n
my_doubler=fun(2)
my_tripler=fun(3)
print(my_doubler(11))
print(my_tripler(10))