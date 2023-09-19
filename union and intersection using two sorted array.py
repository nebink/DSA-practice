def Unionarray(arr1, arr2, n, m):

	seta = set(arr1)
	setb= set(arr2)

	result = list(seta.union(setb))
	return result


if __name__ == "__main__":
	arr1 = [1, 2, 2, 2, 3]
	arr2 = [2, 3, 3, 4, 5, 5]
	n = len(arr1)
	m = len(arr2)


	uni = Unionarray(arr1, arr2, n, m)
	for i in uni:
		print(i, end=" ")
