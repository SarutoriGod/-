arr = []
N_arr = []
N = int(input('Введите длину массива: '))
 
 
print('Теперь надо заполнить наш массив!')
for i in range(0, N):
    arr.append(int(input(f'Введите {i}-й элемент: ')))
 
 
print('Добавим еще 5 элементов...')
for i in range(0, 5):
    arr.append(int(input(f'Введите {i}-й элемент: ')))
 
for i in range(0, len(arr)):
    if arr[i] % 2 != 0:
        N_arr.append(arr[i])
 
 
print(f'Было {arr}')
print(f'Стало {N_arr}')