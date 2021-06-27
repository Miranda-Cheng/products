# 檢查檔案在不在
import os

def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:				
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')  
		if name == 'q':
			break
		price = input('請輸入價格: ')
		p = []    
		p.append(name)
		p.append(price)
		products.append(p)   # 以這個def來說，他不知道products是什麼，需要伸手出去拿，於是我們把它變參數
	print(products)
	return products     # 回傳，重新存下來

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品,價格\n' )
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
	# 只是寫入檔案，不用回傳任何的值

# 寫 main_function(程式的進入點)
def main():
	filename = 'products.csv'  # 降低重複性
	if os.path.isfile(filename):
		print('yeah!找到檔案了!')
		products = read_file(filename)  # 有return,所以存成products
	else:		
		print('找不到檔案......')

	products = user_input(products) # 用products傳遞進去讓他跑，最後再存成products，覆蓋掉原本的products
	print_products(products)  # 沒有回傳
	write_file('products.csv', products)

main()