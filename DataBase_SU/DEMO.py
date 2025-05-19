import mysql.connector
import password_
con =mysql.connector.connect(host='localhost',database='universitydb',user='root',password=password_.password)
ors = con.cursor()

# ors.execute("Create Table Demo(PRN BIGINT PRIMARY KEY,Name VARCHAR(50))")
s = int(input("Enter number of students you want to enter: "))
for i in range(s):
    PRN = int(input("Enter PRN: "))
    Name = input("Enter Name: ")
    ors.execute(f"INSERT INTO Demo (PRN,Name) VALUES ('{PRN}','{Name}')")
    con.commit()

ors.execute("SELECT * FROM Demo")
data = ors.fetchall()
print(data)
ors.close()
# data = ors.fetchone()
# fata = ors.fetchone()
# print(data)
# print(data)