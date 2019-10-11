#! /usr/bin/env python
'''
Created on 2019-10-10
hexiaoming
'''

import os
from os import path
from shutil import copyfile

#源文件夹
srcDir = r'\\192.168.106.201\风控中心综合体系\07、文件模板、函件、通讯\7.2 函件管理\2019年'
#目标文件夹
dstDir = r"D:\\copy_pdf_from_DNS"
#如果目录不存在，则创建
if not path.isdir(dstDir):
    os.makedirs(dstDir)

def download_pdf(startDir):
    fileType = "pdf"
    #nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #filelistlog = path.join("D:\\fileListLog" + str(nowTime) + ".txt")  # 保存文件路径)
    #postfix = set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式
    for maindir, subdir, file_name_list in os.walk(srcDir):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            #if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
            if apath.split('.')[-1] = fileType:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                try:
                    #正在复制pdf文件
                    shutil.copyfile(srcDir, dstDir)
                except:
                    pass    # 所有异常全部忽略即可

    
if __name__ == '__main__':
    startDir = "E:"  # 指定根目录
    #startDir = r'\\192.168.106.201\风控中心综合体系'
    #startDir  = r'\\192.168.106.201\风控中心\监察部'  #监察部共享
    #startDir  = r'\\192.168.106.201\风控中心\审计部'  #审计部共享
    print('开始')
    all_path(startDir)
    print('完成')