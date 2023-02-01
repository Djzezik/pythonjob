# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
sd.resolution  = (500, 500)
leftx, lefty = 0, 0
rightx, righty = 100, 50

leftx2, lefty2 = 50, 50
rightx2, righty2 = 200, 100
for _ in range (2):
    leftx = 0
    rightx = 200
    lefty += 50
    righty += 50

    leftx2 = 0
    rightx2 = 200
    lefty2 += 100
    righty2 += 100
    for _ in range(5):
        left_bottom = sd.get_point(leftx, lefty)
        right_top = sd.get_point(rightx, righty)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)
        leftx += 100
        #lefty += 50
        rightx += 100
        #righty += 50


        left_bottom2 = sd.get_point(leftx2, lefty2)
        right_top2 = sd.get_point(rightx2, righty2)
        sd.rectangle(left_bottom=left_bottom2, right_top=right_top2, width=2)
        leftx2 += 100
        # lefty += 50
        rightx2 += 100
        # righty += 50




sd.pause()