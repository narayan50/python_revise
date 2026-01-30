# adding data to the existing set
#with add() method adding single element
#with update() method adding multiple elements
# sets are mutable

s1={"java","python","c++",}

s1.add("swift")
print("before adding single element:",s1)
print("after adding single element:",s1)

s1.update(["ruby","go","perl"])
print("before adding multiple elements:",s1)
print("after adding multiple elements:",s1)

# copying set data to another set
s5={49,23,23,4,3,6,5}
s8=s5.copy() # pyright: ignore[reportUndefinedVariable]
print("original set data:",s5)  
print("copied set data:",s5)

# removing elements from set
s1={"male ","female","trans","others"}
s1.remove("others")
print("original set data:",s1)
print("after removing element using remove() method:",s1)
s1.discard("trans")
print("after removing element using discard() method:",s1)

# removing random element from set using pop() method
s1.pop()
print("after removing random element using pop() method:",s1)

# clearing entire set using clear() method
s1.clear()
print("after clearing entire set using clear() method:",s1)

r