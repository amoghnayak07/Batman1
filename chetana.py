a = input()
b = list(a)
c = []
for i in b:

	if i.isupper():
		j = i.lower()
		c.append(j)
			
	if i.islower():
		k = i.upper()
		c.append(k)
d = ''.join(c)
print(d)