money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
growth = 1.05
delta = salary - spend
while money_capital + delta >= spend:
    money_capital += delta
    spend = spend * growth
    month += 1

# TODO Оформить решение

print(month)
