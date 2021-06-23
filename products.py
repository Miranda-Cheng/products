products = []
while True:
	name = input('請輸入商品名稱: ')  # 已存成字串
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []    # 小清單，三行可以寫成 p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)   # 更簡潔可以寫成 products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:   # csv可以用excel打開
	f.write('商品,價格\n' )   # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # 字串相加

# 如果程式打開有亂碼，需用編碼(ecoding)來解決
# 最有名的是utf-8
# with open('products.csv', 'w', ecoding = 'utf-8') as f:
# 如果excel依然顯示亂碼，表示讀取有問題
# 到excel-從文字檔-選擇cvs檔案-選擇編碼、