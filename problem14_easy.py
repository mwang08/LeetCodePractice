# 14. Longest Common Prefix


def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        common_prefix = [""]
        for i in range(len(strs)-1):
            if i == 0 or common_prefix[i] == "":
                text1 = strs[i]
            else:
                text1 = common_prefix[i]
            text2 = strs[i+1]
            common_text = ""
            for j in range(min(len(text1), len(text2))):
                if text1[j] == text2[j]:
                    common_text += text1[j]
                else:
                    break
            common_prefix.append(common_text)
    return common_prefix[-1]


longestCommonPrefix(["caa","","a","acb"])