import random
start = input('輸入猜數字範圍下限')
end = input('請輸入猜數字範圍上限')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('請輸入數字')
	num = int(num)
	if num == r:
		print('恭喜猜對!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')
	print('這是你猜的第', count, '次')