def howMax(a,b):
	abAdd = a+b
	abMul = a*b
	return max(abAdd,abMul)

numbersOfFloat = int(raw_input())
floatNums = [float()]*numbersOfFloat

generalIndex = 0

for item in floatNums:
	floatNums[generalIndex] = float(raw_input())
	generalIndex = generalIndex + 1

table = [list()]*numbersOfFloat
functionTable = [list()]*numbersOfFloat

generalIndex = 0
index = 0

for list in table:
	table[generalIndex] = [float()]*numbersOfFloat
	functionTable[index] = ['']*numbersOfFloat
	table[generalIndex][generalIndex] = floatNums[generalIndex]
	generalIndex = generalIndex + 1
	index = index + 1

for index in range(0, numbersOfFloat-1):
	table[index][index+1]=howMax(table[index][index],floatNums[index+1])

for generalIndex in range(2, numbersOfFloat):
	for list in table:
		list[generalIndex]=max(howMax(list[generalIndex-1],floatNums[generalIndex]),howMax(list[generalIndex-2],table[generalIndex-1][generalIndex]))
		generalIndex = generalIndex + 1
		if generalIndex == numbersOfFloat:
			break

if table[0][numbersOfFloat-1]-int(table[0][numbersOfFloat-1])==0:
	print int(table[0][numbersOfFloat-1])
else:
	print table[0][numbersOfFloat-1]
