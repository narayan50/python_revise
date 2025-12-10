s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("Set 1:", s1)
print("Set 2:", s2)
print("symmetric differnce s1 s2 :" ,s1.symmetric_difference(s2))
s1.intersection_update(s2)
print(s1) # s1 now contains only elements also in s2

s3={1,2,3}
s4={2,3}
print("Set 3:", s3)
print("Set 4:", s4)
s3.difference_update(s4)
print(s3) # s3 now contains only elements not in s4

# printing sqaure of elements of a set
s5={1,2,3,4,5}
squared_set={x**2 for x in s5}
print("Squared Set:", squared_set)

# printing cube of elements of a set
s5={1,2,3,4,5}
squared_set={x**3 for x in s5}
print("Squared Set:", squared_set)