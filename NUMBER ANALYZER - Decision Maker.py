numb1 = int(input("Please enter an integer between 1 and 100"))
odd_even = numb1%2
print(odd_even)
if odd_even == 1 and numb1 < 60:
  print("Odd and less than 60")
elif numb1 >= 2:
  print("Even and less than 25")
elif numb1 > 25:
  print("Even and between 26 and 60 inclusive")
elif numb1 > 60:
  print("Even and greater than 60")
elif odd_even == 1 and numb1 > 60:
  print("Odd and greater than 60")
