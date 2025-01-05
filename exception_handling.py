a=input(f"enter a number:")
b=input(f"enter b number:")
try:
    c=int(a)+int(b)
    print(c)
except Exception as e:
    print(e)




a=int(input(f"enter a number:"))
try:
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
except Exception as e:
    print(e)
else:
    print("else block will executed when there is no exception")





a,b=int(input(f"enter a number {a},{b}"))
try:
    if a>b:
        print("a is greater than b")
    else:
        print("not greater")
except Exception as e:
    print(e)
finally:
    print("always prints finally statement")





a=int(input("enter a number"))
b=int(input("enter a num"))
try:
    if a>b:
        print("a is greater than b")
    else:
        print("not greater")
except Exception as e:
    print(e)
else:
    print("it will execute when there is no erron in try block")
finally:
    print("always prints finally statement")







try:
   print('b')              #risky code(becoz it's not having (''))
except:
    print("error")
else:
    print("no error")
finally:
    print("always")

 





try:
    print("a"+10)
except TypeError:
    print("type error")
except ValueError:
    print("value error")






try:
    a=10
    b=0
    print(a/b)
except:
    print("run time error")
else:
    print("no error")
finally:
    print("always")















    