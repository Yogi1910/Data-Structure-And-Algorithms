def palindrome_Check(string):
    string_cleaned = "".join(i.lower() for i in string if i.isalnum())
    string_reverse = string_cleaned[::-1]
    return string_reverse == string_cleaned


print(palindrome_Check("ABCBA"))


