data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('文件读取完了，共有', len(data), '份文件！')

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