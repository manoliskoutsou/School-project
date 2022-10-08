import mysql.connector
import config

def insert_student_per_course(stid, cid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into student_per_course (stid, cid) values (%s, %s);"
        student_per_course = (stid, cid)
        myCursor.execute(sql, student_per_course)
        conn.commit()
        print("Data Inserted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

def update_student_per_course(stid, cid, st_per_c_id ):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("update student_per_course set stid = %s, cid = %s where st_per_c_id = %s;")
          student_per_course = (stid, cid, st_per_c_id)
          myCursor.execute(sql, student_per_course)
          conn.commit()
          print("Data Updated Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()

def select_student_per_course():
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = """select  student_per_course.st_per_c_id, students.firstName,students.lastName, courses.title
                  from students
                  inner join student_per_course on student_per_course.stid = students.stid
                  inner join courses on courses.cid= student_per_course.cid
                  order by student_per_course.st_per_c_id, students.firstName,students.lastName, courses.title;"""
         myCursor.execute(sql)
         result = myCursor.fetchall()
         for a in result:
             print(a)
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()
       
def delete_student_per_course(st_per_c_id):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("delete from student_per_course where st_per_c_id = %s;")
          student_per_course = (st_per_c_id,)
          myCursor.execute(sql, student_per_course)
          conn.commit()
          print("Data deleted Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()

