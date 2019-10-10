#! /usr/bin/env python
'''
Created on 2019-10-09
hexiaoming
'''

import os
from os import path
import datetime
import re


d = r'D:\work'  # 文件所在的文件夹路径
fileList = os.listdir(d)

nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
startDir  = r'\\192.168.106.201\风控中心\监察部\4. 监察方案'
filelistlog = path.join("D:\\fileListLog" + str(nowTime) + ".md")  # 保存文件路径)
print(filelistlog)