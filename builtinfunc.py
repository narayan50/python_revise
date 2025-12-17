# abs

i=- 12

print("Negative value converted into positive:-------",abs(i))

j=90.232

print(abs(j))

k=-12.2320000

print("Floating Negative value converted into positive:----",(abs(k)))

# bin

x=23

print(bin(x))

# bool

print(bool(9098))
print(bool(0))


# bytes string to bytes

string1 = "hello how are u"
print(bytes(string1, 'utf-8'))


# collable() -- it will check the value pass to it callable ot not 
print(callable(42))        
print(callable("hello"))



# sum 
numbers=[12,3,4,5,67,]
print("sum of numbers using sum()", sum(numbers))
# any
print(any([False, True, False])) 
print(any([False, False]))    

li=[23,3,3,43,"hello", 8923,"python"]
li2 = [0, "", False]  

print("any()---------",any(li))
print("any()------here the list totally empty:---",any(li2))

# ascii

# 1. A string with a "fancy" characte
word = "café"

# 2. Normal print shows the accent
print(word)        # Output: café

# 3. ascii() replaces the accent with a "safe code"
print(ascii(word))  # Output: 'caf\xe9'

# float

# convert integer values into the float
q=988

print(float(q))


# min()

# print minimum value

r=[23,34,3,5,56,56,7,6,87]

print(min(r))


# sort

# it will sort the value into ascending orders
li = [3, 1, 2]
print(sorted(li)) 

# zip 

# combine two value together like zip

names = ["Alice", "Bob"]
scores = [85, 90]
combined = list(zip(names, scores)) 
print(combined)

