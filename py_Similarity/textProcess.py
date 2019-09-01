#!/usr/bin/python
# -*- coding: gbk -*-

import re

import jieba.posseg as pseg

def TextProcess(text1,text2):

    if text1 == "" or text2 == "":
        return 0
    try:
        row_text1 = re.sub(r"[^\w\u4e00-\u9fff]+"," ",text1)
        row_text2 = re.sub(r"[^\w\u4e00-\u9fff]+"," ",text2)
        a = []
        b = []
        for k in list(pseg.cut(row_text1)):
            a.append(k.word)
        for k in list(pseg.cut(row_text2)):
            b.append(k.word)

    except e:
        print(e)

    return [a,b]


if __name__ == "__main__":
    a = "建设粤港澳大湾区是立足全局和长远发展作出的重大谋划。作为我国开放程度最高、经济活力最强的区域之一，粤港澳大湾区在国家发展大局中具有重要战略地位。40年改革开放，粤港澳大湾区经济实力、区域竞争力显著增强，已具备建成国际一流湾区和世界级城市群的基础条件。按照规划纲要，粤港澳大湾区不仅要建成充满活力的世界级城市群、国际科技创新中心、“一带一路”建设的重要支撑、内地与港澳深度合作示范区，还要打造成宜居宜业宜游的优质生活圈，成为高质量发展的典范。推动粤港澳大湾区建设，有利于贯彻落实新发展理念，为我国经济创新力和竞争力不断增强提供支撑；有利于进一步深化改革、扩大开放，建立与国际接轨的开放型经济新体制，建设高水平参与国际经济合作新平台。"
    b = "这是习近平对广大新闻工作者提出的殷殷期望。近年来，从召开座谈会和新闻工作者面对面交流，到记者节向新闻工作者发贺信，再到多次深入新闻报道一线调研慰问，习近平一直关心着新闻工作者，关注着新闻舆论工作。秉承总书记的重要指示精神，新闻工作者们牢记使命，扎根基层、记录时代，创作出一个个有思想、有温度、有品质的作品。"
    print(TextProcess(a,b))