import pycorrector
import sys

def typo(strRceive): # 输入 变量text
    corrected_sent, detail = pycorrector.correct(strRceive)
    # print(corrected_sent)

    correctResult = list(corrected_sent)
    strResult = list(strRceive)
    # print(correctResult)
    # print(detail)

    cnt1 = 0
    cnt2 = 0
    for i in detail:
        # print(i)
        correctResult.insert(i[2] + cnt1, '(')
        cnt1 += 1
        correctResult.insert(i[3] + cnt1, ')')
        cnt1 += 1

        strResult.insert(i[2] + cnt2, '(')
        cnt2 += 1
        strResult.insert(i[3] + cnt2, ')')
        cnt2 += 1

    correctResult = "".join(correctResult)
    strResult = "".join(strResult)

    # print("The wrong words in the brackets: \n" + strResult + "\n")
    # print("After corrected: \n" + correctResult + "\n")
    # print(strResult)
    print(correctResult)

if __name__ == '__main__':
    typo(sys.argv[1]) # 接收命令行参数
    # strRceive = "下办啦，打卡成共"
    # typo(strRceive)