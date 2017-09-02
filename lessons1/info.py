user_info = {'first_name' : 'lena', 'last_name': 'glukhova'}
user_first_name = input('Введите имя: ')
user_info['first_name'] = user_first_name
user_last_name = input('Введите фамилию: ')
user_info['last_name'] = user_last_name
for key in user_info:
	print(user_info[key])