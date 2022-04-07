from multiprocessing import connection
from sqlite3 import connect
from tkinter.messagebox import YES
import pypyodbc as odbc 
# pip install pypyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-N6OKRTJP\LOCALDB#FE1E5C3E' 
DATABASE_NAME = "Python"
#SELECT @@SERVERNAME

#uid=<username>
#password<password>
connection_string = f"""
DRIVER={{{DRIVER_NAME}}}
SERVER={SERVER_NAME}
DATABASE={DATABASE_NAME}
Trust_Connection=YES
"""

conn = odbc.connect(connection_string)
print(conn)