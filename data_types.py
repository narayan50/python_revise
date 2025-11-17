var1=1 #int
var='string' #string
var3=90.9 #float

print(var1,var,var3)


# list
l1=[10 ,"hello, 90.3", True ,]
print (l1)
l2=[89,78,34,2,12,34,40]
print(l2)

# tuple
t1=(10 ,"hello, 90.3", True ,)
print (l1)
t2=(89,78,34,2,12,34,40)
print(l2)
print(type(t1),type(t2))
# sets 

s1={1,2,3,4,4,5}
s2=set([3,4,5,6])
print(s1)
print (s2)
print (type(s2))

# union
us=s1|s2
print(us)
# intersection
ints= s1&s2
print(ints)

# 
s5= s1-s2
print(s2)

# sets are mutabel by usinf frozenset we can make it immutable sets

fs1=frozenset(s1)
print(s1)

# dictionary 

dc1={'name':"Narayan",'age':25, 'gender':"male"}
print(dc1,type(dc1))

# range

r=range(10,90,3)
print(r) #henec it is dificult to print range direct you have to first convert it into list
print(list(r)) #converted
print(type(r))

# none tyoe
var9= None
print(var9,(type(var9)))
print(var9)