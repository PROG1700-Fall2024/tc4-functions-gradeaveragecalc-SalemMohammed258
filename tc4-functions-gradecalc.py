############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Salem Mohammed

# MAIN FUNCTION TO GATHER GRADES FOR SIX COURSES AND CALCULATE GPA
def main():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    totalGrade = 0.0
    course_count = 6

    # Gather grades for six courses
    for i in range(1, course_count + 1):
        print(f"\nEntering grade for course {i}:")
        while True:
            letterGrade = input("Please enter a letter grade : ").upper()
            modifier = input("Please enter a modifier (+, - or nothing) : ")
            
            # Calculate numeric grade and validate input
            numericGrade = calculate_numeric_grade(letterGrade, modifier)
            if numericGrade is not None:
                totalGrade += numericGrade
                print("The numeric value is: {0:.1f}".format(numericGrade))
                break
            else:
                print("Invalid input. Please try again.")

    # Calculate and print final GPA for all six courses
    finalGPA = totalGrade / course_count
    print("\nThe final GPA for six courses is: {0:.2f}".format(finalGPA))

# FUNCTION TO CALCULATE NUMERIC GRADE VALUE BASED ON LETTER AND MODIFIER
def calculate_numeric_grade(letterGrade, modifier):
    numericGrade = 0.0

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        # If an invalid entry is made
        print("You entered an invalid letter grade.")
        return None
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    # Ensure the calculated grade does not exceed 4.0
    return min(numericGrade, 4.0)

# PROGRAM EXECUTION STARTS HERE
main()