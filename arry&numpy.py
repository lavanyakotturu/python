'''
from array import *
vals=array('i',[1,2,5,-8,10])
#print(vals)
#print(vals.buffer_info())            #will display address and length
#print(vals.typecode)                  #will show datatype
#vals.append(13)
#vals.remove(-8)
#vals.reverse()
#for i in range(4):
#     print(vals[i])
newarr=array(vals.typecode,(a*a for a in vals))
for e in newarr:
    print(e)
    '''




#user input in array:

'''
from array import *
arr=array('i',[])
n=int(input("enter length of the array"))
for i in range(n):
    x=int(input("enter the value of array"))
    arr.append(x)
print(arr)
val=int(input("enter search value"))
k=0
for i in arr:
    if i==val:
        print(k)
        break
    k+=1
    print(arr.index(val))
''' 


#ways of creating array:
'''
from numpy import *
#arr=array([1,3,5])
#print(arr.dtype)
#arr=linspace(0,15,16)      #start,stop,parts
#arr=linspace(0,15)          #50 parts by default
#arr=arange(0,100,5)
#arr=logspace(1,30,5)
#arr=zeros(5)
#arr=ones(5)
print(arr)
'''


#copying in array:

'''
from numpy import *
arr1=array([1,2,3,5,7])
#arr=arr+5
#print(arr1)
#arr2=array([1,34,54,6,8])
#arr3=arr1+arr2                             #vectorized operation
#print(arr3)
#print(sqrt(arr1))
#print(min(arr1))
#print(concatenate([arr1,arr2]))
#arr2=arr1
#print(id(arr1))
#print(id(arr2))
#arr2=arr1.view()
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

shallow copy:

#arr2=arr1.view()
#arr1[1]=6
#print(arr1)
#print(arr2)
#print(id(arr1))                #same values but different address
#print(id(arr2))

deep copy:

arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)                    #diff values and diff address
print(id(arr1))
print(id(arr2))
'''



