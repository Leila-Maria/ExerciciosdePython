#3.2)Rewrite your pay program using try and except so that your program 
#handles non-numeric input gracefully by printing a message and exiting the program. 
#The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

#####################################################

try:
 hrs = raw_input("Enter Hours:")
 h = float(hrs)
 rate = raw_input("Enter Rate:")
 r = float(rate)
except:
 print "Error, please enter numeric input"
 
print h, r
if h <= 40 :
 pay = h * r
 else:
 pay = r * 40 + (r * 1.5 * (h - 40))
 print pay
