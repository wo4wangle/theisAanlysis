#!/usr/bin/python
# -*- coding: gbk -*-

from gensim.models.doc2vec import Doc2Vec
from similar import similar
from textProcess import TextProcess
import sys


def similarity(text1, text2):

    List_Text = TextProcess(text1,text2)
    if List_Text == 0:
        print("Error")

    load_mod = Doc2Vec.load(r"/home/prouse/test.model")

    load_mod.random.seed(0)
    a_vec = load_mod.infer_vector(List_Text[0], alpha=0.001, epochs=50)
    load_mod.random.seed(0)
    b_vec = load_mod.infer_vector(List_Text[1], alpha=0.001, epochs=50)

    print(similar(a_vec, b_vec))


if __name__ == "__main__":
    # text1 = "ϰ��ƽ������ڻ��̽�¹����϶��ĺ�������в�����Աʱ˵����Щ����䡱"
    # text2 = "ϣ��˫��ý�����Ѻý����Ĵ����ߡ���ʵ�������ƶ��ߡ���г������������"
    similarity(sys.argv[1], sys.argv[2])
