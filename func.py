a = input()
b = list(a)
n = len(a)
new = []
for i in (b[-1::-1]):
	new.append(i)
	
c = "".join(new)
print(c)
