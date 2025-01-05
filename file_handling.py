s=open('demo.txt',mode='r')
print(s.read())      #it will print data in demo.txt
s.close()




'''
s=open('demo.txt',mode='w')
s.write("welcome")        #it will truncate the before data and displays new data
s.close()'''





'''
s=open('demo.txt',mode='a')       #a=append
s.write("welcome")                #it will print before data and add this data
s.close()'''



'''s=open('demo.txt',mode='r+')
print(s.read())                 #it will print all the data
s.write("everyone")
s.close()'''



'''s=open('demo.txt',mode='w+')
s.write("hiii")               #it will truncate before data and only displays this hiii
print(s.read())
s.close()'''





s=open("demofile.txt","r")
print(s.read())
s.close()


s=open("demofile.txt","w")
s.write("\n i am going to learning exception handling also")
s.close()




s=open("demofile.txt","a")
s.write("\n append is used to add text to the text file")
s.close()




s=open("demofile.txt","r")
print(s.readline())
print(s.readline())

s.close()




s=open("demofile.txt","r")
data_read=s.read()
data=len(data_read)
print(data)
s.close()





