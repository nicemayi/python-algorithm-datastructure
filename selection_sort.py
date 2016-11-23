def selection_sort(aList):
	for i in range(len(aList)):
		for j in range(len(aList) - 1 - i):
			if aList[j] > aList[j + 1]:
				aList[j], aList[j + 1] = aList[j + 1], aList[j]
	return aList

if __name__ == "__main__":
	aList = [5,4,1,2,31,5,1,2,6,5,3,2]
	sorted_list = selection_sort(aList)
	print(sorted_list)
	print(aList)