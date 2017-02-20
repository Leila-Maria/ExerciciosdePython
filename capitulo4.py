#Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 

#The function should return a value. 

#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 

#You should use raw_input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.


def computepay(h,r):  
      
    if h<=40:  
        return h*r  
    else:  
        return 40*r+(h-40)*r*1.5  
  
hrs = raw_input("Enter Hours:")  
rate = raw_input("Enter Rate:")  
  
hr = float(hrs)  
ra = float(rate)  
  
pay = computepay(hr,ra)  
  
print pay
