import mysql.connector
import config

def insert_student(firstName, lastName, dateOfBirth, tuitionFees):
     try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into students (firstName, lastName, dateOfBirth, tuitionFees) values (%s, %s, %s, %s);"
        student = (firstName, lastName, dateOfBirth, tuitionFees)
        myCursor.execute(sql, student)
        conn.commit()
        print("Data Inserted Successfully")
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()
  
def update_student(firstName, lastName, dateOfBirth, tuitionFees, stid):
     try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = ("update students set firstName = %s, lastName = %s, dateOfBirth = %s, tuitionFees = %s where stid = %s;")
        student = (firstName, lastName, dateOfBirth, tuitionFees, stid)
        myCursor.execute(sql, student)
        conn.commit()
        print("Data Updated Successfully")
     except mysql.connector.Error as er:
        print("Something went wrong", er)
     finally:
          myCursor.close()
          conn.close()
       
def select_students():
       try:
           conn, myCursor = config.make_connection()
           myCursor.execute("use ind_proj_partb")
           sql = "Select * from students;"
           myCursor.execute(sql)
           result = myCursor.fetchall()
           for a in result:
               print(a)
       except mysql.connector.Error as er:
           print("Something went wrong", er)
       finally:
           myCursor.close()
           conn.close()
       
def delete_student(stid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "delete from students where stid = %s;"
        student =(stid,)
        myCursor.execute(sql, student)
        conn.commit()
        print("Data Deleted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong", er)
    finally:
        myCursor.close()
        conn.close()


  


