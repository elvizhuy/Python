from datetime import datetime, timedelta

def calculate_work_time(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    work_duration = end - start - timedelta(hours=1)
    work_minutes = work_duration.total_seconds() // 60
    return work_minutes

num_employees = int(input())
employees = []

for _ in range(num_employees):
    emp_id = input().strip()
    emp_name = input().strip()
    start_time = input().strip()
    end_time = input().strip()
    
    work_minutes = calculate_work_time(start_time, end_time)
    status = "DU" if work_minutes >= 480 else "THIEU"
    
    hours = work_minutes // 60
    minutes = work_minutes % 60
    
    employees.append((work_minutes, emp_id, emp_name, int(hours), int(minutes), status))

employees.sort(reverse=True, key=lambda x: x[0])

for emp in employees:
    print(f"{emp[1]} {emp[2]} {emp[3]} gio {emp[4]} phut {emp[5]}")
