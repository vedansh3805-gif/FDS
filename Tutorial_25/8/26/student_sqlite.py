import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Q1. Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Student_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Age INTEGER,
    CGPA REAL
)
""")
conn.commit()


# Q2. Insert Records
students = [
    (1, "Aman", "CSE", 20, 8.5),
    (2, "Rahul", "ECE", 21, 7.8),
    (3, "Anjali", "CSE", 19, 9.1),
    (4, "Priya", "EEE", 22, 7.2),
    (5, "Arjun", "ECE", 20, 8.0)
]

cursor.executemany("""
INSERT OR IGNORE INTO Student
(Student_ID, Name, Department, Age, CGPA)
VALUES (?, ?, ?, ?, ?)
""", students)
conn.commit()


# Q3. Display All Records
cursor.execute("SELECT * FROM Student")
print("Q3:", cursor.fetchall())


# Q4. Display Name and Department
cursor.execute("SELECT Name, Department FROM Student")
print("Q4:", cursor.fetchall())


# Q5. Students from CSE
cursor.execute("SELECT * FROM Student WHERE Department = 'CSE'")
print("Q5:", cursor.fetchall())


# Q6. CGPA greater than 8.0
cursor.execute("SELECT * FROM Student WHERE CGPA > 8.0")
print("Q6:", cursor.fetchall())


# Q7. Age between 18 and 22
cursor.execute("SELECT * FROM Student WHERE Age BETWEEN 18 AND 22")
print("Q7:", cursor.fetchall())


# Q8. Names starting with A
cursor.execute("SELECT * FROM Student WHERE Name LIKE 'A%'")
print("Q8:", cursor.fetchall())


# Q9. Students from CSE or ECE
cursor.execute("""
SELECT * FROM Student
WHERE Department IN ('CSE', 'ECE')
""")
print("Q9:", cursor.fetchall())


# Q10. CGPA not equal to 7.5
cursor.execute("SELECT * FROM Student WHERE CGPA <> 7.5")
print("Q10:", cursor.fetchall())


# Q11. Update CGPA
cursor.execute("""
UPDATE Student
SET CGPA = 9.0
WHERE Student_ID = 1
""")
conn.commit()


# Q12. Update Department
cursor.execute("""
UPDATE Student
SET Department = 'CSE'
WHERE Student_ID = 2
""")
conn.commit()


# Q13. Increase CSE CGPA by 0.2
cursor.execute("""
UPDATE Student
SET CGPA = CGPA + 0.2
WHERE Department = 'CSE'
""")
conn.commit()


# Q14. Delete Student
cursor.execute("""
DELETE FROM Student
WHERE Student_ID = 5
""")
conn.commit()


# Q15. Delete CGPA below 5.0
cursor.execute("""
DELETE FROM Student
WHERE CGPA < 5.0
""")
conn.commit()


# Final Records
cursor.execute("SELECT * FROM Student")
print("Final Table:", cursor.fetchall())


# Close Database
conn.close()