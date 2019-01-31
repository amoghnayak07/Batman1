num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []
old = []
for i in num:
	if i < 5:
		new.append(i)
	else:
		old.append(i)
print(new)
print(old)

