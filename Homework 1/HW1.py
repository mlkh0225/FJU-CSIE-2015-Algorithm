m_number = int(raw_input())

def m_order (num):
	diff_order = 0
	if num < 2:
		return 1
	for i in range (1,num):
		diff_order = diff_order+m_order(i)*m_order(num-i)
	return diff_order

print m_order(m_number)