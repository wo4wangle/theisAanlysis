import collections
import itertools
import jieba

# 打开停用词存储的txt文件
f_stop_words = open('e://stop_words.txt', 'r', encoding='utf-8')
# 保存训练文本的分词结果将存在这里
f_cut = open('e://cut.txt', 'w', encoding='utf-8')
# 打开训练文本存储的txt文件
f_news = open('e://news.txt', 'r', encoding='utf-8')
# 保存高频词的映射，用于训练文本的向量化
f_word_map = open('e://word_map.txt', 'w', encoding='utf-8')
# 保存停用词的集合
set_stop_words = set()

while True:
    # 用strip方法删去句末的换行符
    s = f_stop_words.readline().strip()
    if s == '':
        break
    else:
        # 将停用词写入字典set_stop_words
        set_stop_words.add(s)

# 停用词读入完成，及时关掉文件句柄
f_stop_words.close()
# 建立一个counter，用于统计词频，只保留前频率从高到低的前10000个词
word_freq_counter = collections.Counter()
c = itertools.count()

while True:
    line = f_news.readline()
    if line != '':
        i = line.find('\t')
        content = line[i + 1: -1]  # \t前面是主题，最后一个字符是换行符，只有中间是内容
        theme = line[: i]
        # 分词之后只保留非停用词
        cut_words = list(filter(lambda x: x not in set_stop_words, jieba.cut(content)))
        # 将词语更新至计数器
        word_freq_counter.update(cut_words)
        # 写入主题
        f_cut.write(theme)
        # 仍用制表符隔开
        f_cut.write('\t')
        # 将分词结果保留，之后向量化仍需使用
        f_cut.write(' '.join(cut_words))
        f_cut.write('\n')
        print('已完成第', end='')
        print(next(c), end='')
        print('条数据的处理')
    else:
        break

f_cut.close()
f_news.close()
c = itertools.count()
for word, _ in word_freq_counter.most_common(10000):
    i = next(c)
    f_word_map.write(word)
    f_word_map.write(' ')
    f_word_map.write(str(i))
    f_word_map.write('\n')
    print('已完成第', end='')
    print(str(i), end='')
    print('条高频词映射的写入')
