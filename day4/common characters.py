def common_characters(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    common = ""
    for char in str1:
        if char.lower() in str2.lower() and char not in common:
            common += char
    if common == "":
        return -1
    else:
        return common
str1 = "I like Python"
str2 = "Java is a very popular language"
print(common_characters(str1, str2))
