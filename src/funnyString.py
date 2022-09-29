def funnyString(s):
	head = 0
	tail = len(s) - 1
	while head < tail:
		if abs(ord(s[head]) - ord(s[head+1])) != abs(ord(s[tail]) - ord(s[tail-1])):
			return 'Not Funny'
		head, tail = head + 1, tail - 1
	return 'Funny'


