'''

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde

Output:
e
Explanation:
'e' is the letter that was added.

'''



class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # method one 集合运算（考虑不到加入相同字母的情况）
        # return "".join(set(t). - set(s))


        # method two   一个蠢方法
        # dic = {}
        # for i in s:
        #     if i not in dic.keys():
        #         dic[i] = 1
        #     else:
        #         dic[i] = dic.get(i) + 1
        # for j in t:
        #     if dic.get(j) != t.count(j):
        #         return j

        # method three
        return list(collections.Counter(t)-collections.Counter(s))[0]
