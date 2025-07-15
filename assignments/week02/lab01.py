weight=float(input("weight: "))
height=float(input("height: "))
bmi=weight/height **2
if bmi<18.5:
    print('underweight')
    if bmi >= 18.5 and bmi<= 24.9:
        print('normal weight')
        if bmi >= 25.0 and bmi <=29.9:
            print('overweight')
            if bmi  >= 30.0:
                print('obese')
print('your bmi is',bmi)
