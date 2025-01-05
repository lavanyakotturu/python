#blue print of an object

'''
class python():       #class def
    a=2                #class body
    print("a")
'''



class Phone():             #creating a phone class
    def make_call(self):             #methods
        print("let's make a phone call")
    def playig_game(self):
        print("let's play game")
obj=Phone()                #instantiating the object
obj.make_call()            #invoking the methods through objects
obj.playig_game()



class sum():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print(self):
        print(self.a+self.b)
c=sum(3,5)
c.print()


class Vehicle():
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):                #setting and returning the attribute value
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):             
        print("let's make a phone call")
    def playig_game(self):
        print("let's play game")
    
obj=Vehicle()
obj.set_color("pink")
obj.set_cost(50000)
obj.show_color()
obj.show_cost()
obj.make_call()
obj.playig_game()





class Employee():
    def __intit__(self,name,age,salary,gender):       #__init__ constructor
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary :",self.salary)
        print("gender:",self.gender)
a=Employee('lavanya',21,50000,'f')
a.employee_details()









