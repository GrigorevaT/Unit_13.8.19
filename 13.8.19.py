ticket = (int(input('Введите количество билетов:')))
count_1 = 0
count_2 = 0
count_3 = 0
price_1 = 0
price_2 = 0
price_3 = 0
for i in range(ticket):
   age = int(input('Введите ваш возраст:'))
   if age < 18:
      count_1 += 1
      price_1 = 0
   elif 18 <= age < 25:
      count_2 += 1
      price_2 = 990
   elif age >= 25:
      count_3 += 1
      price_3 = 1390
if ticket >= 3:
   S1 = (count_1 * price_1 + count_2 * price_2 + count_3 * price_3) - ((count_1 * price_1 + count_2 * price_2 + count_3 * price_3) * 10 / 100)
   print('Сумма к оплате:', S1)
else:
   S2 = (count_1 * price_1 + count_2 * price_2 + count_3 * price_3)
   print('Сумма к оплате:', S2)

