def round_number(number):
	count = 0
	result = []
	length = len(number)
	for index, digit in reversed(list(enumerate(number))):
		num = int(number[index])
		if(num):
			place_value = length - (index + 1)
			if(place_value == 0):
				result.append(num)
			else:
				result.append(num * (10**place_value))
			count = count + 1
	print(count)
	print(*result)






num_tests =  int(input())

for each_test in range(num_tests):
	input_num = input()
	round_number(input_num)