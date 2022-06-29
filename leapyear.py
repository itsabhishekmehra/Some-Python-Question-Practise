year = int(input("enter a year: "))
if (year/100==0 and year/4==0):
    print('its a leap year')
elif (year%4==0):
    print('Its a leap year')
elif (year%100==0):
    print('its a leap year')
else:
    print('its not a leap year')