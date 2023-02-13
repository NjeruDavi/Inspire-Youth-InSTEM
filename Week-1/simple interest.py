#write a program to calculate simple interest
P = input("Enter the principle amount :")
R = input("Enter the rate :")
T = input("Enter the time duration :")
simple_interest = (int(P) * int(R) * int(T)) / 100
print("The simple interest is :",simple_interest)
#Write a program that calculate the surface area of a sphere
Pi = 3.142
r = input("Enter the radius of the sphere :")
surfacearea=(4*Pi*int(r)*int(r))
print(surfacearea)
#write a program that calculate the surface area of a cylinder
Pi = 3.142
r = input(" Enter the radius of the cylinder :")
h = input("Enter the hieght of the cylinder:")
surfacearea=(2 * Pi * int(r) * int(r) + Pi * 2  * int(r) * int(h))
print(surfacearea)
#Calculate the volume of a sphere
Pi = 3.142
r = input("Enter the radius of a spher:")
volume=(4/3 * Pi * int(r) * int(r) * int(r) )
print(volume)
