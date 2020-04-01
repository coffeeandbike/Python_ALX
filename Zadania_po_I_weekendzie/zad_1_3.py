'''
### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
​
Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach.
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
'''

bmi_low = """your BMI is too low, 
risk of developing problems such as nutritional deficiency and osteoporosis is very high"""

bmi_good = "Your BMI is in the healthy range, keep healthy diet and do sports every day for keeping health"

bmi_higher = """Your BMI is quite higher than should be.
You havem moderate risk of developing heart disease, high blood pressure, stroke, diabetes
Please start healthy nutrition and contact with the doctor """

bmi_very_high = """Your BMI is too high !!!!
You have a high risk of developing heart disease, high blood pressure, stroke, diabetes
PLEASE buck up ASAP if you don't want to eat the roots from the bottom :) """

while True:
    header = "BMI calculator"
    print(f'{header:_^30}')

    weight = float(input('Please enter your weight in kg: '))
    print()
    height = int(input('Please enter your height in cm: '))
    height_2 = height / 100

    bmi = weight / (height_2 ** 2)

    print(f'Your BMI is {bmi:.2f}')

    if bmi < 18.5:
        print(bmi_low)
        break
    elif 18.5 <= bmi < 23:
        print(bmi_good)
        break
    elif 23 <= bmi < 27:
        print(bmi_higher)
        break
    elif bmi >= 27:
        print(bmi_very_high)
        break
    else:
        print("You entered an invalid data")
        continue
