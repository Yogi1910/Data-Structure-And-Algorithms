def is_anagram(str1, str2) -> bool:
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    str2_list = list(str2)

    for i in str1:
        if i in str2_list:
            str2_list.remove(i)
        else:
            return False

    if not str2_list:
        return True

    return False


print(is_anagram("triangle", "integral"))
