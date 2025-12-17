# rarely used arg where we need to pass values 
# with parameter name while calling the function
def posele(name , city):
    print(f"hello, {name}! {city}")
    print("hello", name, ":", city)
posele("Narayan", "pune")
posele(city="Mumbai", name="Narayan")