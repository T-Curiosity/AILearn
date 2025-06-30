"""
Day 1: 环境搭建和基础概念
测试项目环境是否正确配置
"""

import sys
import os
from pathlib import Path

def test_python_version():
    """测试Python版本"""
    print(f"Python版本: {sys.version}")
    assert sys.version_info >= (3, 9), "Python版本需要3.9或更高"
    print("✓ Python版本检查通过")

def test_imports():
    """测试必要包是否正确安装"""
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} 导入成功")
    except ImportError:
        print("✗ NumPy 导入失败")
        
    try:
        import pandas as pd
        print(f"✓ Pandas {pd.__version__} 导入成功")
    except ImportError:
        print("✗ Pandas 导入失败")
        
    try:
        import matplotlib.pyplot as plt
        print("✓ Matplotlib 导入成功")
    except ImportError:
        print("✗ Matplotlib 导入失败")
        
    try:
        import sklearn
        print(f"✓ Scikit-learn {sklearn.__version__} 导入成功")
    except ImportError:
        print("✗ Scikit-learn 导入失败")

def test_project_structure():
    """测试项目结构"""
    project_root = Path(__file__).parent.parent.parent
    required_dirs = [
        "src",
        "data",
        "notebooks",
        "projects",
        "tests"
    ]
    
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"✓ {dir_name}/ 目录存在")
        else:
            print(f"✗ {dir_name}/ 目录不存在")

def main():
    """主函数"""
    print("=== AI学习项目环境检查 ===")
    print()
    
    test_python_version()
    print()
    
    print("检查依赖包...")
    test_imports()
    print()
    
    print("检查项目结构...")
    test_project_structure()
    print()
    
    print("=== 环境检查完成 ===")

if __name__ == "__main__":
    main()
