
count = 0

s_name = "Meserret"
s_surname = "Kabakci"

check = False

print("Simple Student Management System")
print("---------------------------------------------------------------")
print('Have a right to enter name and surname incorrectly three times!')
while count < 3:
    name1 = input("Please enter your name: ")
    surname1 = input("Please enter your surname: ")

    count = count + 1
    if name1 == s_name and surname1 == s_surname:
        break

    if name1 == s_name or surname1 == s_surname:
        print("Try again..")

    elif name1 != s_name or surname1 != s_surname:
        print("Try again..")

if name1 == s_name and surname1 == s_surname:
    print("\nWelcome " +s_name +" " +s_surname)

if name1 != s_name and surname1 != s_surname:
    print("Try again later!")

print("\n------------------Courses-------------------")
courses = []
for lesson in courses:
    print(courses)
print("Enter 5 courses.")
for i in range(5):
    course = input("\nPlease enter course: ")
    courses.append(course.capitalize())
print(courses)


def selectin_course():
    n = int(input("\nEnter the number of courses you will take: "))
    if n<3:
        return print("You failed this class!!")
    elif 3 <= n < 5:
        selected_course = [input("\nEnter course name: ") for i in range(n)]
        return print(selected_course)
    else:
        print("Invalid choice..")

selectin_course()

Math = {"Name":"Math","Midterm":58, "Final":62, "Project":49}
Physics = {"Name":"Physics", "Midterm":58, "Final":77, "Project":54}
Geometry = {"Name":"Geometry", "Midterm":75, "Final":88, "Project":90}
Geology = {"Name":"Geology","Midterm":95, "Final":93, "Project":100}
Chemistry = {"Name":"Chemistry","Midterm":73, "Final":55, "Project":68}


student_courses = [Math, Physics, Geometry, Geology, Chemistry]


def get_average(student_courses):
    midterm = student_courses["Midterm"]
    final = student_courses["Final"]
    project = student_courses["Project"]
    return (0.3*midterm + 0.2*project + 0.5*final)

def assign_letter(score):
    if score >= 90:
        return "AA"
    elif 70 < score < 90:
        return "BB"
    elif 50 < score < 70:
        return "CC"
    elif score < 50:
        print("You failed!")
        return "FF"

ch = input("\nChoose one course from list: ")
ch = ch.capitalize()
if ch == "Math":
    Math = {"Name":"Math" , "Midterm":58, "Final":62, "Project":49}
    print("---------------------------------------------------------")
    print("Grade of Math is: ", get_average(Math))
    print("Letter grade of Math is:  ", assign_letter(get_average(Math)))
elif ch == "Physics":
    Physics = {"Name":"Physics", "Midterm":58, "Final":77, "Project":54}
    print("---------------------------------------------------------")
    print("Grade of Physics is:  " , get_average(Physics))
    print("Letter grade of Physics is:  " ,  assign_letter(get_average(Physics)))
elif ch == "Geometry":
    Geometry = {"Name":"Geometry", "Midterm":75, "Final":88, "Project":90}
    print("---------------------------------------------------------")
    print("Grade of Geometry is: " , get_average(Geometry))
    print("Letter grade of Geometry is: ", assign_letter(get_average(Geometry)))
elif ch == "Geology":
    Geology = {"Name":"Geology", "Midterm":95, "Final":93, "Project":100}
    print("---------------------------------------------------------")
    print("Grade of Geology is: " , get_average(Geology))
    print("Letter grade of Geology is: ", assign_letter(get_average(Geology)))
elif ch == "Chemistry":
    Chemistry = {"Name":"Chemistry" ,"Midterm":73, "Final":65, "Project":68}
    print("---------------------------------------------------------")
    print("Grade of Chemistry is: " , get_average(Chemistry))
    print("Letter grade of Chemistry is: ", assign_letter(get_average(Chemistry)))
else:
    print("Invalid choice of course..")


