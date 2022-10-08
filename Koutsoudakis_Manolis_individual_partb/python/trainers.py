import mysql.connector
import config

def insert_trainer(firstName, lastName, subject1):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "insert into trainers (firstName, lastName, subject1) values (%s, %s, %s);"
        trainer = (firstName, lastName, subject1)
        myCursor.execute(sql, trainer)
        conn.commit()
        print("Data Inserted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong", er)
    finally:
        myCursor.close()
        conn.close()

def update_trainer(firstName, lastName, subject1, trid):
      try:
          conn, myCursor = config.make_connection()
          myCursor.execute("use ind_proj_partb")
          sql = ("update trainers set firstName = %s, lastName = %s, subject1 = %s where trid = %s;")
          trainer = (firstName, lastName, subject1, trid)
          myCursor.execute(sql, trainer)
          conn.commit()
          print("Data Updated Successfully")
      except mysql.connector.Error as er:
          print("Something went wrong", er)
      finally:
          myCursor.close()
          conn.close()

def select_trainers():
       try:
           conn, myCursor = config.make_connection()
           myCursor.execute("use ind_proj_partb")
           sql = "Select * from trainers;"
           myCursor.execute(sql)
           result = myCursor.fetchall()
           for a in result:
               print(a)
       except mysql.connector.Error as er:
           print("Something went wrong", er)
       finally:
           myCursor.close()
           conn.close()

def delete_trainer(trid):
    try:
        conn, myCursor = config.make_connection()
        myCursor.execute("use ind_proj_partb")
        sql = "delete from trainers where trid = %s;"
        trainer =(trid,)
        myCursor.execute(sql, trainer)
        conn.commit()
        print("Data Deleted Successfully")
    except mysql.connector.Error as er:
        print("Something went wrong", er)
    finally:
        myCursor.close()
        conn.close()

   


