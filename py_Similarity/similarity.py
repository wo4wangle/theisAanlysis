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
    # text1 = "习近平总书记在会见探月工程嫦娥四号任务参研参试人员时说了这些“金句”"
    # text2 = "希望双方媒体做友好交往的传播者、务实合作的推动者、和谐共处的守望者"
    similarity(sys.argv[1], sys.argv[2])
