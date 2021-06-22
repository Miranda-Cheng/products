products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []    # 小清單，三行可以寫成 p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)   # 更簡潔可以寫成 products.append([name, price])
print(products)