f=open("./simple.txt")
c=[]
for i in f:
    c.append(i.split(" "))
print(c)
d=0
for i in range(len(c)):
    d=d+i
print(d)
