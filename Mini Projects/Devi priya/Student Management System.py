class Student:
    def __init__(self, student_id, name, age,email,phone,course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email=email
        self.phone =phone
        self.course=course
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age},Email: {self.email},Phone: {self.phone},Course: {self.course}"

class Manage:
    def __init__(self):
        self.students = []
        self.read()
	#loading the student details into the list
    def read(self):
        try:
            with open('student_data.txt', 'r') as file:
                for line in file:
                    student_id, name,age,email,phone,course = line.strip().split(',')
                    self.students.append(Student(int(student_id),name,age,email,phone,course))
        except FileNotFoundError:
            pass
	#storing the student details into the file
    def store(self):
        with open('student_data.txt', 'w') as file:
            for student in self.students:
                file.write(f"{student.student_id},{student.name},{student.age},{student.email},{student.phone},{student.course}\n")
	#adding the student details into the list and then storing to to the file
    def add_student(self, student_id, name, age,email,phone,course):
    	if any(student.student_id == int(student_id) for student in self.students):
        	print(f"Student with ID {student_id} already exists. Please choose a different ID.")
    	else:
    		new_student = Student(student_id, name, age, email, phone, course)
    		self.students.append(new_student)
    		self.store()
    		print("Student added successfully.")
    	#Displayin the student records
    def display_students(self):
        for student in self.students:
            print(student)
	#searching a student record by ID
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
        #searching and displaying students who are in same course
    def search_students_by_course(self, course):
    	matching_students = {}
    	course = course.lower()

    	for student in self.students:
        	if course in student.course.lower():
            		matching_students[student.student_id] = {
                	'Name': student.name,
               	 'Age': student.age,
                	'Email': student.email,
                	'Phone': student.phone
            }
    	if matching_students:
        	print(f"Students in {course}:")
        	for student_id, student_info in matching_students.items():
            		print(f"ID: {student_id}, Name: {student_info['Name']}\n")
    	else:
        	print(f"No students found in {course}.")
        #updating student details	
    def update_student(self, student_id, name, age,email,phone,course):
        student = self.search_student(student_id)
        if student:
            student.name = name
            student.age = age
            self.store()
            print(f"Student with ID {student_id} updated.")
        else:
            print(f"Student with ID {student_id} not found.")
	#Deleting student records
    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            self.store()
            print(f"Student with ID {student_id} deleted.")
        else:
            print(f"Student with ID {student_id} not found.")

def main():
        manage=Manage()
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Search Students by course")
            print("5. Update Student")
            print("6. Delete Student")
            print("7.Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                email = input("Enter student email: ")
                phone = int(input("Enter student phone: "))
                course=input("Enter the course:")
                manage.add_student(int(student_id), name, age,email,phone,course)

            elif choice == '2':
                manage.display_students()

            elif choice == '3':
                student_id = input("Enter student ID to search: ")
                student = manage.search_student(int(student_id))
                if student:
                    print("Student found:")
                    print(student)
                else:
                    print(f"Student with ID {student_id} not found.")
            elif choice == '4':
            	course = input("Enter Course to search for students: ")
            	manage.search_students_by_course(course)
            elif choice == '5':
                student_id = input("Enter student ID to update: ")
                course=input("Enter the course:")
                name = input("Enter updated name: ")
                age = int(input("Enter updated age: "))
                email=input("Enter updated mailid")
                phone=int(input("Enter the updated mobile number"))
                manage.update_student(int(student_id), name, age,email,phone,course)

            elif choice == '6':
                student_id = input("Enter student ID to delete: ")
                manage.delete_student(int(student_id))

            elif choice == '7':
                manage.store()
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
     	main()

  
        
