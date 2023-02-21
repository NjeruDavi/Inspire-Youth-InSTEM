#create an empty list
#using for loop add 5 new musicians
#copy to a new list called celebs
#sort the list
#pop out your favourite musicians
#count the number of remaining
favourite_musicians = []
for musician in range (5):
    y = input("Enter the name of musicians :")
    favourite_musicians.append(y)
print(favourite_musicians) 
celebs = favourite_musicians.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop(3)
print(celebs)
print(len(celebs))
