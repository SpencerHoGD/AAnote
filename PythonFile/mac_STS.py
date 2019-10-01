#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-09-09
hexiaoming
'''
import os

#file = '/Users/hexiaoming/Documents'

with open('/tmp/test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')

with open('/tmp/test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} had just been deleted.')
else:
    print(f'{f.name} does not exists.')
