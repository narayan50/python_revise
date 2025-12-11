person={
    "Name":"ram",
    "age":34,
    "gender":"male",
     "city":"pune",
     "country":"india"
     
}
print(person)

for key in person:
    value=person[key]
    print(key,"->",value)

print(person.get("state","mumbai"))
print(person.get("state","pune"))


d1={"name":"naryan" , "gender": " male"}
d2={
    "city":"pune", "country":"india" 
}
print(d1)
print(d2)
d1.update(d2)
print("Updated value", d1)

print(d2.values())
print(d2.keys())



print(dict.fromkeys(['a', 'b', 'c'], 0))    