def power(number, pow):
    print('Функция вызвали с параметроми', number, pow)
    power_lalue = number ** pow
    return power_lalue

my_list = [3, 14, 15, 92, 6]
for element in my_list:
    result = power(element, 10)
    print(result)