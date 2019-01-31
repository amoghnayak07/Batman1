a = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
n = []
search = int(input())
for i, value in enumerate(a):
	if value == search:
		n.append(i)
print(n)