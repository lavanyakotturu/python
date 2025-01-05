#reverse of a  number
num=int(input("enter a number:"))
temp=num
rev=0
while num > 0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse of {} is {}".format(temp,rev))



#fibonacci series
num=int(input("enter a num:"))
n1,n2 =0, 1
print("fibonacci series:",n1,n2,end="")
for i in range (2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end="")
print()
