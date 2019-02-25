def fun(g2, g1):
	for key, value in enumerate(score):
		l = [g2, g1]
		g = ' '.join(l)
		if value == g:
			print(g2, " scored", score[g], " in ", g1)

score = {'Amogh Math':99, 'Amogh Physics':99, 'Amogh Chemistry':89, 'Amogh Biology':75, 'Amogh Social Science':90, 'Raju Math':69, 'Raju Physics':69, 'Raju Chemistry':69, 'Raju Biology':69, 'raju Social Science':69}
give1 = input("Enter suject: ").capitalize()
give2 = input("Enter name: ").capitalize()
fun(give2, give1)