def get_summ(word, num, delimetre = ' '):
	output_string = word + str(delimetre) + str(num)
	return output_string.upper()
print(get_summ('Hello', 2, '&'))
