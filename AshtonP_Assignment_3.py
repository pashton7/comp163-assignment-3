# Initial test case initializing variables
student_name = "Ashton"
current_gpa = 3.7
study_hours = 30
social_points = 40
stress_level = 20

print(f"Hello {student_name}, your GPA is {current_gpa}, your study hours are {study_hours}, you have {social_points} social points, and your stress level is {stress_level}")

# First set of conditionals determining work load
print("Choose your course load:")
print("A) Light (12 Credits)\nB) Standard (15 credits)\nC) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if stress_level > 50 and current_gpa < 3.0:
        if study_hours > 45:
            print("Unusually high course load!")
        else:
            print("Put more time into studying and regulate stress")
    elif current_gpa < 3.0:
        print("Spend more time studying")
    else:
        print("Keep up the good work")
elif choice == "B":
    if stress_level > 60 and current_gpa < 2.6 and study_hours < 50:
        print("Put more time into studying")
    elif current_gpa > 3.5 and stress_level > 70 and study_hours > 50:
        print("Spend a little less time studying to help with stress levels")
    elif current_gpa < 3.0:
        print("Spend more time studying")
    else:
        print("Keep up the good work!")
elif choice == "C":
    if study_hours < 58 and  current_gpa < 3.0:
        print("Spend more time studying")
    elif study_hours > 58 and current_gpa >= 3.0 and stress_level >= 75:
        print("Take a break from studying to reduce stress")
    elif current_gpa < 2.8:
        print("Spend more time studying")
    else:
        print("Amazing work!")
else:
    print("Given input is invalid! Please try again.")