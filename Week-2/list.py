#making a list
names = [ "David" , "Reezy" , " Prodigy" , "Nicole" , "Winnie"]
#Accessing components in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
fruits = [ "mango" , "banana","kiwi" ,"passion" , "guavas" , "pumpkin" , "lemon"]
print(fruits)
print(fruits[3])
print("My favourite fruit is :",(fruits[2]))
print("My favourite fruit is :",(fruits[2].upper()))
#Adding two lists
vegetables = ["kales", "spinach", "managu", "lettuce", "broccoli"]
stationary = ["pens" , "ink","books" , "glue","stapler"]
shoppings = vegetables + stationary
print(shoppings)
print(shoppings[5])
#for loop
for vegetable in vegetables :
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("My name is " + names[0]+ "  and my favourite fruit is " + fruits[1])
