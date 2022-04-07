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


#https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-python-from-the-command-line
#https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=reinstall%20Python%203.9.-,'Pip'%20Is%20Not%20Recognized%20as%20an%20Internal%20or%20External%20Command,via%20the%20Python%20executable%20installer.
