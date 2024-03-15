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