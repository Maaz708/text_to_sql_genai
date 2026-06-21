import sqlite3

connection = sqlite3.connect("student.db")


cursor = connection.cursor()


table_info = """
    Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
    SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

cursor.execute('''
               Insert into STUDENT values('krish','Data Science','A',30)
               ''')
cursor.execute('''
               Insert into STUDENT values('Maaz','Computer Science','C',39)
               ''')
cursor.execute('''
               Insert into STUDENT values('Arbas','Information Science','A',55)
               ''')
cursor.execute('''
               Insert into STUDENT values('Khalid','Mechanical','B',60)
               ''')
cursor.execute('''
               Insert into STUDENT values('Sajid','AI/ML','A',69)
               ''')
cursor.execute('''
Insert into STUDENT values('Ayaan','Data Science','B',72)
''')

cursor.execute('''
Insert into STUDENT values('Zara','Computer Science','A',88)
''')

cursor.execute('''
Insert into STUDENT values('Ishaan','AI/ML','C',45)
''')

cursor.execute('''
Insert into STUDENT values('Meera','Information Science','B',91)
''')

cursor.execute('''
Insert into STUDENT values('Rohan','Mechanical','A',53)
''')

cursor.execute('''
Insert into STUDENT values('Fatima','Data Science','C',67)
''')

cursor.execute('''
Insert into STUDENT values('Kabir','Computer Science','B',38)
''')

cursor.execute('''
Insert into STUDENT values('Nina','AI/ML','A',74)
''')

cursor.execute('''
Insert into STUDENT values('Aditya','Information Science','C',82)
''')

cursor.execute('''
Insert into STUDENT values('Sara','Mechanical','B',59)
''')

print("Inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()