import mysql.connector
import config

def insert_assignment(title, description1, subDateTime, oralMark, totalMark):
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = "insert into assignments (title, description1, subDateTime, oralMark, totalMark) values (%s, %s, %s, %s, %s);"
         assignment = (title, description1, subDateTime, oralMark, totalMark)
         myCursor.execute(sql, assignment)
         conn.commit()
         print("Data Inserted Successfully")
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()

def update_assignment(title, description1, subDateTime, oralMark, totalMark, asid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = ("update assignments set title = %s, description1 = %s, subDateTime = %s, oralMark = %s, totalMark = %s where asid = %s;")
        assignment = (title, description1, subDateTime, oralMark, totalMark, asid)
        myCursor.execute(sql, assignment)
        conn.commit()
        print("Data Updated Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

def select_assignments():
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "Select * from assignments;"
        myCursor.execute(sql)
        result = myCursor.fetchall()
        for a in result:
            print(a)
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

def delete_assignment(asid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "delete from assignments where asid = %s;"
        assignment =(asid,)
        myCursor.execute(sql, assignment)
        conn.commit()
        print("Data Deleted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

    


