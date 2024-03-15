data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  # count = count + 1
		if count % 1000 == 0:  # count / 1000的餘數
			print(len(data))  # 每1000筆以print產出進度
		
print('檔案讀取完了，總共有', len(data), '筆留言')  # 讀完100萬筆才會通知"共有100萬筆資料"
print(data[0])  #印出第一筆資料
print('----------------')
print(data[1])  #印出第二筆資料

sum_len = 0
for d in data:
	sum_len += len(d)  #sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data), '個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)  # append前面要是清單
print('一共有', len(new), '筆留言長度小於100個字')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言中有good的評論共有', len(good), '筆')
print(good[0])