"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)


"""
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("pasu", 19, "korat", "thai")
    hobbies = []

    while True:
        print("\nMenu:")
        print("1. Show personal info")
        print("2. Add a hobby")
        print("3. Remove last hobby")
        print("4. Update age")
        print("5. Exit")
        
        choice = input("Please choose (1-5): ")

        if choice == '1':
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies)

        elif choice == '2':
            hobby = input("What is your new hobby? ")
            hobbies.append(hobby)
            print("Hobby added.")

        elif choice == '3':
            if hobbies:
                removed = hobbies.pop()
                print(f"Removed hobby: {removed}")
            else:
                print("No hobbies to remove.")

        elif choice == '4':
            person_list = list(person)
            age = input("How old are you? ")
            if age.isdigit():
                person_list[1] = int(age)
                person = tuple(person_list)
                print("Age updated.")
            else:
                print("Invalid age. Please enter a number.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    personal_info_manager()

