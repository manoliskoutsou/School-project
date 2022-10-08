import mysql.connector
import config

def insert_assignment_per_student_per_course(asid, stid, cid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into assignment_per_student_per_course (asid, stid, cid) values (%s, %s, %s);"
        assignment_per_student_per_course = (asid, stid, cid)
        myCursor.execute(sql, assignment_per_student_per_course)
        conn.commit()
        print("Data Inserted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

def update_assignment_per_student_per_course(asid, stid, cid, as_per_st_per_c_id):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = ("update student_per_course set asid = %s, stid = %s, cid = %s where as_per_st_per_c_id = %s;")
        assignment_per_student_per_course = (asid, stid, cid, as_per_st_per_c_id)
        myCursor.execute(sql,assignment_per_student_per_course)
        conn.commit()
        print("Data Updated Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()     

def select_assignment_per_student_per_course():
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = """select  assignment_per_student_per_course.as_per_st_per_c_id, assignments.title, courses.title, students.firstName, students.lastName
                  from assignments
                  inner join assignment_per_student_per_course on assignment_per_student_per_course.asid = assignments.asid
                  inner join courses on courses.cid= assignment_per_student_per_course.cid
                  inner join students on students.stid = assignment_per_student_per_course.stid
                  order by  assignment_per_student_per_course.as_per_st_per_c_id, assignments.title, courses.title, students.firstName, students.lastName;"""
         myCursor.execute(sql)
         result = myCursor.fetchall()
         for a in result:
             print(a)
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()

def delete_assignment_per_student_per_course(as_per_st_per_c_id):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("delete from assignment_per_student_per_course where as_per_st_per_c_id = %s;")
          assignment_per_student_per_course = (as_per_st_per_c_id,)
          myCursor.execute(sql, assignment_per_student_per_course)
          conn.commit()
          print("Data Deleted Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()


