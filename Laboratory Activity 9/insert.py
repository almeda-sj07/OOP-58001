import pyodbc
from pyodbc import Cursor

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\steff\OneDrive\Documents\Database1.accdb;')
    print("Connected to a Database")

    user_id = 11
    Inventors = "Tiffany Kate S. Evangelista, Stephanie Joy G. Almeda, Ralph Mikhail B. Barbado, Rafael B. Espina, Jeremiah L. Manalang, Joanna Micka E. Medina, Alexander Tomagan, Charles Ian B. Villamin"
    Invention = "Lab9"
    Date_of_Invention = 2022
    Description = "The group made a Python program that connects to a Database File to insert data."

    record = connect.cursor()
    record.execute("INSERT INTO tblInventor VALUES (?,?,?,?,?)", (user_id, Inventors, Invention, Date_of_Invention, Description))
    record.commit()
    print("Data is inserted")

except pyodbc.Error as e:
    print("Error in Connection")
