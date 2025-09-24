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
course_load = ""
if choice == "A":
    if  current_gpa >= 3.0 and study_hours < 25:
        course_load = "Light"
    elif study_hours > 30 and stress_level >= 35:
        course_load = "Medium"
    elif study_hours > 30:
        course_load = "Heavy"
    else:
        course_load = "Light"
elif choice == "B":
    if current_gpa >= 3.2 and study_hours <= 25:
        course_load = "Light"
    elif current_gpa <= 3.0 or study_hours > 40:
        course_load = "Heavy"
    elif current_gpa >= 2.8 and study_hours < 40:
        course_load = "Medium"
    else:
        course_load = "Medium"
elif choice == "C":
    if current_gpa >= 3.0 and study_hours <= 50:
        course_load = "Medium"
    elif study_hours > 50 and current_gpa < 3.0:
        course_load = "Heavy"
    elif study_hours <= 50 and current_gpa > 3.0:
        course_load = "Light"
    else:
        course_load = "Heavy"
else:
    print("Given input is invalid! Please try again.")

print(f"According to your data your actual course load is: {course_load}")

study_options = ["Programming", "Math", "English", "History"]
select_class = input(f"Select the class you perform the best in from the list {study_options}: ")
focus = ""
if select_class in study_options:
    if social_points < 55 and current_gpa >= 3.0:
        focus = "Social"
    elif social_points >= 60 and current_gpa < 2.8:
        focus = "Study"
    elif stress_level > 50 and social_points < 60:
        focus = "Social"
    elif social_points < 50:
        focus = "Social"
    else:
        focus = "Study"
elif select_class not in study_options:
    print(f"{select_class} is not a valid option!")
summary = ""
if course_load == "Light":
    if focus == "Study":
        if stress_level >= 60:
            summary ="To reduce stress you should socialize a little more but still focus on studying."
    elif focus == "Study":
        summary = "You should focus on studying"
    elif focus == "Social":
        summary = "You should take a break from studying and socialize"
elif course_load == "Medium":
    if focus == "Study":
        if stress_level >= 70:
            summary = "Take a break between study sessions to socialize!"
    elif focus == "Study":
        summary = "You should study"
    elif focus == "Social":
        summary = "You should spend more time socializing"
elif course_load == "Heavy":
    if focus == "Study":
        if stress_level >= 70 and social_points < 45:
            summary = "You should take a break from studying and socialize."
        else:
            summary = "With your work load you should spend more time studying."
    elif focus == "Social":
        summary = "You should take a break from your heavy work load and study."

print("=== YOUR FINAL STATS ===")
print(f"Name: {student_name}")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level (0-100): {stress_level}")
print(f"Your best class: {select_class}")
print(f"Your calculated course load: {course_load}")
print(f"Your summary: {summary}")