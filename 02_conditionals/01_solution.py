age = int(input('Enter age:'))

if(age < 13):
    print('child')
elif (age <= 19):
    print('teen')
elif (age <= 59):
    print('adult')
else: 
    print('senior')