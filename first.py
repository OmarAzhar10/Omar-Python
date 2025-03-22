for i in range(1, 11):
    print(f"count is on {i}")

students = ['omar', 'sir', 'karan']
for student in students:
        print(student)

name = "Python"
for char in name:
      print(char , end=",")

count = 1
while count <= 10:
      print(count)
      count += 1

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print('* ', end='')
    print()