

# 浮点数的定义
def float_example():
    score = 95.5
    print('type 95.5 is :', type(score))
    num = 12345678901234567890123456789099999999999999.9999999999999
    print("type long float number is ", type(num))
    print(num)
    distance = 1.5e-4  # 科学计数法表示
    print("distance in scientific notation:", distance)

# 浮点数的运算
def float_operations():
    a = 5.5
    b = 2.2
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)

    # 浮点数的比较
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")

    # 乘方 开N次方
    import math
    print("a ** 2 =", a ** 2)  # 乘方
    print("Square root of a =", a ** (1 / 2))  # 开平方
    print("Square root of a =", a ** (1 / 3))  # 开3次方

    # 指数和对数
    print("Exponential of a =", math.exp(a))  # 指数
    print("Logarithm of a (base e) =", math.log(a))
    print("Logarithm of a (base 10) =", math.log10(a))
    print("Logarithm of a (base 2) =", math.log2(a))

    # 类型转换
    print("Convert a to int:", int(a))  # 转换为整数
    print("Convert a to float:", float(a))  # 转换为浮点数
    print("Convert a to string:", str(a))  # 转换为字符串
    print("Convert '3.14' to float:", float('3.14'))  # 字符串强转为float

    # 取整
    print("Floor of a:", math.floor(a))  # 向下取整
    print("Ceil of a:", math.ceil(a))  # 向上取整
    print("Convert a to int:", int(a)) # 截断取整 正整数时同向下取整 小数时 同向上取整..
    print("Round a to nearest integer:", round(a,0))  # 四舍五入

    # 比较
    print("Is a equal to b?", a == b)
    print("Is a not equal to b?", a != b)
    # 精度的比较
    a = 1 - 0.55
    print("(1-0.55) == 0.45 ?", a == 0.45)
    print("using fabs to compare float :", math.fabs(a - 0.45) < 1e-6)  # 使用绝对误差判断浮点数相等


def main():
    """主函数"""
    print("=== AI学习项目 - Day 03: float ===")
    float_example()
    float_operations()

if __name__ == "__main__":
    main()

