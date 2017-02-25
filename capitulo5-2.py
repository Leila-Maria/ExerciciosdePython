#Chapter 5 - exercicio 5.2
#Write another program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead
#of the average.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done

largest = None  
smallest = None  
  
while True:  
    num = raw_input("Enter a number: ")  
    if num == "done" : break  
          
    try:  
        n=int(num)  
  
    except:  
        print "Invalid input"  
              
    if n>largest:  
        largest=n  
    if smallest is None or n<smallest:  
        smallest=n
             
print "Maximum is", largest  
print "Minimum is", smallest  
