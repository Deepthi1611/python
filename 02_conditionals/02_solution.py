age = int(input('Enter age:'))
day = input('Enter day:')

# short hand notation for if else
price = 12 if(age >= 18) else 8

if(day.lower() == 'wednesday'):
    price = price-2 

print(price)