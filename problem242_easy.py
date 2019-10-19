# 242. Valid Anagram

from collections import Counter


def isAnagram(s, t):

    a = Counter(s)
    b = Counter(t)

    if a == b:
        return True
    else:
        return False



