#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

#Exercicio 3.1

#######################################
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
pay = 40 * r
extra_pay = (h - 40) * r * 1.5
if h > 40:
    print pay + extra_pay
else:
    pay = h * r
