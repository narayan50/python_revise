# lambda function with single arguments

no = lambda a: a * a

print(no(67))


# lambda function with multple arguments

no1= lambda x,y: y+x

x=(input("enter the first value:---" ))
y=(input("enter the first value:---" ))



# connditional statements in lambda function
no3 = lambda s: "zero" if s == 0 else ("even" if s % 2 == 0 else "odd")



print(no3(23))

print(no3(34))

print(no3(89))

print(no3(40))

# passing multpile operation in lamda


cal= lambda o,p: (o+p ,o-p,o%p,o/p)
result=cal(98,23)
print(result)


# filterfunction in lambda

l1=[23,23,34,3,45,65,6,67,]

is_even= filter (lambda a: a%2==0 ,l1)

print(list(is_even))

# map in lambda

square=map(lambda a:a**a,l1)

print(list(square))