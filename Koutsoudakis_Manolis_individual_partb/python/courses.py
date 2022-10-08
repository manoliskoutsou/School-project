import mysql.connector
import config

def insert_course(title, stream1, type1, start_date, end_date):
     try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into courses (title, stream1, type1, start_date, end_date) values (%s, %s, %s, %s, %s);"
        course = (title, stream1, type1, start_date, end_date)
        myCursor.execute(sql, course)
        conn.commit()
        print("Data Inserted Successfully")
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()

def update_course(title, stream1, type1, start_date, end_date, cid):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("update courses set title = %s, stream1 = %s, type1 = %s, start_date = %s, end_date = %s where cid = %s;")
          course = (title, stream1, type1, start_date, end_date, cid)
          myCursor.execute(sql, course)
          conn.commit()
          print("Data Updated Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()

def select_courses():
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = "Select * from courses;"
         myCursor.execute(sql)
         result = myCursor.fetchall()
         for a in result:
             print(a)
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()
       
def delete_course(cid):
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = "delete from courses where cid = %s;"
         course =(cid,)
         myCursor.execute(sql, course)
         conn.commit()
         print("Data Deleted Successfully")
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()






   


