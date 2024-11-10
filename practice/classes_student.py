'''
In main.py define the Student class that has two attributes: name and gpa

Implement the following instance methods:

A constructor that sets name to "Louie" and gpa to 1.0
set_name(self, name) - set student's name to parameter name
get_name(self) - return student's name
set_gpa(self, gpa) - set student's gpa to parameter gpa
get_gpa(self) - return student's gpa
Ex. If a new Student object is created, the default output is:

Louie/1.0
Ex. If the student's name is set to "Felix" and the gpa is set to 3.7, the output becomes:

Felix/3.7
'''

class Student:
    # Type your code here

    if __name__ == "__main__":
        initial_student = Student()
        print(initial_student.get_name(),'/', initial_student.get_gpa())

        initial_student.set_name('Felix')
        initial_student.set_gpa(3.7)
        print(initial_student.get_name(), '/', initial_student.get_gpa())