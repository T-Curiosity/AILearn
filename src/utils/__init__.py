"""
工具函数模块
"""

import os
import logging
from typing import Any, Dict, List, Optional
import pandas as pd
import numpy as np
from pathlib import Path


def setup_logging(level: str = "INFO") -> None:
    """设置日志配置"""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ai_learn.log'),
            logging.StreamHandler()
        ]
    )


def load_config(config_path: str = ".env") -> Dict[str, str]:
    """加载环境配置"""
    from dotenv import load_dotenv
    load_dotenv(config_path)
    return dict(os.environ)


def save_results(data: Any, filepath: str, format: str = "json") -> None:
    """保存结果到文件"""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    if format == "json":
        import json
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    elif format == "csv":
        if isinstance(data, pd.DataFrame):
            data.to_csv(filepath, index=False)
        else:
            pd.DataFrame(data).to_csv(filepath, index=False)
    elif format == "pickle":
        import pickle
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)


def load_data(filepath: str) -> Any:
    """从文件加载数据"""
    filepath = Path(filepath)
    
    if filepath.suffix == ".csv":
        return pd.read_csv(filepath)
    elif filepath.suffix == ".json":
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif filepath.suffix in [".pkl", ".pickle"]:
        import pickle
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f"不支持的文件格式: {filepath.suffix}")


def create_experiment_dir(base_dir: str = "experiments") -> str:
    """创建实验目录"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = Path(base_dir) / f"exp_{timestamp}"
    exp_dir.mkdir(parents=True, exist_ok=True)
    return str(exp_dir)
