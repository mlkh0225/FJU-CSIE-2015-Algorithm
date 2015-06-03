chars = int(raw_input())
char_dict = dict()

for i in range(0, chars):
	a = raw_input()
#	t = int(a.find(', '))
	t = int(a.find(',')) + 1
	e = len(a)
#	if t == -1:
#		t = int(a.find(',')) + 1
#	else:
#		t = t + 2
	word = a[0]
	frequency = int(a[t:e])
	char_dict[frequency] = '1'+word

t = char_dict.keys()
#print t
#t.sort()
#for key in t:
#	print key, char_dict[key]

output_dict = dict(char_dict)
while True:
	t.sort()
	i = 0
	j = 1
	k_d = t[i]+t[j]
	output_dict[k_d] = '0' + output_dict[t[i]] + output_dict[t[j]]
	del output_dict[t[i]]
	del output_dict[t[j]]
	t.pop(0)
	t.pop(0)
	t.append(k_d)
	if len(output_dict)==1:
		break

print output_dict[t[0]]