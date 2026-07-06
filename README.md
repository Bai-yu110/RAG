RAG-DS-Assistant/
├── app.py                  # 前端主入口（同学B负责）
├── requirements.txt        # 依赖库清单（全员共用）
├── README.md               # 项目说明书（同学D负责）
├── backend/                # 后端核心模块（同学A负责）
│   ├── __init__.py         # 标识这是一个Python包
│   ├── llm.py              # 封装大模型API
│   ├── vector_store.py     # 知识库读取与向量化
│   └── rag.py              # 最终的对外接口函数 ask()
├── knowledge/              # 规范知识库（同学C负责）
│   ├── 排序/
│   └── 树/
├── tests/                  # 测试模块（同学D负责）
│   └── questions.json      # 标准测试集
└── docs/                   # 报告与PPT（同学D负责）