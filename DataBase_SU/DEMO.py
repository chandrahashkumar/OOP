import mysql.connector
con =mysql.connector.connect(host='localhost',database='universitydb',user='root',password='Kali@2022$')
ors = con.cursor()
# ors.execute("Create Table Demo(PRN BIGINT PRIMARY KEY,Name VARCHAR(50))")
# ors.execute("Insert into Demo(PRN,Name) Values (41029,'Nikhil')")
# ors.execute('Select * from Demo')
# data = ors.fetchall()
# for d in data:
#     print(d)
#     con.commit()
ors.execute("Delete from Demo Where Name = 'Name'")
ors.execute("Select * from Demo")
data = ors.fetchall()
for d in data:
    print(d)

# ors.execute("SELECT * FROM Students")
# data = ors.fetchall()
# for d in data:
#     print(d)
# data = ors.fetchone()
# fata = ors.fetchone()
# print(data)
# print(data)