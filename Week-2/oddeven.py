#odd numbers & even numbers
for odd_numbers in range(1,100):
    if(odd_numbers%2 != 0):
      print(odd_numbers)
print("--------------------------")     
for even_numbers in range (1,100):
    if(even_numbers%2 ==0):
      print(even_numbers) 
    
          #OR
for i in range(1,100):
  if(i%2 ==0):
    print(i," is even ")
  else:
    print(i,"is odd")  