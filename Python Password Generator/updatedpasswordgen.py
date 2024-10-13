import random
regenpassword = ' '
updatelength = 0

print("Hello this program is intended to give you a randomely generated password!")

length = int(input('How many characters long should your password be?: '))
while length < 5:
    length = int(input('Not enough characters enter a number higher than 5: '))
    
    
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*?'


password = ' '
for x in range(length):
    password += random.choice(chars)

oglength = length
#finalpass = print('Your password: ' + password)

if length < 10:
        #password = ' '
        updatelength = int(input('Password could be stronger if character count is above 10 would you like to update? If so re-enter new number or enter same number!: '))
if updatelength == oglength:
     print(password)
else:
     for x in range(updatelength):
        password += random.choice(chars)

print('Your password: ' + password)

regenlength = updatelength
regen = str(input("Would you like to regenerate your password? If so please type yes. If no please type no: "))

if regen == "yes":
     regenpassword = ' '
     for x in range(regenlength):
          regenpassword += random.choice(chars)
     print("New password: " + regenpassword)
          
else:
     print("Your password: " + password)



     
