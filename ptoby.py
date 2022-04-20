# корректный ввод пользователя
while True:
    user_input = input('Введите 42 >> ')
    result = int(user_input)
    if result == 42:
        print('Спасибо за сотрудничество!')
        break
    else:
        print('Я просил 42, а Вы ввели', result, 'Попробуйте еще раз...')
        #проверка git c ноута