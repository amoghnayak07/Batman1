key = list(input("Enter keys for 1st dict").split())
value = list(input("Enter values for 1st dict").split())
n = 0
x = {}
for i in key:
	t = value[n]
	a = {i: t}
	x.update(a)
	n += 1



key2 = list(input("Enter keys for 2snd dict").split())
value2 = list(input("Enter values for 2nd dict").split())
n2 = 0
y = {}
for i in key2:
	u = value2[n2]
	b = {i: u}
	y.update(b)
	n2 += 1



a = list(x.keys())
b = list(x.values())
c = list(y.keys())
d = list(y.values())
o = 0
for  i in a:
	p = b[o]
	q = c[o]
	r = d[o]
	if i == q and p == r:
		print(i, ":", p, " is in both x and y")
	else:
		pass