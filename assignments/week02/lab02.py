Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used

direction = input('what is your conversiondirtion(1: thb to usd,2 usd to thb):')
amount=float(input('amount to convert:'))
if direction == "1":
    result = amount/35.5
    print('result:',result,"usd")
    if direction == "2":
        result = amount*35.5
        print('result:',result,"thb")

       