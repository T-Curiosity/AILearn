

def bool_example():
    """布尔类型示例"""
    a = True
    b = False
    print("a:", a, "Type:", type(a))
    print("b:", b, "Type:", type(b))

    # 布尔运算
    print("a and b:", a and b)  # 与运算
    print("a or b:", a or b)    # 或运算
    print("not a:", not a)      # 非运算

    # 布尔值的比较
    if a:
        print("a is True")
    else:
        print("a is False")

    # 作为整数运算
    print("a + 1 ", a + 1)  # True作为1处理
    print("b + 1 ", b + 1)  # False作为0处理

    # 捕获除数异常
    try:
        result = 10 / False
    except ZeroDivisionError:
        print("除数不能为零")


def main():
    """主函数"""
    print("=== AI学习项目 - Day 04: bool ===")
    bool_example()

if __name__ == "__main__":
    main()
