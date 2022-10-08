import mysql.connector
import config

def insert_trainer_per_course(trid, cid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into student_per_course (trid, cid) values (%s, %s);"
        trainer_per_course = (trid, cid)
        myCursor.execute(sql, trainer_per_course)
        conn.commit()
        print("Data Inserted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong",er)
    finally:
        myCursor.close()
        conn.close()

def update_trainer_per_course(trid, cid, tr_per_c_id):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("update trainer_per_course set trid = %s, cid = %s where tr_per_c_id = %s;")
          trainer_per_course = (trid, cid, tr_per_c_id)
          myCursor.execute(sql, trainer_per_course)
          conn.commit()
          print("Data Updated Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()

def select_trainer_per_course():
     try:
         conn, myCursor = config.make_connection()
         myCursor.execute("use ind_proj_partb")
         sql = """select trainer_per_course.tr_per_c_id, trainers.firstName,trainers.lastName, courses.title
                  from trainers
                  inner join trainer_per_course on trainer_per_course.trid = trainers.trid
                  inner join courses on courses.cid= trainer_per_course.cid
                  order by trainer_per_course.tr_per_c_id, trainers.firstName,trainers.lastName, courses.title;"""
         myCursor.execute(sql)
         result = myCursor.fetchall()
         for a in result:
             print(a)
     except mysql.connector.Error as er:
         print("Something went wrong",er)
     finally:
         myCursor.close()
         conn.close()

def delete_trainer_per_course(tr_per_c_id):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("delete from trainer_per_course where tr_per_c_id = %s;")
          trainer_per_course = (tr_per_c_id,)
          myCursor.execute(sql, trainer_per_course)
          conn.commit()
          print("Data Deleted Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong",er)
      finally:
          myCursor.close()
          conn.close()


       