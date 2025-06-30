# AI课程学习项目

这是一个用于AI课程学习的项目，包含每日训练和项目实践内容。

## 项目结构

```
AILearn/
├── pyproject.toml          # 项目配置和依赖管理
├── README.md              # 项目说明
├── .gitignore            # Git忽略文件
├── main.py               # 项目入口文件
├── daily_training/       # 每日训练
│   ├── day01_python_basic/     # 第1天: Python基础
│   ├── day02_numpy/            # 第2天: NumPy
│   ├── day03_pandas/           # 第3天: Pandas
│   └── ...
├── projects/            # 项目实践
├── src/                 # 源代码
├── tests/               # 测试代码
└── data/                # 数据文件
```

## 环境设置

本项目使用 [uv](https://github.com/astral-sh/uv) 进行Python包管理。

### 安装依赖

```bash
# 安装项目依赖
uv sync

# 添加新的依赖包
uv add package_name
```

### 运行每日训练

```bash
# 运行第一天的训练
uv run daily_training/day01_python_basic/main.py

# 运行其他天的训练
uv run daily_training/day02_numpy/main.py
```

## 学习计划

- 每日训练：包含理论学习、代码练习和测试
- 项目实践：综合应用所学知识
- 持续跟踪学习进度和效果

## 使用说明

1. 每天在对应的 `dayXX_topic/` 目录下进行学习
2. 使用 `uv run` 命令执行每日的训练脚本
3. 完成练习后提交代码到Git仓库