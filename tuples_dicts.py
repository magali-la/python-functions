# script going through months using tuples
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# print first and last of the month
print(months[0])
print(months[-1])

# attempt to overwrite an index, set an error since it's immutable rename the error so it doesn't print the whole class
try:
    months[0] = "NewMonth"
except TypeError as error:
    print(f"Tuples are immutable, error: {error}")


# students dictionary with names and grades
students = {
    "Bob": 75,
    "Tina": 96,
    "Grace": 82
}

# add a new student
students["Mary"] = 70

# print all students
print(students)

# update Bob, he improved his test score
students["Bob"] = 80

# loop to print each student and grade - need items so it reads through everything
for (student, grade) in students.items():
    print(f"{student}: {grade}")