import statistics  # Import built-in module to perform statistical calculations like mean (average).

# Define a function to determine the letter grade based on the numeric average score.
def letter_grade(grades_score):
    # Check if the score is 90 or above and assign letter grade 'A'.
    if grades_score >= 90:
        print("Your score for the class is currently an A")  # Immediate feedback to user.
        return "A"
    # Check if score is 80-89 and assign 'B'.
    elif grades_score >= 80:
        print("Your score for the class is currently a B")
        return "B"
    # Check if score is 70-79 and assign 'C'.
    elif grades_score >= 70:
        print("Your score for the class is currently a C")
        return "C"
    # Check if score is 60-69 and assign 'D'.
    elif grades_score >= 60:
        print("Your score for the class is currently a D")
        return "D"
    # If below 60, assign 'F'.
    else:
        print("Your score for the class is currently an F")
        return "F"

grades_dict = {}  # Initialize an empty dictionary to store each subject's average score.
subjects = []     # Initialize a list to hold the names of all subjects.

# Prompt the user to enter the number of classes they want to calculate grades for.
# Use a loop with exception handling to ensure a valid integer input.
while True:
    try:
        number_of_classes = int(input("How many classes are you trying to calculate your grade in? "))
        break  # Exit loop if input is valid.
    except ValueError:
        print("Please enter a valid number.")  # Prompt user again if input is invalid.

# Prompt user for how many assignments each class has, similarly validating input.
while True:
    try:
        num_assignments = int(input("How many assignments per class? "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Collect the names of all classes based on the number specified.
for i in range(number_of_classes):
    subject = input(f"Enter the name of class {i + 1}: ")
    subjects.append(subject)  # Add each subject name to the subjects list.

# For each subject, collect assignment scores from the user.
for subject in subjects:
    grades = []  # Temporary list to store scores for the current subject.
    print(f"\nEntering grades for {subject}:")  # Inform user which subject they are inputting grades for.

    # Keep asking for assignment scores until the number matches 'num_assignments'.
    while len(grades) < num_assignments:
        try:
            user_input = int(input(f"Enter the score for assignment {len(grades) + 1}: "))  # Dynamic assignment number.
            # Validate that the score is between 0 and 100.
            if 0 <= user_input <= 100:
                grades.append(user_input)  # Add valid score to the grades list.
            else:
                print("Please enter a number between 0 and 100.")  # Reject invalid range inputs.
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer inputs gracefully.

    # Calculate the average score for the current subject, rounded to two decimal places.
    grades_score = round(statistics.mean(grades), 2)
    print(f"Average score for {subject}: {grades_score}")  # Display the calculated average.

    # Store the average score in the dictionary with the subject as key.
    grades_dict[subject] = grades_score

    # Calculate and display the letter grade based on the average score.
    final_grade = letter_grade(grades_score)

# After processing all subjects, print a final summary of all subjects with their average scores and letter grades.
print("\nSummary of all subjects and grades:")
for subject, avg_score in grades_dict.items():
    final_grade = letter_grade(avg_score)  # Get letter grade for each subject.
    print(f"{subject}: Average Score: {round(avg_score, 2)} | Final Grade: {final_grade}")

# Write the summary of grades to a text file for persistent storage.
with open("grade_summary.txt", "w") as f:
    for subject, avg_score in grades_dict.items():
        final = letter_grade(avg_score)
        # Format and write each subject's average and letter grade to the file.
        f.write(f"{subject}: Average Score: {round(avg_score, 2)} | Final Grade: {final}\n")

print("Summary saved to grade_summary.txt")  # Inform the user that the summary has been saved.
  
