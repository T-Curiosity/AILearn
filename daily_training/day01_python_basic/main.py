"""
Day 01: Python基础练习和环境测试
使用 uv run 命令执行
"""

import sys
from pathlib import Path

def test_environment():
    """测试环境配置"""
    print("=== AI学习项目 - Day 01 ===")
    print(f"Python版本: {sys.version}")
    print(f"当前工作目录: {Path.cwd()}")
    print("✓ 环境测试通过\n")

def python_basic_review():
    """Python基础回顾"""
    print("=== Python基础回顾 ===")
    
    # 数据类型
    print("1. 数据类型:")
    numbers = [1, 2, 3, 4, 5]
    text = "Hello, AI Learning!"
    data = {"name": "AI学习者", "day": 1}
    print(f"列表: {numbers}")
    print(f"字符串: {text}")
    print(f"字典: {data}\n")
    
    # 控制流
    print("2. 控制流:")
    for i, num in enumerate(numbers, 1):
        if num % 2 == 0:
            print(f"第{i}个数字 {num} 是偶数")
        else:
            print(f"第{i}个数字 {num} 是奇数")
    print()
    
    # 函数
    print("3. 函数练习:")
    result = calculate_sum(numbers)
    print(f"数列和为: {result}")
    print()

def calculate_sum(numbers):
    """计算数列和"""
    return sum(numbers)

def file_operation_demo():
    """文件操作演示"""
    print("=== 文件操作 ===")
    
    # 创建练习文件
    practice_file = Path("daily_training/day01_python_basic/practice_output.txt")
    practice_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(practice_file, 'w', encoding='utf-8') as f:
        f.write("Day 01 Python基础练习完成!\n")
        f.write(f"完成时间: {Path(__file__).stat().st_mtime}\n")
    
    print(f"✓ 已创建练习文件: {practice_file}")
    
    # 读取文件
    with open(practice_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"文件内容:\n{content}")

def daily_summary():
    """每日总结"""
    print("=== Day 01 总结 ===")
    print("今天完成的内容:")
    print("1. ✓ 环境配置测试")
    print("2. ✓ Python基础语法回顾")
    print("3. ✓ 数据类型操作")
    print("4. ✓ 控制流练习")
    print("5. ✓ 函数定义和调用")
    print("6. ✓ 文件操作")
    print("\n明天学习计划: NumPy数组操作")

def main():
    """主函数"""
    test_environment()
    python_basic_review()
    file_operation_demo()
    daily_summary()
    print("\n🎉 Day 01 学习完成!")

if __name__ == "__main__":
    main()
