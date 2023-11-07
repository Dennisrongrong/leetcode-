# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/7 12:43
@Auth ： 归去来兮
@File ：File_Write.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
filename = 'programming.txt'
with open(filename,'w') as  file_object:
    file_object.write("I love programming")
    file_object.write("I love creating new games.")
    file_object.write("I love programming\n")
    file_object.write("I love creating new games.\n")
