# -*- coding: utf-8 -*-
from SimpleQIWI import *
token = raw_input('Введите токен: ')
phone = raw_input('Введите номер: ')
api = QApi(token=token, phone=phone)
print('''
1.Проверка баланса.
2.Перевод средств.
3.Выход ''')
while True:
	a= int(raw_input('Какое действие выполнить?:'))
	if a == 1:
		print(api.balance)
	if a == 2:
		phone2 = raw_input('Введите свой номер для перевода:')
		balanc = raw_input('Введите сумму:')
		#comm = input('Введите комментарий для перевода: ')
		api.pay(account=phone2, amount=balanc, comment='1')
		print(api.balance)
	if a == 3:
		quit()
else:
	print('''
		Тут могло быть много ошибок, до свидания!
		 ''')
