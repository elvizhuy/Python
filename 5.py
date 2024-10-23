from datetime import datetime

def calculate_work_time(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    work_time = end - start
    work_time_in_minutes = work_time.total_seconds() / 60
    return work_time_in_minutes

# Input handling
num_employees = int(input())

employee_data = []

for _ in range(num_employees):
    code = input().strip()
    name = input().strip()
    start_time = input().strip()
    end_time = input().strip()
    
    worked_minutes = calculate_work_time(start_time, end_time)
    
    if worked_minutes >= 8 * 60:
        status = "DU"
    else:
        status = "THIEU"
    
    hours = worked_minutes // 60
    minutes = worked_minutes % 60
    employee_data.append((name, hours, minutes, status))

# Sort by work time in descending order
employee_data.sort(key=lambda x: (x[1] * 60 + x[2]), reverse=True)

for name, hours, minutes, status in employee_data:
    print(f"{name} {int(hours)} gio {int(minutes)} phut {status}")
