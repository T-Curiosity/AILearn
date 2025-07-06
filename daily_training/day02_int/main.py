

def declare_variables():
    score=100
    print('type 100 is :', type(score))

    num = 999999999999999999999999999999999999999999999
    print("type long number is " ,type(num))
    print(num)

def func_add(a, b):
    return a + b
def func_subtract(a, b):
    return a - b
def func_multiply(a, b):
    return a * b
def func_divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

#乘方
def func_power(a, b):
    return a ** b
# 开N次方
def func_nth_root(a, n):
    if n == 0:
        raise ValueError("n不能为零")
    return a ** (1 / n)

#指数
def func_exponential(a):
    import math
    return math.exp(a)
#对数
def func_logarithm(a, base=10):
    import math
    if a <= 0:
        raise ValueError("对数的输入必须大于零")
    return math.log(a, base)

# 类型转换
def convert_to_int(value):
    """将值转换为整数"""
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"无法将 {value} 转换为整数")
def convert_to_string(value):
    """将值转换为字符串"""
    return str(value)

# 比较

def test_operations():
    print("3 + 4 = ", func_add(3, 4))
    print("10 / 2 =",func_subtract(10, 5))
    print("2 * 3 = ",func_multiply(2, 3))
    print("8 / 3 = ",func_divide(8, 3))

    print("2 ** 3 = ",func_power(2, 3))
    print("27 nth root 3 = " , func_nth_root(27, 2))

    print("e^2 = ", func_exponential(2))
    print("log(100, 10) = ", func_logarithm(100, 10))

    print("Convert 123 to int:", type(convert_to_int("123")))
    print("Convert 456 to string:", type(convert_to_string(456)))

    print("Comparing 5 and 10:", "5 < 10 is", 5 < 10)
    print("Comparing 10 and 5:", "10 > 5 is", 10 > 5)
    print("Comparing 5 and 5:", "5 == 5 is", 5 == 5)
    print("Comparing 5 and 10:", "5 >= 10 is", 5 >= 10)


def main():
    """主函数"""
    print("=== AI学习项目 - Day 02: int ===")

    declare_variables()
    test_operations()


if __name__ == "__main__":
    main()

