# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/7 12:56
@Auth ： 归去来兮
@File ：Basic_Operation.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
# title = "Alice in Wonderland"
# print(title.split())



# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)
# words=contents.split()
# num_words=len(words)
# print("The file " + filename + " has about " + str(num_words) + " words.")

import json
# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)