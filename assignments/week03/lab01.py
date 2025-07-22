# Complete this program to classify people by age
#age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

age=int(input("Enter age:"))
if age<=12:
     print ('child')
elif age<=19:
    print('teenager')
elif age<=59:
    print('adult')
else:
    print('senior')
