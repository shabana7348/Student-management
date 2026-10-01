def add_student(stu_list):
    name=input("Enter Student Name: ")
    stu_id=input("Enter student id: ")
    year=input("Enter Year of study: ")
    dept=input("Enter department name: ")
    stu_list.append([name,stu_id,year,dept])
def stu_details(stu_list):
    for stu in stu_list:
        print('Name: ',stu[0])
        print('Student ID: ',stu[1])
        print('Year: ',stu[2])
        print('Department: ',stu[3])
    if len(stu)==0:
        print("No Student details found")
def stu_search(stu_list,stu_id):
    for stu in stu_list:
        if stu[1]==stu_id:
            print(stu_id," details are found")
            print(stu[0], stu[2], stu[3])
            break
    else:
        print("Student details not found")
def stu_delete(stu_list,stu_id):
    for i in range(len(stu_list)):
        if stu_list[i][1]==stu_id:
            d=stu_list.pop(i)
            print(d," deleted successfully")
            break
    else:
        print("Student detail not found")
    
            
            
            
        
    
