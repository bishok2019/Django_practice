# 1.Find the Largest Number in a List
a = [2,12,23,4,5,12,]
# largest = a[100]
# for value in a:
#     if value > largest:
#         largest = value

# print(largest)

a.sort()
print(a)
b = a[::-1]
print(b)

# 2.Reverse a List Without Using In-Built Functions'
# a = [1,2,3,4,5,6,0,'a']
# b=[1,2,3,0,5,4,'z']
# d=b[::-1]
# print(d)
# print(f'reverse:{d}')

# c=max(a)
# a.sort()
# print(a)
# c=sorted(b)
# print(c)

# 3.Count Word Frequency in a Sentence
# sentence = " Ohh! Jingle bell jingle bell, Jingle all the way"
# split_word = sentence.split()
# word = []
# print('aaaaa',split_word)
# for i in split_word:
#     # if i not in word:
#         word.append(i)

# print(word)

# for i in range(0, len(word)):
#     print("frequency of '",word[i], "' is:", sentence.count(word[i]))

# set_word=set(word)
# final = list(set_word)

# print('set_word',set_word)
# print(final)
# for i in range(0, len(final)):
#       print("frequency of '",final[i], "'is:", sentence.count(word[i]))

# 4.Print Unique Letters from a String Without Using In-Built Functions

# a = 'bishokkkk'
# b=[]
# for i in a:
#       if i not in b:
#             b.append(i)
# print(b)

# 5.Generate a Fibonacci Sequence
# n = int(input("enter nth term: "))
# a = 0
# b = 1
# c = b
# if n<0:
#     print("Error ")
# while 0 <= n:
#     print(c)
#     n -= 1
#     a, b = b ,c 
#     c = a+b
# print()
######################################################
# a = [0,1,2,3,4,5,6,7]
# b = [9,10]
# c= a+b
# print(c)
# print(a[0:2])
# dicti= {2:1,1:'a','c':3}
# print(dict)
# b.extend([11,12])
# b.update([11,12])
# print(b)
# dicti['c']=4
# print(dicti.get('c'))

# for x, y in dicti.items(): # print all key with values
#     print(x,y)

# for x in dicti: # print all the key
#     print(x)

# for x in dicti: # get all the values
#     print(dicti[x])

# print(dicti.get('a')) #get value with key 

# print([key for key,val in dicti.items() if val=='a']) #get key with value

# class Solution:
#     def intToRoman(self, num):
#         val = [
#             (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
#             (1, 'I')
#         ]
#         roman_numeral =""
#         for i,r in val:
#             while num >= i:
#                 roman_numeral  += r
#                 print(roman_numeral)
#                 num -= i
#                 print(num)
#         return roman_numeral

# n = int(input("Enter an integers: "))
# result = Solution().intToRoman(n)
# print(result)