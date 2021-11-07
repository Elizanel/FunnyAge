# ask user for their age and print a greeting

year = int(input("Greetings! What is your year of origin?"))
if year <= 1900:
    print ("Woah, You are old!" ) 
elif year > 1900 and year < 2020:
    print ("I guess you are young!")
elif year > 2020:
    print ("Awesome, that's the future!!")
