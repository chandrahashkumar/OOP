import mysql.connector
con =mysql.connector.connect(host='localhost',database='universitydb',user='root',password='Kali@2022$')
ors = con.cursor()
#ors.execute("CREATE TABLE STUDENT_DATA(PRN VARCHAR(12) PRIMARY KEY, NAME VARCHAR (50),SEX VARCHAR(20),BRANCH VARCHAR(100),EMAIL_ID VARCHAR(100) UNIQUE,MOBILE BIGINT,ADMISSION_DATE DATE)")
# ors.execute("ALTER TABLE STUDENT_DATA RENAME COLUMN MOBILE TO MOBILE_NUMBER ")
print("____WELCOME TO STUDENT DATABASE____")
print("PRESS ANY KEY TO CONTINUE")
input()
while True:
    print("\n1. ADD New Student\n2. Display Students List\n3. Delete data\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s = int(input("Enter number of students you want to enter: "))
        for i in range(s):
            PRN = int(input("Enter PRN: "))
            Name = input("Enter Name: ")
            Sex = input("Enter sex: ")
            Branch = input("Enter Branch: ")
            Email = input("Enter Email: ")
            Mobile = int(input("Enter Mobile Number: "))
            Admission_Date = input("Enter Admission Date(YYYY-MM-DD): ")
            ors.execute(f"INSERT INTO STUDENT_DATA(PRN,Name,Sex,Branch,Email_ID,Mobile_Number,Admission_Date) VALUES ('{PRN}','{Name}','{Sex}','{Branch}','{Email}','{Mobile}','{Admission_Date}') ")
    if choice == 2:
        ors.execute("SELECT * FROM STUDENT_DATA")
        d = ors.fetchall()
        print(d)
    elif choice == 4:
        print("Thanks for using our service")
        break

