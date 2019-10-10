
# -*- coding: utf-8 -*-
# time: 2019-10-10 11:16

from collections import defaultdict
import os
from os import path

# 获取每个数据集的分类及数量
dataDir = r'D:\cnews'
with open(path.join(dataDir + '\\cnews.%s.txt') % data_type, 'r', encoding='utf-8') as f:
    content = [_.strip() for _ in f.readlines() if _.strip()]

print(content)