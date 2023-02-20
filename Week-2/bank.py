# if you are earning ranging btwn 100k- 150k
 

 #19% tax income btwn 150k - 300k
 #30% tax income above 300k
 #5% tax income less than 100k
 #print gross income and net income
gross_income = int(input("Enter your income:"))
if(gross_income <= 100000):
    net =  gross_income - (gross_income *0.05)
elif((gross_income > 100000)& (gross_income <= 150000)):
    net = gross_income - (gross_income *0.16)
elif((gross_income > 150000)&(gross_income <= 300000)):
    net = gross_income - (gross_income*0.19 )   
elif(gross_income > 300000):
    net =  gross_income - (gross_income *0.30)
print(gross_income)
print(net)  



  
