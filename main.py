import csv
import os
file_name = "students.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone", "Department"])


print("==============================")
print(" STUDENT ONBOARDING SYSTEM")
print("==============================")

print("1. Student Registration")
print("2. View Student Details")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")

choice = input("Enter your choice: ")

if choice == "1":

    print()
    print("----- Student Registration -----")

    name = input("Enter student name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    department = input("Enter department: ")

    if name == "":
        print("Name cannot be empty.")

    elif "@" not in email:
        print("Invalid email.")

    elif not phone.isdigit() or len(phone) != 10:
        print("Phone number must contain 10 digits.")

    elif department == "":
        print("Department cannot be empty.")

    else:
     with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            email,
            phone,
            department
        ])

    print()
    print("Registration Successful!")
    print("Student details saved successfully.")

elif choice == "2":

    print()
    print("----- Student Details -----")

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for student in reader:
            found = True

            print("----------------------")
            print("Name:", student["Name"])
            print("Email:", student["Email"])
            print("Phone:", student["Phone"])
            print("Department:", student["Department"])

        if not found:
            print("No students registered.")

elif choice == "3":

    print()
    print("----- Search Student -----")

    search_name = input("Enter student name: ")

    found = False

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:

            if student["Name"].lower() == search_name.lower():

                print()
                print("Student Found!")
                print("Name:", student["Name"])
                print("Email:", student["Email"])
                print("Phone:", student["Phone"])
                print("Department:", student["Department"])

                found = True
                break

    if not found:
        print("Student not found.")
elif choice == "4":

    print()
    print("----- Update Student -----")

    search_name = input("Enter student name: ")

    students = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:

            if student["Name"].lower() == search_name.lower():

                print("Student found.")

                new_department = input(
                    "Enter new department: "
                )

                if new_department == "":
                    print("Department cannot be empty.")
                    found = True
                    students.append(student)
                    continue

                student["Department"] = new_department
                found = True

            students.append(student)

    if found:

        with open(file_name, "w", newline="") as file:

            fieldnames = [
                "Name",
                "Email",
                "Phone",
                "Department"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student details updated successfully.")

    else:
        print("Student not found.")

elif choice == "5":

    print()
    print("----- Delete Student -----")

    search_name = input("Enter student name: ")

    students = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:

            if student["Name"].lower() == search_name.lower():
                found = True
            else:
                students.append(student)

    if found:

        with open(file_name, "w", newline="") as file:

            fieldnames = [
                "Name",
                "Email",
                "Phone",
                "Department"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully.")

    else:
        print("Student not found.")

elif choice == "6":
    print("Thank you for using the system.")

else:
    print("Invalid choice.")