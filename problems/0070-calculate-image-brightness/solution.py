
def calculate_brightness(img):
	if not img:
		return -1
	n,m=len(img),len(img[0])
	for i in range(n):
		if len(img[i])!=m:
			return -1
	summ=0
	for i in range(n):
		for j in range(m):
			if 0<=img[i][j]<=255:
				summ+=img[i][j]
			else:
				return -1
	return (summ/(n*m))

