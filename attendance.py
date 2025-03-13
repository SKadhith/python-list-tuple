from datetime import datetime

# Sample Employee Data (Tuples)
employees = [
    (101, "Adhithyan", "IT"),
    (102, "Babu", "IT"),
    (103, "Sibi", "Finance"),
    (104, "Dhanush", "IT"),
    (105, "Sibi nila", "Marketing")
]

# Sample Attendance Records (List of Tuples)
attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

# Function to mark attendance
def mark_attendance(employee_id, status):
    today = datetime.today().strftime('%Y-%m-%d')  
    attendance_records.append((employee_id, today, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")

# Function to search attendance by Employee ID
def search_attendance(employee_id):
    records = [rec for rec in attendance_records if rec[0] == employee_id]
    
    if records:
        print(f"\n Searching Attendance for Employee ID {employee_id}:")
        for record in records:
            print(f"Date: {record[1]}, Status: {record[2]}")
    else:
        print("No attendance records found for this employee.")

def display_summary():
    print("\nAttendance Summary:")
    for emp in employees:
        emp_id = emp[0]
        emp_records = [rec for rec in attendance_records if rec[0] == emp_id]
        
        total_days = len(emp_records)
        present_days = sum(1 for rec in emp_records if rec[2] == "Present")
        
        if total_days > 0:
            attendance_percentage = (present_days / total_days) * 100
            print(f"{emp[1]}: {attendance_percentage:.2f}% Present")
        else:
            print(f"{emp[1]}: No attendance records found.")

# Example Usage
mark_attendance(101, "Present")
mark_attendance(102, "Present")
mark_attendance(103, "Absent")
mark_attendance(104, "Present")
mark_attendance(105, "Present")

search_attendance(102)
display_summary()
