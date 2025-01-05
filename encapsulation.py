'''
1)encapsulation
2)polymorphism
3)data abstraction

1)encapsulation:
wrapping of variables and methods into a single unit is called encapsulation
public
private(__)
protected(_)
'''
class encp():
    __a=5  #private
    _b=10  #protected
    print(__a)
    print(_b)




class encp():
    def __init__(self,a,b):
     self.__a=a    #private
     self._b=b  #protected
class encp2(encp):
    def out(self):
       print(self._b)
c=encp2(5,6)
c.out()
  



#polymosrphism:

def add(a,b):
   print(a+b)
add(3,5)
add('a','b')
add([1,2],[3,4])
add((1,2),(3,4))




#abstraction
#hiding the information or implementation is nothing but data abstraction
