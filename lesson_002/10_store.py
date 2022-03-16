#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

styl_code = goods['Стол']
styl_item = store[styl_code][0]
styl_quantity = styl_item['quantity']
styl_price = styl_item['price']
styl_cost = styl_quantity * styl_price
styl_code = goods['Стол']
styl_item1 = store[styl_code][1]
styl_quantity1 = styl_item1['quantity']
styl_price1 = styl_item1['price']
styl_cost1 = styl_quantity1 * styl_price1
resylt = (styl_cost+styl_cost1)* (styl_price+ styl_price1)
allquantity = styl_quantity + styl_quantity1
print('Стол -', allquantity, 'шт, стоимость', styl_cost, 'руб')

divan_code = goods['Диван']
divan_item = store[divan_code][0]
divan_quantity1 = divan_item['quantity']
divan_price = divan_item['price']
divan_cost = divan_quantity1 * divan_price
divan_code = goods['Диван']
divan_item = store[divan_code][1]
divan_quantity2 = divan_item['quantity']
divan_price = divan_item['price']
divan_cost1 = divan_quantity2 * divan_price
print('Диван -', divan_quantity2 + divan_quantity1, 'шт, стоимость', divan_cost + divan_cost1, 'руб')


# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






