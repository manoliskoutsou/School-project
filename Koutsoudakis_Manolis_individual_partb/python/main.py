import students
import courses
import trainers
import assignments
import student_per_course
import trainer_per_course
import assignment_per_student_per_course
import datetime

def menu():
    print("WELCOME TO PRIVATE SCHOOL")

menu()

while True:
    try : 
        print("1.Students")
        print("2.Courses")
        print("3.Trainers")
        print("4.Assignments")
        print("5.Student per course")
        print("6.Trainer per course")
        print("7.Assignment per student per course")
        print("8.Exit")
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
                print("1.Insert Student")
                print("2.Update Student")
                print("3.Select Students")
                print("4.Delete Student")
                print("5.Main Menu")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    firstName = input("Enter Firstname : ")
                    lastName = input("Enter Lastname : ")
                    dateOfBirth = datetime.date(int(input("Enter year of birth: ")),int(input("Enter month of birth: ")),int(input("Enter day of birth: ")))
                    tuitionFees = float(input("Enter Fees : "))
                    students.insert_student(firstName, lastName, dateOfBirth, tuitionFees)
                elif choice == 2:
                    stid = int(input("Enter The Id : "))
                    firstName = input("Enter Firstname : ")
                    lastName = input("Enter Lastname : ")
                    dateOfBirth = datetime.date(int(input("Enter year of birth: ")),int(input("Enter month of birth: ")),int(input("Enter day of birth: ")))
                    tuitionFees = float(input("Enter Fees : "))
                    students.update_student(firstName, lastName, dateOfBirth, tuitionFees, stid)
                elif choice == 3:
                    students.select_students()
                elif choice == 4:
                    stid = int(input("Enter The Id To Delete :"))
                    students.delete_student(stid)
                else :
                    print(menu())
        elif choice == 2:
                print("1.Insert Course")
                print("2.Update Course")
                print("3.Select Courses")
                print("4.Delete Course")
                print("5.Main Menu")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    title = input("Enter Title : ")
                    stream1 = input("Enter Stream : ")
                    print("Enter Type : \n1 - Full Time \n2 - Part Time")
                    type1 = int(input()) 
                    if type1 == 1:
                        type1 = "Full time"
                    elif type1 == 2:
                        type1 = "Part time"
                    else :
                        print("No valid integer! Please try again")
                        continue
                    start_date = datetime.date(int(input("Enter year of start day: ")),int(input("Enter month of start day: ")),int(input("Enter day of start day: ")))
                    end_date = datetime.date(int(input("Enter year of end day: ")),int(input("Enter month of end day: ")),int(input("Enter day of end day: ")))
                    courses.insert_course(title, stream1, type1, start_date, end_date)
                elif choice == 2:
                    cid = int(input("Enter The Id : "))
                    title = input("Enter Title : ")
                    stream1 = input("Enter Stream : ")
                    print("Enter Type : \n1 - Full Time \n2 - Part Time")
                    type1 = int(input()) 
                    if type1 == 1:
                        type1 = "Full time"
                    elif type1 == 2:
                        type1 = "Part time"
                    else:
                        print("No valid integer! Please try again")
                        continue
                    start_date = datetime.date(int(input("Enter year of start day: ")),int(input("Enter month of start day: ")),int(input("Enter day of start day: ")))
                    end_date = datetime.date(int(input("Enter year of end day: ")),int(input("Enter month of end day: ")),int(input("Enter day of end day: ")))
                    courses.update_course(title, stream1, type1, start_date, end_date, cid)
                elif choice == 3:
                    courses.select_courses()
                elif choice == 4:
                    cid = int(input("Enter The Id To Delete :"))
                    courses.delete_course(cid)
                else :
                    print(menu)
        elif choice == 3:
                print("1.Insert Trainer")
                print("2.Update Trainer")
                print("3.Select Trainers")
                print("4.Delete Trainer")
                print("5.Main Menu")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    firstName = input("Enter Firstname : ")
                    lastName = input("Enter Lastname : ")
                    subject1 = input("Enter Subject : ")
                    trainers.insert_trainer(firstName, lastName, subject1)
                elif choice == 2:
                    trid = int(input("Enter The Id : "))
                    firstName = input("Enter Firstname : ")
                    lastName = input("Enter Lastname : ")
                    subject1 = input("Enter Subject : ")
                    trainers.update_trainer(firstName, lastName, subject1, trid)
                elif choice == 3:
                    trainers.select_trainers()
                elif choice == 4:
                    trid = int(input("Enter The Id To Delete :"))
                    trainers.delete_trainer(trid)
                else :
                    print(menu)
        elif choice == 4:
                print("1.Insert Assignment")
                print("2.Update Assignment")
                print("3.Select Assignments")
                print("4.Delete Assignment")
                print("5.Main Menu")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    title = input("Enter Title : ")
                    description1 = input("Enter Description : ")
                    subDateTime = datetime.date(int(input("Enter year of sub date time: ")),int(input("Enter month of sub date time: ")),int(input("Enter day of sub date time: ")))
                    oralMark = float(input("Enter Oral Mark : "))
                    if oralMark <= 10 and oralMark > 0 :
                        print(oralMark)
                    else :
                        print("No valid integer! Please try again")
                        continue
                    totalMark = float(input("Enter Total Mark : "))
                    if totalMark <= 10 and totalMark >= 0 :
                        print(totalMark)
                    else :
                        print("No valid integer! Please try again")
                        continue
                    assignments.insert_assignment(title, description1, subDateTime, oralMark, totalMark)
                elif choice == 2:
                    asid = int(input("Enter The Id : "))
                    title = input("Enter Title : ")
                    description1 = input("Enter Description : ")
                    subDateTime = datetime.date(int(input("Enter year of sub date time: ")),int(input("Enter month of sub date time: ")),int(input("Enter day of sub date time: ")))
                    oralMark = float(input("Enter Oral Mark : "))
                    if oralMark <= 10 and oralMark > 0 :
                        print(oralMark)
                    else :
                        print("No valid integer! Please try again")
                        continue
                    totalMark = float(input("Enter Total Mark : "))
                    if totalMark <= 10 and totalMark >= 0 :
                        print(totalMark)
                    else :
                        print("No valid integer! Please try again")
                        continue
                    assignments.update_assignment(title, description1, subDateTime, oralMark, totalMark, asid)
                elif choice == 3:
                    assignments.select_assignments()
                elif choice == 4:
                    asid = int(input("Enter The Id To Delete :"))
                    assignments.delete_assignment(asid)
                else :
                    print(menu)
        elif choice == 5:
            print("1.Insert Student Per Course")
            print("2.Update Student Per Course")
            print("3.Select Student Per Course")
            print("4.Delete Student Per Course")
            print("5.Main Menu")
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                stid = int(input("Enter Student Id : "))
                cid = int(input("Enter Course Id : "))
                student_per_course.insert_student_per_course(stid, cid)
            elif choice == 2:
                st_per_c_id = int(input("Enter Student Per Course Id : "))
                stid = int(input("Enter Student Id : "))
                cid = int(input("Enter Course Id : "))
                student_per_course.update_student_per_course(stid, cid)
            elif choice == 3:
                student_per_course.select_student_per_course()
            elif choice == 4:
                 st_per_c_id = int(input("Enter Student Per Course Id : ")) 
                 student_per_course.delete_student_per_course(st_per_c_id) 
            else :
                print(menu)        
        elif choice == 6:
            print("1.Insert Trainer Per Course")
            print("2.Update Trainer Per Course")
            print("3.Select Trainer Per Course")
            print("4.Delete Trainer Per Course")
            print("5.Main Menu")
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                trid = int(input("Enter Trainer Id : "))
                cid = int(input("Enter Course Id : "))
                trainer_per_course.insert_trainer_per_course(trid, cid)
            elif choice == 2:
                tr_per_c_id = int(input("Enter Trainser Per Course Id : "))
                trid = int(input("Enter Trainer Id : "))
                cid = int(input("Enter Course Id : "))
                trainer_per_course.update_trainer_per_course(trid, cid, tr_per_c_id)  
            elif choice == 3:
                trainer_per_course.select_trainer_per_course()
            elif choice == 4:
                tr_per_c_id = int(input("Enter Trainser Per Course Id : "))
                trainer_per_course.delete_trainer_per_course(tr_per_c_id)
            else :
                print(menu)    
        elif choice == 7:
            print("1.Insert Assignment Per Student Per Course")
            print("2.Update Assignment Per Student Per Course")
            print("3.Select Assignment Per Student Per Course")
            print("4.Delete Assignment Per Student Per Course")
            print("5.Main Menu")
            choice = int(input("Enter Your Choice : "))
            if choice == 1 :
                asid = int(input("Enter Assignment Id : ")) 
                stid = int(input("Enter Student Id : ")) 
                cid = int(input("Enter Course Id : "))
                assignment_per_student_per_course.insert_assignment_per_student_per_course(asid, stid, cid)
            elif choice == 2:
               as_per_st_per_c_id = int(input("Enter Assignment Per Student Per Course Id : "))
               asid = int(input("Enter Assignment Id : "))
               stid = int(input("Enter Student Id : "))
               cid = int(input("Enter Course Id : ")) 
               assignment_per_student_per_course.update_assignment_per_student_per_course(asid, stid, cid, as_per_st_per_c_id)
            elif choice == 3:
                assignment_per_student_per_course.select_assignment_per_student_per_course()
            elif choice == 4:
                as_per_st_per_c_id = int(input("Enter Assignment Per Student Per Course Id : "))
                assignment_per_student_per_course.delete_assignment_per_student_per_course(as_per_st_per_c_id)
            else :  
                print(menu)           
        elif choice == 8:
            exit()
        else :
            print("Invalid Selection! Please Try Again!")
    except ValueError :
        print("No valid integer! Please try again")