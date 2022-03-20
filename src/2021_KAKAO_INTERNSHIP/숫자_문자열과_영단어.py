def solution(s):
	answer = ''
	num_list = ['zero', 'one', 'two', 'three', 'four',
				'five', 'six', 'seven', 'eight', 'nine']
	tmp = ''
	for i, c in enumerate(list(s)):
		if c.isdigit():
			answer += c
			continue
		tmp += c
		if tmp in num_list:
			answer += str(num_list.index(tmp))
			tmp = ''
	return int(answer)

def solution(s):
	answer = ''
	num_dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
			   'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
	tmp = ''
	for i, c in enumerate(list(s)):
		if c.isdigit():
			answer += c
			continue
		tmp += c
		if tmp in num_dic:
			answer += str(num_dic[tmp])
			tmp = ''
	return int(answer)
