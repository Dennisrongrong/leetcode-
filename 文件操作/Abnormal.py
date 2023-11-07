# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/7 12:48
@Auth ： 归去来兮
@File ：Abnormal.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print("%d"%(answer)+"")
