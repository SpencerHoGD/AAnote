#! /usr/bin/env python3

with open ('/tmp/0001ILoveLiyani100MillionTimes.txt', 'w') as f:
    spam = 0
    while spam < 1000000:
        f.write(' I Love Liyani ' +str(int(spam) + 1) + ' Times. \n')
        spam = spam + 1
    print("The job is done!")
    f.close

