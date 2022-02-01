count = 0

for x in range(3,100):
	for i in range(2,x-1):
		if(x%i == 0):
			count+=1
	if (count == 0):
		print(x)
	count = 0
