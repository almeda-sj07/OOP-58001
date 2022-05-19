import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\steff\OneDrive\Desktop\files\Database1.accdb;')
    print("Connected to a Database")

    record = connect.cursor()
    record.execute('select * from Table1')
    for row in record.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection")
