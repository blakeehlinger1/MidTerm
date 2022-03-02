'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''
from atexit import register
import CourseClass as C 


def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']

    course = C.Course(name,crn,seats,status)
    
    
    for student in students:
       if course.get_status() == "closed":
          register = C.Register(student,crn)

          #print("Sorry joane, Registration is closed for MIS 4322 - Advanced Pyton")
          print("Sorry "+ register.get_name() + ", registration is closed for MIS 4322 - Advanced Python")
          print()
       else:
         register = C.Register(student,crn)
       #f status == "Closed":
          #print("Sorry joane, Registration is closed for MIS 4322 - Advanced Pyton")
      #print("Student Name:", students[0])
         course.update_seat_count()

         print("Student Name:", register.get_name())
         print("Course Name:", course.get_name())
         print("CRN:", course.get_crn())
         print("Seats left:", course.get_seats())
         print()
         print()
      
       #course.update_seat_count()


    
main()



        
    
    
