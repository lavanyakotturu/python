'''
types:
1) single inheritance
2)multilevel inheritance
3)multiple inheritance
4)hierarchical ineritance  or hybrid



'''






class father():
    def output(self):
        print("i am father")
class child(father):
    def outputc(self):
        print("i am child")
c=child()
c.outputc()
c.output()                




class grandfather():
    def outputg(self):
        print("i am grandfather")
class father(grandfather):
    def output(self):
        print("i am father")
class child(father):
    def outputc(self):
        print("i am child")
c=child()
c.outputc()
c.output()
c.outputg() 




class father():
    def output(self):
        print("i am father")
class mother():
    def outputm(self):
        print("i am mother")
class child(father,mother):
    def outputc(self):
        print("i am child")
c=child()
c.outputc()
c.outputm()  
c.output()





class father():
    def output(self):
        print("i am father")
class child1(father):
    def outputc(self):
        print("i am child1")
class child2(father):
    def output2(self):
        print("i am child2")
c1=child1()
c2=child2()
c1.outputc()
c1.output() 
c2.output2()
c2.output()




class parent():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a,self.b)
s=parent(3,4)
s.add()
    
