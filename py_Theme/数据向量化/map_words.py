import itertools

# 打开存储分好词的训练数据
f_data = open('e://cut.txt', 'r', encoding='utf-8')
# 打开存储高频词的映射数据
f_word_map = open('e://word_map.txt', 'r', encoding='utf-8')
# 定义训练样本和测试样本数
train_number = 40000
test_number = 10000
# 高频词映射字典
word_map = {}
# 定义主题映射
theme_map = {}
theme_index = itertools.count()

# 存放训练数据、训练标签、测试数据、测试标签的文件
f_train_data = open('e://train_data.txt', 'w', encoding='utf-8')
f_train_label = open('e://train_label.txt', 'w', encoding='utf-8')
f_test_data = open('e://test_data.txt', 'w', encoding='utf-8')
f_test_label = open('e://test_label.txt', 'w', encoding='utf-8')

while True:
    s = f_word_map.readline().strip()
    if s == '':
        break
    word, index = s.split(' ')
    word_map[word] = int(index)

print('映射表读入完毕')
f_word_map.close()

for k in range(train_number):
    s = f_data.readline().strip()
    i = s.find('\t')
    theme = s[: i]
    theme_label = theme_map.setdefault(theme, next(theme_index))
    f_train_label.write(str(theme_label))
    words = s[i + 1:].split()
    for word in words:
        if word in word_map:
            f_train_data.write(str(word_map[word]) + ' ')
    f_train_data.write('\n')
    print('已完成第', end='')
    print(k + 1, end='')
    print('条训练数据的处理')

f_train_data.close()
f_train_label.close()

k = itertools.count(1)
while True:
    s = f_data.readline().strip()
    if s == '':
        break
    i = s.find('\t')
    theme = s[: i]
    theme_label = theme_map.setdefault(theme, next(theme_index))
    f_test_label.write(str(theme_label))
    words = s[i + 1:].split()
    for word in words:
        if word in word_map:
            f_test_data.write(str(word_map[word]) + ' ')
    f_test_data.write('\n')
    print('已完成第', end='')
    print(next(k), end='')
    print('条测试数据的处理')

f_data.close()
f_test_data.close()
f_test_label.close()
