from flask import g
from flaskext.mysql import MySQL


mysql = MySQL()

def select(raw_sql):
  conn = mysql.connect()
  cursor = conn.cursor()    
  cursor.execute(raw_sql)
  result = cursor.fetchall()
  cursor.close()
  conn.close()
  return result
