employeeId = int(input("Enter the Employee Id : "))
employeeName = input("Enter the Employee Name : ")
designation = input("Enter the Designation : ")
basicSalary = float(input("Enter the Basic Salary : "))

da = basicSalary * 0.5
hra = basicSalary * 0.35
ta = basicSalary * 0.25

grossSalary = basicSalary + da + hra + ta

print("**************************************")

print("Employee Id: ", employeeId)
print("Employee Name: ", employeeName)
print("Designation: ", designation)
print("Basic Salary: ", basicSalary)

print("Gross Salary : ", grossSalary)