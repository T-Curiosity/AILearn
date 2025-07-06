
def str_expamle():
    """字符串的基本使用"""
    # 字符串的定义
    str1 = "Hello, World!"
    str2 = 'Python is fun!'
    str3 = """This is a multi-line string.
    It can span multiple lines."""
    str4 = '''This is another multi-line string.
    It can also span multiple lines.'''

    # 打印字符串
    print("str1:", str1)
    print("str2:", str2)
    print("str3:", str3)
    print("str4:", str4)

    # 字符串的拼接
    str5 = str1 + " " + str2
    print("Concatenated string:", str5)

    # 字符串的重复
    str6 = str1 * 2
    print("Repeated string:", str6)

    # 字符串的长度
    print("Length of str1:", len(str1))

    # 常规字符操作
    # 长度
    print("Length of str2:", len(str2))
    print("Length of str3:", str3.__len__())
    # 索引 切片 遍历
    print("First character of str1:", str1[0])
    print("Last character of str2:", str2[-1])
    print("Characters from index 0 to 4 in str3:", str3[0:5])
    # 按步长切片
    print("Characters from index 0 to 10 with step 2 in str4:", str4[0:10:2])
    # 循环
    print("Characters in str1:")
    for char in str1:
        print(char, end=' ')
    # 去除白字符 含空格 \t \n \r
    str7 = "   Hello, Python!   \n \r"
    print("\nString with spaces:{", str7, "}")
    print("String without spaces: {", str7.strip(),"}")
    print("String without leading spaces: {", str7.lstrip(),"}")
    print("String without trailing spaces: {", str7.rstrip(),"}")
    # 字符串替换
    str8 = "Hello, Python!"
    str9 = str8.replace("Python", "World")
    print("Replaced string:", str9)
    # 切分
    str10 = "apple,banana,cherry"
    fruits = str10.split(",")
    print("Split string:", fruits)
    # 拼接
    str11 = " ".join(fruits)
    print("Joined string:", str11)
    # 大小写转换
    print("Uppercase str1:", str1.upper())
    print("Lowercase str2:", str2.lower())
    # 加法
    str12 = "Hello"
    str13 = "World"
    str14 = str12 + " " + str13
    print("Concatenated string using +:", str14)
    # 数乘
    str15 = "Repeat me! "
    str16 = str15 * 3
    print("Repeated string using *:", str16)
    # 重复元素统计
    str17 = "strawberry"
    count_r = str17.count("r")
    print("Count of 'r' in 'strawberry':", count_r)
    # 查找子字符串
    index_of_substring = str17.find("berry1")
    if index_of_substring != -1:
        print("Index of 'berry1' in 'strawberry':", index_of_substring)
    else:
        print("'berry1' not found in 'strawberry'")
    # 成员判断 in 函数使用
    if "berry1" in str17:
        print("'berry' is in 'strawberry'")
    else:
        print("'berry' is not in 'strawberry'")


def main():
    """主函数"""
    print("=== AI学习项目 - Day 04: str ===")
    str_expamle()

if __name__ == "__main__":
    main()

