"""
Day 02: NumPy基础练习
需要先运行: uv add numpy
"""

import sys

def test_numpy_import():
    """测试NumPy是否安装"""
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} 导入成功")
        return np
    except ImportError:
        print("✗ NumPy 未安装")
        print("请运行: uv add numpy")
        sys.exit(1)

def array_creation_demo(np):
    """数组创建演示"""
    print("\n=== NumPy数组创建 ===")
    
    # 从列表创建
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"从列表创建: {arr1}")
    
    # 创建特殊数组
    zeros = np.zeros(5)
    ones = np.ones((2, 3))
    arange = np.arange(0, 10, 2)
    
    print(f"零数组: {zeros}")
    print(f"一数组:\n{ones}")
    print(f"等差数列: {arange}")

def array_operations_demo(np):
    """数组操作演示"""
    print("\n=== NumPy数组操作 ===")
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"原数组:\n{arr}")
    print(f"形状: {arr.shape}")
    print(f"数据类型: {arr.dtype}")
    
    # 索引和切片
    print(f"第一行: {arr[0]}")
    print(f"第二列: {arr[:, 1]}")
    
    # 数学运算
    print(f"数组 + 10:\n{arr + 10}")
    print(f"数组平方:\n{arr ** 2}")
    print(f"数组和: {np.sum(arr)}")
    print(f"每行和: {np.sum(arr, axis=1)}")

def broadcasting_demo(np):
    """广播机制演示"""
    print("\n=== 广播机制 ===")
    
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr1d = np.array([10, 20, 30])
    
    print(f"2D数组:\n{arr2d}")
    print(f"1D数组: {arr1d}")
    print(f"广播相加:\n{arr2d + arr1d}")

def practical_exercise(np):
    """实际练习"""
    print("\n=== 实际练习 ===")
    
    # 创建一个模拟数据集
    data = np.random.seed(42)  # 设置随机种子
    scores = np.random.randint(60, 100, (5, 3))  # 5个学生，3门课程
    
    print("学生成绩表 (5个学生，3门课程):")
    print(scores)
    
    # 统计分析
    print(f"\n每个学生平均分: {np.mean(scores, axis=1)}")
    print(f"每门课程平均分: {np.mean(scores, axis=0)}")
    print(f"最高分: {np.max(scores)}")
    print(f"最低分: {np.min(scores)}")
    print(f"标准差: {np.std(scores):.2f}")

def daily_summary():
    """每日总结"""
    print("\n=== Day 02 总结 ===")
    print("今天完成的内容:")
    print("1. ✓ NumPy环境配置")
    print("2. ✓ 数组创建方法")
    print("3. ✓ 数组索引和切片")
    print("4. ✓ 数学运算操作")
    print("5. ✓ 广播机制理解")
    print("6. ✓ 实际数据分析练习")
    print("\n明天学习计划: Pandas数据处理")

def main():
    """主函数"""
    print("=== AI学习项目 - Day 02: NumPy ===")
    
    np = test_numpy_import()
    array_creation_demo(np)
    array_operations_demo(np)
    broadcasting_demo(np)
    practical_exercise(np)
    daily_summary()
    
    print("\n🎉 Day 02 学习完成!")

if __name__ == "__main__":
    main()
