# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/7 12:53
@Auth ： 归去来兮
@File ：alice.py.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
# filename = 'alice.txt'
# with open(filename) as f_obj:
#  contents = f_obj.read()


filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)