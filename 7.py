n = int(input("Enter number"))
student_marks = {}
for i in range(n):
    name, *line = input("Enter name and score").split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query = input("Name required")
lis = student_marks[query]
a, b, c = lis
avg = (a+b+c)/3.00
print(avg)
