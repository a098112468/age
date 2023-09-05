drive = input('有開過車嗎?')
if drive != '有' and drive != '沒有':
	print('請輸入有或沒有')
	raise SystemExit

age = input('你的年齡是?')
age = int(age)

if drive == '有':
	if age >= 18:
		print('good')
	else:
		print('bad')

if drive == '沒有':
	if age >= 18:
		print('可以嘗試')
	else:
		print('還未成年')
