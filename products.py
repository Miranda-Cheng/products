# 檢查檔案在不在
import os

products = []
	# 不管疫開始檔案有沒有存在，等一下都要寫入，所以提出來寫

if os.path.isfile('products.csv'):
	print('yeah!找到檔案了!')
	#讀取檔案
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
		# split(',') 遇到,就切割
		# split切割完的結果是清單
		# strip() 去調換行(\n)符號
		# 如果出現讀取錯誤，須加上相同編碼
		# with open('products.csv', 'r', ecoding = 'utf-8') as f:
		# continue、break 只能在回圈內寫
		# continue 繼續: 掠過下面的程式,跑下一輪for loop,通常是寫在比較高的位置
else:
	print('找不到檔案......')
	# os = operating system(作業系統) = 電腦的政府
	# 相對路徑(與此程式檔相同路徑) :輸入檔名
	# 絕對路徑 :輸入地址
	# 要用再查

# 使用者輸入
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

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w') as f:   # csv可以用excel打開
	f.write('商品,價格\n' )   # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # 字串相加

	# 如果程式打開有亂碼，需用編碼(ecoding)來解決
	# 最有名的是utf-8
	# with open('products.csv', 'w', ecoding = 'utf-8') as f:
	# 如果excel依然顯示亂碼，表示讀取有問題
	# 到excel-從文字檔-選擇cvs檔案-選擇編碼、