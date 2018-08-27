import time

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('文件读取完了，共有', len(data), '份文件！')

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每份留言的平均长度为：', sum_len/ len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '份留言长度小于100')
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '份包含good的文件')
#good = [d for d in data if 'good' in d]

#文字计数
start_time = time.time()
wc = {}#word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key进字典

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')

print(len(wc))

while True:
	word = input('请问你想查什么字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现过的次数', wc[word])
	else:
		print('未出现过改字')
print('感谢查询')
	



