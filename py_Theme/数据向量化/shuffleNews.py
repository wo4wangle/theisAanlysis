import random

orig = open('e://cnews.train.txt', 'r', encoding='utf-8')
shuffled = open('e://news.txt', 'r', encoding='utf-8')
arr = []

while True:
    s = orig.readline()
    if s != '':
        arr.append(s)
    else:
        break
        
orig.close()
random.shuffle(arr)

for i in arr:
    shuffled.write(i)

shuffled.close()
