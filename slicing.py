str ="fortune cloud"

print(str[0:5],str[:5])

print(str[8:],str[8:])


# reverse str
str2 ="Hello world"

print(str2[::-3])


# string mutability test

str9= "fortune cloud"

print("k"+str9[0:3]+"l"+str[3:])
print("str9 remain same even after concatination" , str9)

# by assigning it to new variable it is possiblr]e

new="k"+str9[0:3]+"l"+str[3:]

print("by asssigning str9 to new variable", new)

# opertions on string

str6 ="fortune cloud"

print("the lenght of str6 is :", len(str6))
print("now it converted into upper case :" ,str6.upper())
print("now it converted into lower case :" ,str6.lower())


# how to remove unncersssary space from string 

var0= "   fortune cloud    "
print("space removed", var0.strip())

# replace
var9= " Learing python is fun with fortune cloud "
print(var9)
print("replace : the word" , var9.replace("fun","amazing"))

# format dtring
a= "Narayan"
b=9888828232

print(f"My name is {a} and my phone number is {b}")

# .format function

var4= "I am {} and my phone is {}".format(a,b)

print(var4)



