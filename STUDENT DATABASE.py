print("Welcome! which student would you like to learn more about? Enter a number 1-3:")

name_values = {"Sophia Petrillo": 1, "Rose Nylund": 2, "Blanche Devereaux": 3}
hometown_values = {"Sicily": 1,  "Atlanta": 2, "Oregon": 3}
favorite_food_values = {"cupcakes": 1, "chicken": 2, "pasta": 3}

max_number = len(name_values)
student_number = int(input("Enter a number 1-3: "))
if student_number < 1 or student_number > max_number:
    print("Number is out of range! Please enter a number only between 1-3.")
else:
    category = input("What information category would you like to display? Enter 'Hometown' or 'Favorite Food': ").capitalize()
    if category not in ['Hometown', 'Favorite Food']:
        print("Invalid category! Please enter either 'Hometown' or 'Favorite Food'.")
