def abbreviate(word, word_length):
	middle = word_length - 2
	result = word[0] + str(middle) + word[-1]
	return result


def solve():
	
	word = input()
	word_length = len(word)
	
	if(word_length > 10):
		abbreviation = abbreviate(word, word_length)
		print(abbreviation)
		return
	
	print(word)
	return


num_tests = int(input())

for each_test in range(num_tests):
	solve()