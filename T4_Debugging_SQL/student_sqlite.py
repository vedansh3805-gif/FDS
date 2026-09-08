import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Q1. Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Student_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Age INTEGER,
    CGPA REAL
)
""")


# Q2. Insert five records
cursor.execute("""
INSERT OR REPLACE INTO Student
(Student_ID, Name, Department, Age, CGPA)
VALUES
(1, 'Aman', 'CSE', 20, 8.5),
(2, 'Riya', 'ECE', 21, 9.0),
(3, 'Arjun', 'CSE', 19, 7.5),
(4, 'Neha', 'MECH', 22, 6.8),
(5, 'Ankit', 'ECE', 20, 5.5)
""")

conn.commit()


# Q3. Display all records
print("\nQ3. All Students:")
cursor.execute("SELECT * FROM Student")
for row in cursor.fetchall():
    print(row)


# Q4. Display Name and Department
print("\nQ4. Name and Department:")
cursor.execute("SELECT Name, Department FROM Student")
for row in cursor.fetchall():
    print(row)


# Q5. Students belonging to CSE
print("\nQ5. CSE Students:")
cursor.execute("""
SELECT * FROM Student
WHERE Department = 'CSE'
""")
for row in cursor.fetchall():
    print(row)


# Q6. Students whose CGPA is greater than 8.0
print("\nQ6. CGPA greater than 8.0:")
cursor.execute("""
SELECT * FROM Student
WHERE CGPA > 8.0
""")
for row in cursor.fetchall():
    print(row)


# Q7. Students whose age is between 18 and 22
print("\nQ7. Age between 18 and 22:")
cursor.execute("""
SELECT * FROM Student
WHERE Age BETWEEN 18 AND 22
""")
for row in cursor.fetchall():
    print(row)


# Q8. Students whose names start with A
print("\nQ8. Names starting with A:")
cursor.execute("""
SELECT * FROM Student
WHERE Name LIKE 'A%'
""")
for row in cursor.fetchall():
    print(row)


# Q9. Students from CSE or ECE
print("\nQ9. CSE or ECE Students:")
cursor.execute("""
SELECT * FROM Student
WHERE Department IN ('CSE', 'ECE')
""")
for row in cursor.fetchall():
    print(row)


# Q10. Students whose CGPA is not equal to 7.5
print("\nQ10. CGPA not equal to 7.5:")
cursor.execute("""
SELECT * FROM Student
WHERE CGPA != 7.5
""")
for row in cursor.fetchall():
    print(row)


# Q11. Update CGPA of a student using Student_ID
cursor.execute("""
UPDATE Student
SET CGPA = 8.2
WHERE Student_ID = 3
""")
conn.commit()

print("\nQ11. Updated Student ID 3:")
cursor.execute("""
SELECT * FROM Student
WHERE Student_ID = 3
""")
print(cursor.fetchone())


# Q12. Change department of a particular student
cursor.execute("""
UPDATE Student
SET Department = 'CSE'
WHERE Student_ID = 4
""")
conn.commit()

print("\nQ12. Updated Department of Student ID 4:")
cursor.execute("""
SELECT * FROM Student
WHERE Student_ID = 4
""")
print(cursor.fetchone())


# Q13. Increase CGPA of all CSE students by 0.2
cursor.execute("""
UPDATE Student
SET CGPA = CGPA + 0.2
WHERE Department = 'CSE'
""")
conn.commit()

print("\nQ13. CSE students after CGPA increase:")
cursor.execute("""
SELECT * FROM Student
WHERE Department = 'CSE'
""")
for row in cursor.fetchall():
    print(row)


# Q14. Delete a student based on Student_ID
cursor.execute("""
DELETE FROM Student
WHERE Student_ID = 5
""")
conn.commit()

print("\nQ14. Records after deleting Student ID 5:")
cursor.execute("SELECT * FROM Student")
for row in cursor.fetchall():
    print(row)


# Q15. Delete students whose CGPA is below 5.0
cursor.execute("""
DELETE FROM Student
WHERE CGPA < 5.0
""")
conn.commit()

print("\nQ15. Final Student Records:")
cursor.execute("SELECT * FROM Student")
for row in cursor.fetchall():
    print(row)


# Close database
conn.close()