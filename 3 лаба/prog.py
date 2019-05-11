import os


def FindAll():
	path = input('Введите директорию: ')
	count = str(len(next(os.walk(path))[1]))
	return count


def Sort():
	products = []
	file = open('products.txt', 'r')
	for line in file:
		products.append(line.strip().split(';'))
	if not products[0][2].isdigit():
		products.remove(products[0])
	products = [x for x in products if int(x[2]) > 1700]
	products.sort(key= lambda x:x[1])
	products = Stock(products)
	Save(products)
	return products


def Stock(products):
	max_id = -1
	min_id = len(products)**len(products)
	for item in products:
		if int(item[0]) > max_id:
			max_id = int(item[0])
		if int(item[0]) < min_id:
			min_id = int(item[0])
	queue = []
	confirmation = input('Вы хотите изменить цены некоторых товаров? ')
	if confirmation.upper() in stop:
		print(f'{max_id} - максимальный id, {min_id} - минимальный id')
		while True:
			input_id = input('Введите id: ')
			if input_id.isdigit():
				if int(input_id) >= min_id and int(input_id) <= max_id:
					queue.append(input_id)
				else:
					print(f'id не может быть меньше {min_id} и больше {max_id}')
			else:
				if input_id.upper() in stop:
					break
				print('Вводите числа')
		amount = input('Введите число, на которое хотите увеличить: ')
		for item in products:
			if item[0] in queue:
				item[2] = int(item[2]) + abs(int(amount))
	return products


def Save(products):
	while True:
		case = input('Вы желаете сохранить данные в новый файл? \n'
			'0 - выйти из программы \n'
			'1 - сохранить в новый файл \n'
			'2 - сохранить в старый файл \n')
		if case.isdigit():
			if int(case) == 0:
				return products
				break
			elif int(case) == 1:
				file_name = input('Введите название нового файла: ')
				file = open(file_name + '.txt', 'w')
				for i in range(0, len(products)):
					for j in range(0, len(products[i])):
						if 0 <= j <= 2:
							file.write(str(products[i][j]) + ';')
						else:
							file.write(str(products[i][j]))
					file.write('\n')
				file.close()
				break
			elif int(case) == 2:
				file = open("products.txt", "w")
				for i in range(0, len(products)):
					for j in range(0, len(products[i])):
						if 0 <= j <= 2:
							file.write(str(products[i][j]) + ';')
						else:
							file.write(str(products[i][j]))
					file.write('\n')
				file.close()
				break
		else:
			print('Введите число от 0 до 2')


stop = ["YES", "Y", "TRUE", "ДА", "Д", "1", "STOP"]


print('0 - выход из программы \n'
	'1 - первое задание \n'
	'2 - второе задание \n'
	'3 - третье задание \n'
	'4 - четвертое задание \n')
while True:
	command = input('Введите цифру: ')
	if command.isdigit():
		if int(command) == 0:
			confirmation = input('Вы действительно хотите выйти?')
			if confirmation.upper() in stop:
				print('До встречи')
				break
		if int(command) == 1:
			print(FindAll())
		if int(command) == 2:
			print(Sort())
		#if int(command) == 3:
		#if int(command) == 4:
	else:
		print('Для использования функции введите цифру')