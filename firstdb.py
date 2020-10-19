import sqlite3
conn = sqlite3.connect("patientsdetail.db")
cur = conn.cursor()

sql = """
   
    CREATE TABLE PATIENT (
        roll TEXT,  
        first_name TEXT,
        last_name  TEXT,
        email TEXT,
        state TEXT,
        country TEXT,
        pincode TEXT,
        phonenumber TEXT,
        primary key(roll)

        ) """

cur.execute(sql)
print(" patient Table has been created")

conn.commit()
conn.close()     

