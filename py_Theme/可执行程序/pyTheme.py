from jieba import cut
from keras.models import load_model
import sys
import numpy as np


# 将句子序列向量化
def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


#获得主题，必须将word_map.txt和theme_model.h5文件与本脚本放在同一路径
def get_theme(str_accept):
    word_map = {}
    f_word_map = open(sys.path[0] + '\\word_map.txt', 'r', encoding='utf-8')
    # 读入高频词并建立映射字典
    while True:
        s = f_word_map.readline()
        if s == '':
            break
        word, index = s.strip().split()
        word_map[word] = int(index)
    f_word_map.close()
    # 载入训练好的模型
    model = load_model(sys.path[0] + '\\model.h5')
    # 主题映射字典
    themes = ['时政', '财经', '游戏', '体育', '房产',
              '教育', '科技', '娱乐', '时尚', '家居']
    # 将输入分割
    cut_input = [list(map(lambda x: word_map[x],
                 filter(lambda x: x in word_map, cut(str_accept))))]
    vector_input = vectorize_sequences(cut_input)
    prediction = model.predict(vector_input)[0]
    _, p = max((prediction[i], i) for i in range(len(prediction)))
    print(themes[p])


if __name__ == '__main__':
    get_theme(sys.argv[1])
