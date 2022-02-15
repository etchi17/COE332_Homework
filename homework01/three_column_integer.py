int_list = []
for x in range(1,10):
	int_list.append(x)

int_list_sq = []
for x in range(9):
	int_list_sq.append(int_list[x]**2)

int_list_cu = []
for x in range(9):
	int_list_cu.append(int_list[x]**3)

for x in range(9):
	print(int_list[x], ", ", int_list_sq[x], ", ", int_list_cu[x])
