while True:
	try:
		chars = int(raw_input('How many different characters? '))
		break
	except:
		print 'Integer only!'
		continue

char_dict = dict()
for i in range(0, chars):
	while True:
		try:
			a = raw_input('Enter [character],[frequency] %d of %d: ' %((i+1),chars))
			a = a.replace(" ", "")
			t = int(a.find(',')) + 1
			e = len(a)
			word = a[0:t-1]
			frequency = int(a[t:e])
			char_dict[frequency] = '1' + word
			break
		except:
			print 'Bad character or frequency, try again!'

t = char_dict.keys()
while len(t)!=1:
	t.sort()
	char_dict[t[0]+t[1]] = '0' + char_dict[t[0]] + char_dict[t[1]]
	t.append(t[0]+t[1])
	t.pop(0)
	t.pop(0)

print 'Result: ' + char_dict[t[0]]