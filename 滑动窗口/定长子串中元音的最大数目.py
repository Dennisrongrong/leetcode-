# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/5 10:42
@Auth ： 归去来兮
@File ：定长子串中元音的最大数目.py
@IDE ：PyCharm
@Motto:花中自幼微风起
"""
"""
给你字符串s和整数k 。
请返回字符串s中长度为k的单个子字符串中可能包含的最大元音字母数。
英文中的元音字母为（a, e, i, o, u）。
示例 1：
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
"""
s,k = "abciiidef",3
vowels={'a','e','i','o','u'}
cnt=0
for i in range(k):
    if s[i] in vowels:
        cnt+=1
res=cnt
for i in range(k,len(s)):
    if s[i] in vowels:
        cnt+=1
    if s[i-k] in vowels:
        cnt-=1
    res=max(res,cnt)
print(res)
