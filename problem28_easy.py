# 28.Implement strStr()

def strStr(haystack, needle):
    """
    :param haystack: string
    :param needle: string
    :return: position index
    """
    if len(haystack) < len(needle):
        return -1
    if len(needle) == 0:
        return 0
    for i in range(0, len(haystack)-len(needle)+1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1


strStr('hello', 'll')