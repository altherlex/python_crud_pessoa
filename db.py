from flask import g
from flaskext.mysql import MySQL


mysql = MySQL()

def select(raw_sql):
  conn = mysql.connect()
  cursor = conn.cursor()    
  cursor.execute(raw_sql)
  # TODO: Return result as Object instead of a array
  result = cursor.fetchall()
  cursor.close()
  conn.close()
  return result

def insert(raw_sql, values):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(raw_sql, values)
    conn.commit()
    cursor.close()
    conn.close()
