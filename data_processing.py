# script to get average grades using tuples

# helper function
def get_average_grade(grade_tuple):
    # get the length first
    length = len(grade_tuple)

    try:
        # loop through the tuple and multiply it
        total_sum = sum(grade_tuple)
        
        return total_sum / length

    # this one is for the division by 0, if num2 == 0
    except ZeroDivisionError:
        print("You can't divide by 0. Add grades first.")
        return None
    
# expty input
# get_average_grade(())

# real input
print(get_average_grade((70, 83, 58, 93, 100)))

# dictionary with class averages per subject
class_grades = {
    "Math": (68, 92, 75, 80),
    "History": (86, 60, 73, 98),
    "Gym": (85, 92, 90, 100),
    "Art": ()
}

# loop through and print averages with an except block for empty input
for subject, tuples in class_grades.items():
    # use helper function to get the average
    avg = get_average_grade(tuples)

    # the helper returns None, so use this for empty tuples
    if avg == None:
        print(f"{subject} has no grades currently.") 
    else:
        print(f"The average grade for {subject} is {avg}")