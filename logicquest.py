def full_pyramid(n):
 for i in range(0,n):
    for j in range(n-i):
        print("*",end="")
    print()
full_pyramid(10)


#access both key and value using items() from dict 

dict={"name":"lavs","rollno":28}
#print(dict.items())             it will print both keys and vals
for i,j in dict.items():       #it will also
   print(i,j)


#calc the lenth of the string

s="lava nya"
#print(len(s))
def str_len(str1):
   count=0
   for i in str1:
      count+=1
   return count
print(str_len(s))


#calc no. of upper case letters and no.of lower case letters

def str_test(s):
   d={'upper_case':0,'lower_case':0}
   for i in s:
      if i.isupper():
         d['upper_case']+=1
      elif i.islower():
         d['lower_case']+=1
      else:
         pass
   print("upper case letters:",d["upper_case"])
   print("lower case letters:",d["lower_case"])
str_test("Hi I Am Lavanya")


#check if the first and last number of a list is the same

nums=[10,20,30,40,10]
if nums[0]==nums[-1]:
   print("true")
else:
   print("false")
           
#usig functions
nums=[10,20,30,40,1]
def fun(nums):
   first=nums[0]
   last=nums[-1]
   if first==last:
      return True
   else:
      return False
print(fun(nums))     #return false


#check if key is already present in a dictionary

my_dict={1:'a',2:'b',3:'c'}
if 2 in my_dict:
   print("present")        
else:
   print("not present")



#create list of empty dictionary
#[{},{},{}]

print([{} for _ in range(10)])


#extend list without append
l1=[1,2,3,45,5]
l2=[5,6,7,8]
#l1[0:]=l2    #[5,6,7,8]
l1[:0]=l2    #[5, 6, 7, 8, 1, 2, 3, 45, 5]
print(l1)


#fibonacci sequence

def fib(n):
   if n==1 or n==2:
      return 1
   else:
      return(fib(n-1)+fib(n-2))
print(fib(4))


#find largest num among three

x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
if (x>=y) and (x>=z):
   print("x is larger")
elif (y>=x) and (y>=z):
   print("y is larger")
else:
   print("z is larger")



#check if  num is positive or not

s=int(input("enter a number"))
if (s>0):
   print("positive")
elif(s<0):
   print("negative")
else:
   print("zero")



#check even or odd


a=int(input("enter number"))
if (a%2==0):
   print("a is even",format(a))
else:
   print("not")


list=[1,2,3,4,5]
for i in list:
   if i%2==0:
      print(" is even",format(i))
   else:
      print("is odd",format(i))


#to get a substring of a string

s="hello lavanya"
print(s[4:13])
print(len(s))


#get the last element of the list
l=['l','a','v','a','n','y','a']
print(l[-1])



#add two given lists 
l1=[3,45,6,65]
l2=[21,3,54,45,56]
print(l1+l2)


#add two given lists using map and lambda

l1=[3,45,6,65]
l2=[21,3,54,45,56]
s=map(lambda x,y:x+y,l1,l2)
print(list(s))


v1=10.5
v2=12.5
v3=12.15
average=(v1+v2+v3)/3
print(int(average))



var=10.45
var=20.55
print(var)



def pyr(n):
  for i in range(1,5,2):
      print("*")


A=8 
B=3
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)




n=int(input())
if n==28:
    print("i am young")
else:
    print("i am not young")


n=int(input())
if n>1:
    print("You entered more")
elif n>=1:
    print ("You entered less")






a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)