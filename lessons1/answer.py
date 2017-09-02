def get_answer(question, to = 'чувак'):
	answer = {'привет':'И тебе привет!'
	, 'как дела': 'Лучше всех'
	, 'пока': 'Увидимся!'}
	return str(answer[question].lower())+', '+to

print(get_answer(input('введи вопрос: ')))