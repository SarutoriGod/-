import random


number = random.randint(0,100)


while True:
	user_number = int(input('Введите число: '))
	if user_number == number:
		print('Поздравляю, вы победили')
		break
	elif user_number > number:
		print('Загаданное число меньше')
	else:
		print('Загаданное число больше')
