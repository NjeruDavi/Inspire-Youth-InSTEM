age = 16
gender = "male"
if (age < 18 ):
    print("You are still young")
else:
    print("You get an ID")    



#Compound/ Multiple conditions
if((age > 30) & (gender == "male")):
    print("You qualify for a loan")
else:
    print("No loan for you")


fav_colour = "grey"
age = 22
if(fav_colour == "grey") | (age <= 20):
    print("Happy birthday to you")
else:
    print("No birthday for you")     
   