from events import *
ch = int(input("Enter func: "))
n = int(input("Enter num of students: "))
for i in range(n):
	if ch == 1:
		add()
	elif ch== 2:
		see()
	elif ch == 3:
		break
