a = input("Enter any string: ")
b = list(a)
c = []
cou = []
num = {}
f = 0
for i in b:
	if i not in c:
		c.append(i)
	else:
		pass
c.sort()
for n in c:
	coun = b.count(n)
	cou.append(coun)
print(c)
print(cou)
for s in c:
	t = cou[f]
	lis = {s: t}
	num.update(lis)
	f+=1
print(num)