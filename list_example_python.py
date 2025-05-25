# Creating a dictionary with student information
student = {
    "first_name": "George",
    "last_name": "Papadopoulos",
    "age": 21,
    "courses": ["Mathematics", "Programming", "Physics"]
}

# Displaying student information
print("Student Information:")
print("First Name:", student["first_name"])
print("Last Name:", student["last_name"])
print("Age:", student["age"])
print("Courses:")
for course in student["courses"]:
    print("-", course)

# Adding a new field
student["grade_average"] = 8.5

print("\nNew Field - Grade Average:", student["grade_average"])
