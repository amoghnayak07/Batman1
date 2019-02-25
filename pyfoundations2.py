def fun(g1):
	s2 = []
	i = subject.index(g1)
	for key, value in enumerate(score):
	
		s = score[value]
		s1 = s[i]
		s2.append(s1)
		s2.sort()
	print(s2)

		
		#print(g1, " has scored: " score(g1).sort())

score = {'Amogh':[99, 99, 89, 70, 90], 'Raju':[69, 69, 69, 69, 69]}
#give1 = input("Enter suject: ").capitalize()
give1 = input("Enter subject: ").capitalize()
subject = ['Math', 'Physics', 'Chemistry', 'Biology', 'Social Science']
fun(give1)		