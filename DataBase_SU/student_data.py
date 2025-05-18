import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kali@2022$",
    database="universitydb"
)
cursor = db.cursor()

# cursor.execute("CREATE TABLE STUDENT_DATA(PRN VARCHAR(12) PRIMARY KEY, NAME VARCHAR (50),SEX VARCHAR(20),BRANCH VARCHAR(100),EMAIL_ID VARCHAR(100) UNIQUE,MOBILE BIGINT,DOB DATE,ADMISSION_YEAR YEAR)")
# cursor.execute("ALTER TABLE STUDENT_DATA RENAME COLUMN MOBILE TO MOBILE_NUMBER ")
# cursor.execute("ALTER TABLE student_data ADD COLUMN ADDRESS VARCHAR(300)")

print("____WELCOME TO STUDENT DATABASE____")
print("PRESS ANY KEY TO CONTINUE")
input()
while True:
    print("\n1. ADD New Student\n2. Display Students List\n3. Update Student detail\n4. Delete data\n5. Exit")
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
            DOB = input("Enter Date of Birth(YYYY-MM-DD): ")
            Address = input("Enter Address: ")
            Admission_Year = input("Enter Admission Year: ")
            quary = f"INSERT INTO STUDENT_DATA(PRN,Name,Sex,Branch,Email_ID,Mobile_Number,DOB,Address,ADMISSION_YEAR) VALUES ('{PRN}','{Name}','{Sex}','{Branch}','{Email}','{Mobile}','{DOB}','{Address}','{Admission_Year}')"
            cursor.execute(quary)
            db.commit()
            print("Data inserted successfully!")
    if choice == 2:
        cursor.execute("SELECT * FROM STUDENT_DATA")
        data = cursor.fetchall()
        for d in data:
            print(d)
    elif choice == 3:
        PRN = int(input("Enter PRN to update: "))
        up = int(input("UPDATE\n1. Name\n2. Sex\n3. Branch\n4. Email\n5. Mobile\n6.Date of Birth\n7. Address\n8. Exit\nEnter your choice: "))
        if up == 1:
            Name = input("Enter New Name: ")
            quary = f"UPDATE STUDENT_DATA SET NAME = '{Name}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 2:
            Sex = input("Enter New Sex: ")
            quary = f"UPDATE STUDENT_DATA SET SEX = '{Sex}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 3:
            Branch = input("Enter New Branch: ")
            quary = f"UPDATE STUDENT_DATA SET BRANCH = '{Branch}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 4:
            Email = input("Enter New Email: ")
            quary = f"UPDATE STUDENT_DATA SET EMAIL_ID = '{Email}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 5:
            Mobile = int(input("Enter New Mobile Number: "))
            quary = f"UPDATE STUDENT_DATA SET MOBILE_NUMBER = '{Mobile}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 6:
            DOB = input("Enter New Date of Birth(YYYY-MM-DD): ")
            quary = f"UPDATE STUDENT_DATA SET DOB = '{DOB}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 7:
            Address = input("Enter New Address: ")
            quary = f"UPDATE STUDENT_DATA SET ADDRESS = '{Address}' WHERE PRN = '{PRN}'"
            cursor.execute(quary)
            db.commit()
            print("Data updated successfully!")
        elif up == 8:
            break
        else:
            print("Invalid choice try again")
    elif choice == 4:
        PRN = int(input("Enter PRN to delete: "))
        quary = f"DELETE FROM STUDENT_DATA WHERE PRN = '{PRN}'"
        cursor.execute(quary)
        db.commit()
        print("Data deleted successfully!")
    elif choice == 5:
        cursor.close()
        db.close()
        print("Thanks for using our service")
        break
    else:
        print("Invalid choice try again")
