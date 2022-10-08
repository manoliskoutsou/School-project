import mysql.connector

def make_connection():
    conn = mysql.connector.connect(host = "localhost",
                                  user = "root",
                                  passwd = "18/06/1985mkoutsou",
                                  database = "ind_proj_partb")
    myCursor = conn.cursor()
    return conn, myCursor

def conn_close(myCursor, conn):
     myCursor.close(),conn.close()

def conn_continue(conn):
    conn.rollback()
    