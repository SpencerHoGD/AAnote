#! /usr/bin/env python3

# 以写入模式创建及打开txt文件，用while循环写入100万行文字，完成后打印出“工作完成”，关闭文件。
with open ('/tmp/0001ILoveLiyani100MillionTimes.txt', 'w') as f:
    spam = 0
    while spam < 1000000:
        f.write(' I Love Liyani ' +str(int(spam) + 1) + ' Times. \n')
        spam = spam + 1
    print("The job is done!")
    f.close

