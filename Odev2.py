personal_information = [] #empty list
f_name = input("Please enter your first name: ")
l_name = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
date_of_birth = int(input("Please enter your year of birth: "))

personal_information.append(f_name)
personal_information.append(l_name)
personal_information.append(age)
personal_information.append(date_of_birth)

len(personal_information)

i = 0 #counter value

while (i < len(personal_information)):
    print(personal_information[i])
    i+=1

if age < 18:
    print("You can't go out because it's too dangerous!")
else:
    print("You can go out to the street.")
