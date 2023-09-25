employees=[{"name":"ajay","salary":300},{"name":"shyam","salary":400},{"name":"ram","salary":900}]

max_salary=0

for employee in employees:
    if employee["salary"] > max_salary:
        max_salary = employee["salary"]

print("Maximum salary:", max_salary)