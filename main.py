print("""        WELCOME TO STUDENT MANAGEMENT SYSTEM     """)
import student
student_list=[]
def menu():
    while True:
        print("""Enter your choice (1-5):
                 1.Add Student Details
                 2.Display Student Details
                 3.Search Student Detail
                 4.Delete Student Detail
                 5.Exit""")
        choice=int(input("Enter: "))
        if choice==1:
            student.add_student(student_list)
        elif choice==2:
            student.stu_details(student_list)
        elif choice==3:
            student_id=input("Enter Student id to search: ")
            student.stu_search(student_list,student_id)
        elif choice==4:
            student_id=input("Enter Student id to delete: ")
            student.stu_delete(student_list,student_id)
        elif choice==5:
            break
        else:
            print("Invalid choice enter(1-5)")
menu()
    

