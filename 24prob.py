key = list(input().split())
value = list(input().split())
n = 0
dic = {}
for i in key:
	x = value[n]
	a = {int(i):x}
	dic.update(a)
	n += 1


for i, (key, value) in enumerate(dic.items()):
	print(key, "--", value )