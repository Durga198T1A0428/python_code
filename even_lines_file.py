# file=open("find_even_lines_file.txt", mode='w+')
# cricket_batting_order=["Rohit\n","Gill\n","Virat\n","Kl\n","Iyer\n","Hardik\n","MSD\n","Jaddu\n"]
# file.writelines(cricket_batting_order)
# file.close()
# try:
#     file = open("find_even_lines_file.txt", mode='r')
#     file_even = file.readlines()
#     for batters in range(len(file_even)):
#         if batters % 2 == 0:
#             print(file_even[batters])
# except(ZeroDivisionError) as message:
#     print("you are dividing with  0")
#
#     file.close()
# # import os
import csv
# # cwd=os.getcwd()
# # print(cwd)
# # os.mkdir("pythonProject1employee_data")
#
with open("emp.csv", 'w', newline='') as file:
    write_obj = csv.writer(file)
    write_obj.writerow(["name", "dname", "Job", "Emp_no", "Hire_Date", "Location", "salary"])
n = int(input("Enter the number of employees: "))
high_salary_employees = []
for emp_data in range(n):
    name = input("Enter employee name: ")
    dname = input("Enter employee dname: ")
    job = input("Enter employee job name: ")
    Emp_no = input("Enter employee Emp_no: ")
    Hire_Date = input("Enter employee Hire_Date: ")
    Location = input("Enter employee Location: ")
    salary = float(input("Enter employee salary: "))
    if salary > 3000:
        high_salary_employees.append([name, dname, job, Emp_no, Hire_Date, Location, salary])
with open("emp.csv", 'a', newline='') as file:
    write_obj = csv.writer(file)
    write_obj.writerows(high_salary_employees)
# if high_salary_employees:
    for emp in high_salary_employees:
        print(emp)
# else:
#     print("No employees with salary > 3000.")
