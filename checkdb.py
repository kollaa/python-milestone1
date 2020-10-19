import sqlite3, csv
 
conn = sqlite3.connect('patientsdetail.db')
 
c = conn.cursor()
c.execute("SELECT * FROM PATIENT")


#c.execute("DROP TABLE PATIENT")

 
print(c.fetchall())

c.close()
conn.close()

