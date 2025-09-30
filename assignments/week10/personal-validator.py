"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""


#name="pasu peryruthai"
#age= 25
#phone = "0918156782"


print('=== PERSONAL INFORMATION VALIDATOR ===')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
phone = input('Enter your phone number: ')

#name validation ตรวจสอบชื่อ
nameFlag = True
for i in name:
    if not (i.isalpha() or i == ' '):
        nameFlag = False
        break

# Validate age ตรวจอายุ
ageflag = True
if age < 18 or age > 65:
    ageflag = False

# Validate phone ตรวจโทรสับ
phoneflag = True
if len(phone) != 10:
    phoneflag = False
else:
    for char in phone:
        if not char.isdigit():
            phoneflag = False
            break

# Show Validation Results
print('\nValidation Results:')
if nameFlag:
    print('Name: Valid (contains only letters and spaces)')
else:
    print('Name: Invalid')

if ageflag:
    print('Age: Valid (%d years old)' % age)
else:
    print('Age: Invalid (Must be between 18 and 65)')

if phoneflag:
    print('Phone: Valid (10-digit number)')
else:
    print('Phone: Invalid (Must contain exactly 10 digits)')

# Show Formatted Output
print('\nFormatted Information:')
print('Name: %s' % name.upper())

if 18 <= age <= 30:
    print('Age Group: Young Adult (18-30)')
elif 31 <= age <= 50:
    print('Age Group: Middle Aged (31-50)')
else:
    print('Age Group: Senior (51-65)')

print('Phone: +91-%s' % phone)





