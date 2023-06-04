# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task_3.txt", "r") as file:
    temp_list = file.readlines()
    summa = 0
    purchase = []
    for price in temp_list:
        price = ''.join([i for i in price if i.isdigit()])
        if price == '':
            purchase.append(summa)
            summa = 0
        else:
            summa += int(price)
    purchase.append(summa)


three_most_expensive_purchases = sum(sorted(purchase)[-3:])
assert three_most_expensive_purchases == 202346
