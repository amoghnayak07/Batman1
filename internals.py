fib = []
n = int(input())

for i in range(n+1):

	if i == 0:
		fib.append(0)

	if i == 1:
		fib.append(1)

	if i > 1:
		fib.append(fib[i-1] + fib[i-2])

print(fib)