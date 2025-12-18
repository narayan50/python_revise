# importing partial modules 

# limited function

from moduletest import add ,multi

no1=int(input("enter first number:----"))
no2=int(input("enter second number:---"))

print(add(no1,no2))
print(multi(no1,no2))
# following code won't work due to limited acesss 

# print(div(no1,no2))
# print(sub(no1,no2))

# ---------------------------------------------------

#  importing all methods
from moduletest import *
from foreignmodule.squarenmodule import square


no1=int(input("enter first number:----"))
no2=int(input("enter second number:---"))


print("addtion of two number:-----",add(no1,no2))
print("multiplocation of two number:-----",multi(no1,no2))

print("division of two number:-----",div(no1,no2))
print("substraction of two number:-----",sub(no1,no2))

print(square(no1,no2))

# importing foreign file in local modules




