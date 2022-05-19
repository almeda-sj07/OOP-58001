import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\steff\OneDrive\Desktop\files\Database1.accdb;')
    print("Connected to a Database")

    Fullname = "Almeda, Stephanie Joy G."
    Assignment = 87
    Laboratory = 90
    Quiz = 85
    Exam = 94
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?, Quiz = ?, Exam = ? WHERE id = ?', (Fullname, Assignment, Laboratory, Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
