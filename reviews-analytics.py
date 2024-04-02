data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1  # count = count + 1
        # if count % 1000 == 0:  # count / 1000的餘數
            # print(len(data))  # 每1000筆以print產出進度
        
print('檔案讀取完了，總共有', len(data), '筆留言')  # 讀完100萬筆才會通知"共有100萬筆資料"
print(data[0])  # 印出第一筆資料

sum_len = 0
for d in data:
    sum_len += len(d)  # sum_len = sum_len + len(d)
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

# 文字計數
wc = {}  # word_count
for d in data:
    words = d.split()  # words變成一個清單中裝了很多的單字word
    for word in words:    # word 是一組字串
        if word in wc:
            wc[word] += 1  # 如果字典中有這個word,次數+1
        else:
            wc[word] = 1   # 如果沒有出現過，加入字典，次數初始設定1

print('留言中出現超過100萬次的單字和出現次數為：')
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])  # 印出這個單字word，並印出這個word key在字典中的次數value

print('留有中出現過的單字總共有：', len(wc), '個') # 字典長度=多少個key

while True:
    word = input('請問你要查詢的單字：')
    if word == 'q':    
        break
    if word in wc:
        print(word, '在留言中出現的次數為：', wc[word])
    else:
        print('這個字沒有出現過，請換單字查詢！')
print('感謝使用查詢功能！')    