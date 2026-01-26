# MCP 学习 - 第一次实践

## 运行步骤

### 1. 安装依赖（如果还没安装）
```bash
pip install mcp
```

### 2. 运行测试客户端
```bash
cd D:\code\claude\mcp-learning
python test_client.py
```

## 你会看到什么

- 成功连接到 MCP 服务器
- 列出可用的工具和资源
- 实际调用工具并看到结果
- 读取服务器资源

## 学习提示

运行代码后，不要急着继续下一步。先停下来思考：
- 服务器和客户端是如何通信的？
- 工具（Tool）和资源（Resource）有什么区别？
- 为什么需要用 JSON Schema 定义工具的输入？
