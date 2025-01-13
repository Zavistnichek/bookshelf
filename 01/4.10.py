user_numbers = input('Введите список чисел через пробел: ')
user_sort = input('Как сортировать? (1 - по возрастанию, 2 - по убыванию): ')

while user_sort not in ['1', '2']:
    print('Ошибка: введите 1 или 2.')
    user_sort = input('Как сортировать? (1 - по возрастанию, 2 - по убыванию): ')

numbers_list = list(map(int, user_numbers.split()))

if user_sort == '1':
    numbers_list.sort()
    print(f'По возрастанию: {numbers_list}')
else:
    numbers_list.sort(reverse=True)
    print(f'По убыванию: {numbers_list}')
