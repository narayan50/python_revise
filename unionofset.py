# union of two sets
s1={10,40,20,40,10,50}
s2={20,50,50,50,10}
# we can use union() method or '|' operator to perform union operation
print(s1)
print(s2)

print("using union() method:",s1.union(s2))
print("using '|' operator:",s1 | s2)

# intersection of two sets
s3={10,20,30,40,50}
s4={30,40,50,60,70}
# we can use intersection() method or '&' operator to perform intersection operation
print(s3)
print(s4)
print("using intersection() method;",s3.intersection(s4))
print("using  & opertaor :", s3& s4)

# difference method
print("difference method using - operator:",s3 - s4)
print("difference method using difference() method:",s3.difference(s4))