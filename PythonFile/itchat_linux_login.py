#! /usr/bin/env python3
#encoding:utf-8

import itchat

itchat.auto_login(enableCmdQR = 2)
#itchat.run()
itchat.send('Hello, filehelper', toUserName = 'filehelper')
