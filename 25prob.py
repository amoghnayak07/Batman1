key = list(input("Enter keys: ").split())
value = list(input("Enter values: ").split())
n = 0
dic = {}
for i in key:
	x = value[n]
	a = {i:x}
	dic.update(a)
	n += 1





search_element = input("Enter element to be searched: ")





for i in key:
	if dic[i] == search_element:
		print("Key of searched value is ", i)
