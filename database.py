import mysql.connector
from tkinter import messagebox

def connect_db():
    try: 
        conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql123",
        database = "student_management",
        )
        mycursor = conn.cursor()
        return conn,mycursor
    except mysql.connector.Error as e:
        messagebox.showerror(f"Database Error: {e}")
        return None, None

conn, mycursor = connect_db()

def insert(stuId, stuName, stuDOB, stuGender, stuProgram):
    sql = "INSERT INTO students (stuId, stuName, stuDOB, stuGender,stuProgram) VALUES (%s, %s, %s, %s, %s)"
    values = (stuId, stuName, stuDOB, stuGender, stuProgram)
    try:
        mycursor.execute(sql, values)
        conn.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

def id_exist(stuId):
    mycursor.execute('SELECT COUNT(*) FROM students WHERE stuId = %s', (stuId,))
    result = mycursor.fetchone()
    return result[0]> 0

def fetch_students():
    mycursor.execute('SELECT * from students')
    result = mycursor.fetchall()
    return result

def update(id,new_name,new_DOB,new_Gender,new_Program):
    mycursor.execute('UPDATE students SET stuName=%s,stuDOB=%s,stuGender=%s,stuProgram=%s WHERE stuId = %s', (new_name,new_DOB,new_Gender,new_Program,id))
    conn.commit()

def delete(stuId):
    mycursor.execute('DELETE FROM students WHERE stuId = %s', (stuId,))
    conn.commit()

def search(option, value): 
    option = option.lower().strip()
    column_map = {
        "student id": "stuId",
        "name": "stuName",
        "gender": "stuGender",
        "program": "stuProgram"
    }
    column = column_map.get(option)
    if column is None:
        raise ValueError(f"Invalid search option: {option}") 
    sql = "SELECT * FROM students WHERE {} = %s".format(column)
    print("Executing SQL:", sql, "| With value:", value)  
    mycursor.execute(sql, (value,))
    return mycursor.fetchall()

def delete_all_students():
    mycursor.execute("TRUNCATE TABLE students")
    conn.commit()

connect_db()