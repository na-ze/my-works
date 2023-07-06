from colorama import init, Fore, Back, Style
init()

print(Back.GREEN + "Hi there, welcome to DMI calculation software!")
print(Back.CYAN)
weight = float(input("What's your weight?: "))
height = float(input("And what's your height?: "))
print("")

bmi = float("{0:.2f}".format(weight/ ((height / 100) * (height / 100))))

print(Back.RED + "Your current BMI is " + str(bmi))

if( bmi <= 16 ):
    print(Back.RED + "(High body mass deficit", end = ' ')
if( bmi >= 16 and bmi <= 18.5 ):
    print(Back.YELLOW + "(Insufficient body weight", end = ' ')
if( bmi >= 18.5 and bmi <= 25 ):
    print(Back.GREEN + "(Your weight is OK", end = ' ')
if( bmi >= 30 and bmi <= 35 ):
    print(Back.RED + "(Obesity of the 1 degree", end = ' ')
if( bmi >= 35 and bmi <= 40 ):
    print(Back.RED + "(Obesity of the 2 degree", end = ' ')
if( bmi > 40 ):
    print(Back.RED + "(Obesity of the 3 degree (morbid)", end = ' ')


    
    
    
    
    
