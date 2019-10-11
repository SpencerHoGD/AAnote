import os
from os import path
from shutil import copyfile

#源文件夹
srcDir = r'\\192.168.106.201\风控中心综合体系\07、文件模板、函件、通讯\7.2 函件管理\2019年'
#目标文件夹
dstDir = r"D:\\copy_pdf"
#如果目录不存在，则创建
if not path.isdir(dstDir):
    os.makedirs(dstDir)
