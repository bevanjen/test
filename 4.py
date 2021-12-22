import decimal
from decimal import Decimal

while True:
	print('運算選項:\n(1)相加\n(2)相減\n(3)相乘\n(4)相除')
	operation = input('輸入你的選項(1/2/3/4): ')
	
	if operation == '1':
		number1 = Decimal(input('輸入第一個數字: '))
		number2 = Decimal(input('輸入第二個數字: '))
		number3 = number1 + number2
		number3 = Decimal(number3)
		print(number1, '+', number2, '=', number3)

	elif operation == '2':
		number1 = Decimal(input('輸入第一個數字: '))
		number2 = Decimal(input('輸入第二個數字: '))
		number3 = number1 - number2
		number3 = Decimal(number3)
		print(number1, '-', number2, '=', number3)

	elif operation == '3':
		number1 = Decimal(input('輸入第一個數字: '))
		number2 = Decimal(input('輸入第二個數字: '))
		number3 = number1 * number2
		number3 = Decimal(number3)
		print(number1, 'x', number2, '=', number3)

	elif operation == '4':
		number1 = Decimal(input('輸入第一個數字: '))
		number2 = Decimal(input('輸入第二個數字: '))
		number3 = number1 / number2
		number3 = float(number3)
		print(number1, '/', number2, '=', number3)

	else:
		print('超出選項範圍')
		break