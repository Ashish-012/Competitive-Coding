def replacePi(s):
	if len(s) == 0:
		return ''
	if len(s) == 1:
		return s

	first = s[0].lower()
	second = s[1].lower()

	if first == 'p' and second == 'i':
		return str(3.14) + replacePi(s[2:])
	else:
		return first + replacePi(s[1:])

print(replacePi('asdqwepisdppisdpppqiiwpis'))