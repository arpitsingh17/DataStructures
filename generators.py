def factors(n):
	for k in range(1,n+1):
		if n % k == 0:
			yield k

var = factors(100)
for i in var:
	print i