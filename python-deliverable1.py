def main():
    # Prompting user for their name
    name = input("Please enter your name: ")

    # Prompting user for number of holes
    num_holes = int(input("Would you like to play 3 or 6 holes? Enter 3 or 6: "))
    while num_holes not in [3, 6]:
        num_holes = int(input("Invalid input. Please enter 3 or 6: "))

    # Initialize total score and par
    total_score = 0
    course_par = num_holes * 3

    # Loop to get scores for each hole
    for i in range(1, num_holes + 1):
        score = int(input(f"Enter the number of putts for hole {i}: "))
        total_score += score

    # Calculate score relative to par
    score_difference = total_score - course_par

    # Output message based on score difference
    if score_difference > 0:
        print(f"Nice try, {name}... Your total score was: +{score_difference}.")
    elif score_difference < 0:
        print(f"Great job, {name}! Your total score was: {score_difference}.")
    else:
        print(f"Good game, {name}. Your total score was: 0.")

if __name__ == "__main__":
    main()
