"""
Day 03: Pandas基础练习
需要先运行: uv add pandas
"""

import sys
from pathlib import Path

def test_pandas_import():
    """测试Pandas是否安装"""
    try:
        import pandas as pd
        print(f"✓ Pandas {pd.__version__} 导入成功")
        return pd
    except ImportError:
        print("✗ Pandas 未安装")
        print("请运行: uv add pandas")
        sys.exit(1)

def dataframe_basics(pd):
    """DataFrame基础操作"""
    print("\n=== DataFrame基础 ===")
    
    # 创建DataFrame
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 9500, 11000]
    }
    
    df = pd.DataFrame(data)
    print("创建的DataFrame:")
    print(df)
    print(f"\n数据形状: {df.shape}")
    print(f"列名: {list(df.columns)}")
    print(f"数据类型:\n{df.dtypes}")

def data_selection_demo(pd):
    """数据选择演示"""
    print("\n=== 数据选择和过滤 ===")
    
    # 重新创建数据
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 9500, 11000]
    }
    df = pd.DataFrame(data)
    
    # 选择列
    print("选择name列:")
    print(df['name'])
    
    print("\n选择多列:")
    print(df[['name', 'salary']])
    
    # 条件过滤
    print("\n年龄大于30的员工:")
    print(df[df['age'] > 30])
    
    print("\n工资在9000-12000之间的员工:")
    print(df[(df['salary'] >= 9000) & (df['salary'] <= 12000)])

def statistical_analysis(pd):
    """统计分析"""
    print("\n=== 统计分析 ===")
    
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 9500, 11000]
    }
    df = pd.DataFrame(data)
    
    print("基础统计信息:")
    print(df.describe())
    
    print(f"\n平均年龄: {df['age'].mean():.1f}")
    print(f"平均工资: {df['salary'].mean():.0f}")
    print(f"工资中位数: {df['salary'].median()}")
    
    print("\n按城市分组统计:")
    city_stats = df.groupby('city')['salary'].agg(['mean', 'count'])
    print(city_stats)

def data_manipulation_demo(pd):
    """数据操作演示"""
    print("\n=== 数据操作 ===")
    
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 9500, 11000]
    }
    df = pd.DataFrame(data)
    
    # 添加新列
    df['bonus'] = df['salary'] * 0.1
    df['total_income'] = df['salary'] + df['bonus']
    
    print("添加新列后的数据:")
    print(df[['name', 'salary', 'bonus', 'total_income']])
    
    # 排序
    print("\n按工资降序排列:")
    print(df.sort_values('salary', ascending=False)[['name', 'salary']])

def file_operations_demo(pd):
    """文件操作演示"""
    print("\n=== 文件操作 ===")
    
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 9500, 11000]
    }
    df = pd.DataFrame(data)
    
    # 保存到CSV
    output_dir = Path("daily_training/day03_pandas")
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_file = output_dir / "sample_data.csv"
    
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"✓ 数据已保存到: {csv_file}")
    
    # 读取CSV
    df_loaded = pd.read_csv(csv_file)
    print(f"✓ 成功读取数据，形状: {df_loaded.shape}")

def daily_summary():
    """每日总结"""
    print("\n=== Day 03 总结 ===")
    print("今天完成的内容:")
    print("1. ✓ Pandas环境配置")
    print("2. ✓ DataFrame创建和基础操作")
    print("3. ✓ 数据选择和过滤")
    print("4. ✓ 统计分析功能")
    print("5. ✓ 数据操作(添加列、排序)")
    print("6. ✓ 文件读写操作")
    print("\n明天学习计划: 机器学习入门")

def main():
    """主函数"""
    print("=== AI学习项目 - Day 03: Pandas ===")
    
    pd = test_pandas_import()
    dataframe_basics(pd)
    data_selection_demo(pd)
    statistical_analysis(pd)
    data_manipulation_demo(pd)
    file_operations_demo(pd)
    daily_summary()
    
    print("\n🎉 Day 03 学习完成!")

if __name__ == "__main__":
    main()
