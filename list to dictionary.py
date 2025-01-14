students = [[1, "Rayed", "VI"], [2, "Mimo", "VI"]]

print(students)

result={}

for item in students:
    result[item[0]] = item[1:]

print(result)    