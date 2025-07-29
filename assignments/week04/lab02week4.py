"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
 
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input("Insert number [" + str(i+1) + "]: "))
        numbers.append(number)
    
    
    print(f"\nOriginal numbers: {numbers}")
    even_numbers = []
    odd_numbers = []
    
    average = sum(numbers) / len(numbers)
    
    above_average = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        if num > average:
            above_average.append(num)
    
    print("Even number list:", even_numbers)
    print("Odd number list:", odd_numbers)
    print("Above average numbers:", above_average)
    print("Average:", average)
    print("Min:", min(numbers))
    print("Max:", max(numbers))

if __name__ == "__main__":
    number_operations()
