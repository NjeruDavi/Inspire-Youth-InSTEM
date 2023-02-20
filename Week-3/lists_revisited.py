#!/usr/bin/env python3

my_favourite_fruits = ["mango" , "bananas" , "kiwi" , "pawpaw"]
for fruit in my_favourite_fruits :
    print(fruit)
#replacing items in a list by removal of the item number
print(len(my_favourite_fruits))
friends = ["Davi" , "Cehu" , "Lee" , "Miami"]
print(friends)
friends[0] = "Mary"
print(friends)
print("------------------------")
new_friends = friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)
new_friends.reverse()
print(new_friends)

