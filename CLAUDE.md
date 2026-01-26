# Claude 学习对话记录

## 📅 日期：2025-01-26

## 🎯 学习主题：深入理解 MCP 协议与官方服务器

---

## 📝 对话大纲

### 1. 环境准备
- 安装 Python 3.12
- 配置虚拟环境
- 安装 MCP SDK

### 2. 第一个 MCP 服务器
- 创建计算器服务器
- 理解 Tool 和 Resource
- 成功运行客户端-服务器通信

### 3. 核心概念理解
- MCP vs 普通 API 的区别
- Tool vs Resource 的使用场景
- stdio 通信方式

### 4. 配置官方 MCP 服务器
- filesystem 服务器
- fetch 服务器
- 测试验证

### 5. 深入分析
- FastMCP vs 低级别 API
- Tool vs Prompt 的区别
- Fetch 服务器源代码分析

---

## 🔑 关键知识点总结

### 1. MCP vs 普通 API

**MCP 的特点**：
- 使用 stdio（标准输入/输出）进行通信
- 进程间通信（IPC），不是网络通信
- 客户端启动服务器为子进程
- 通过 stdin/stdout 传递 JSON-RPC 消息
- 浏览器无法直接访问

**普通 API（Flask/FastAPI）**：
- 使用 HTTP 协议
- 网络通信
- 独立运行，监听端口
- 浏览器可以直接访问

### 2. Tool vs Resource vs Prompt

| 类型 | 用途 | 返回值 | 使用场景 | 判断标准 |
|------|------|--------|----------|----------|
| **Tool** | 可执行的功能 | 具体结果 | AI 自动调用 | 执行操作、有副作用、需要参数 |
| **Resource** | 静态/动态数据 | 数据内容 | AI 访问数据源 | 提供数据、只读操作、URI 友好 |
| **Prompt** | 预定义的提示模板 | 消息列表 | 用户主动选择 | 复杂工作流、需要步骤说明 |

### 3. FastMCP vs 低级别 API

**FastMCP**：
- 适合快速开发
- 自动处理签名、JSON Schema、调用
- 灵活性较低
- 适合简单工具

**低级别 API**：
- 适合复杂需求
- 完全控制每个细节
- 需要手动处理很多事
- 适合需要特殊逻辑的场景

### 4. Fetch 服务器的设计亮点

**为什么不用 FastMCP？**
1. 需要同时实现 Tool 和 Prompt
2. 需要 robots.txt 检查（前置验证）
3. 复杂的错误处理
4. 支持分页（start_index, max_length）

**Tool vs Prompt 的实现差异**：
- **Tool**：检查 robots.txt（AI 自动访问），使用 `user_agent_autonomous`
- **Prompt**：不检查 robots.txt（用户主动选择），使用 `user_agent_manual`

---

## 🤔 苏格拉底式学习过程

### 问题 1：MCP vs 普通 API 的区别？

**初始回答**：
- 有 HTTP 路由
- 通过调接口与客户端通信
- 不能用浏览器直接访问

**纠正过程**：
- 重新审视代码，发现没有 HTTP 路由
- 理解 stdio 通信方式
- 理解进程间通信 vs 网络通信

**最终理解**：
- ✅ MCP 使用 stdio（进程间通信）
- ✅ 客户端启动服务器为子进程
- ✅ 通过 stdin/stdout 传递 JSON-RPC 消息
- ✅ 浏览器无法直接访问

### 问题 2：Tool vs Resource 的使用场景？

**测试题目**：
1. 获取当前时间 - Tool ✅
2. 读取文件内容 - Tool → Resource（纠正）
3. 执行数据库查询 - Tool ✅
4. 获取数据库表列表 - Resource → Tool（纠正）
5. 计算两数之和 - Tool ✅

**判断框架**：
- ✅ 使用 Tool：执行操作、有副作用、需要参数
- ✅ 使用 Resource：提供数据、只读操作、URI 友好

### 问题 3：FastMCP vs 低级别 API？

**困惑**：思考题 1 就难倒了

**拆解过程**：
1. 对比代码量：FastMCP 简单，低级别 API 复杂
2. 理解自动化：FastMCP 自动处理签名、JSON Schema
3. 理解使用场景：FastMCP 适合快速开发，低级别 API 适合复杂需求

**最终理解**：
- ✅ 快速添加 10 个工具 → FastMCP 更划算
- ✅ 复杂需求（如 Fetch）→ 低级别 API

### 问题 4：Tool vs Prompt 的区别？

**初始困惑**：Prompt 不是提示词吗？

**理解过程**：
1. 传统 Prompt：用户输入的文本
2. MCP Prompt：服务器提供的预定义提示模板

**关键区别**：
- **Tool**：AI 调用，返回具体结果
- **Prompt**：用户主动选择，返回提示模板，AI 执行它

**测试结果**：
1. MCP Prompt 是什么？→ 服务器提供的预定义提示模板 ✅
2. Calculate 需要 Prompt 吗？→ 不需要（只要结果）✅
3. 计算器辅导用什么？→ Prompt（需要讲解过程）✅

---

## 💡 重要理解

### Tool vs Prompt 的本质区别

**Tool**：
```
用户: "10 + 5 等于多少？"
  ↓
AI: 调用 calculate Tool
  ↓
服务器: 返回 "15"
  ↓
AI: "10 + 5 = 15"
```

**Prompt**：
```
用户: 选择 "math_tutor" Prompt
  ↓
输入：operation="add", a=10, b=5
  ↓
服务器返回:
"""
你是一个数学老师。请讲解：
10 add 5 = ?
要求：...
"""
  ↓
AI: "加法是将两个数合并在一起..."
```

### MCP Prompt 的真正含义

**MCP Prompt ≠ 传统的提示词**

**MCP Prompt** = 服务器提供的**可重用的提示模板**
- 用户可以在 UI 中看到这些 Prompt
- 用户主动选择并填入参数
- 服务器返回预定义的消息列表
- AI 根据这个消息执行任务

---

## ✅ 学习成果

### 已完成
- [x] 创建第一个 MCP 服务器（calculate）
- [x] 理解 MCP vs 普通 API 的区别
- [x] 理解 Tool vs Resource vs Prompt
- [x] 配置官方 MCP 服务器（filesystem, fetch）
- [x] 分析 Fetch 服务器源代码
- [x] 理解 FastMCP vs 低级别 API

### 实践文件
- `mcp-learning/my_first_server.py` - 第一个 MCP 服务器
- `mcp-learning/test_client.py` - 测试客户端
- `mcp-learning/test_filesystem_server.py` - 测试 filesystem
- `mcp-learning/test_fetch_server.py` - 测试 fetch
- `.claude/mcp_servers.json` - MCP 服务器配置
- `.gitignore` - Git 忽略配置

### 待实践
- [ ] 为 calculate 服务器添加 Prompt 版本（math_tutor）
- [ ] 创建数据库操作 MCP 服务器
- [ ] 创建 API 集成 MCP 服务器

---

## 🎯 下一步计划

### 短期目标
1. 为 calculate 服务器添加 Prompt 版本
2. 实践 Tool vs Prompt 的区别

### 中期目标
1. 创建数据库操作 MCP 服务器
2. 创建 API 集成 MCP 服务器

### 长期目标
1. 学习 Agent Skills
2. 整合 MCP + Skills
3. 开发完整的应用

---

## 📚 参考资料

### 官方文档
- [MCP 官方文档](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP 文档](https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp/server/fastmcp)

### 学习资源
- Fetch 服务器源码：`.venv\Lib\site-packages\mcp_server_fetch\server.py`
- 官方服务器集合：https://github.com/modelcontextprotocol/servers

---

## 💭 学习反思

### 什么方法最有效？
1. **苏格拉底式提问** - 通过问题引导思考，而不是直接给答案
2. **对比学习** - 对比不同实现方式，理解设计权衡
3. **源代码分析** - 阅读真实的服务器代码，理解最佳实践

### 需要改进的地方
1. 对 Prompt 的理解需要加强（容易和传统提示词混淆）
2. 需要更多实践来巩固 Tool vs Resource vs Prompt 的判断

### 最大的收获
1. 理解了 MCP 的本质（进程间通信，不是 HTTP）
2. 理解了 Tool vs Prompt 的本质区别（AI 调用 vs 用户选择）
3. 理解了 FastMCP vs 低级别 API 的使用场景

---

## 📝 待解决的问题

### 剩余疑问
1. 如何在 Claude Code 中使用 Prompt？（还没实践过）
2. 低级别 API 的具体实现细节（需要更多练习）
3. 什么时候需要同时实现 Tool 和 Prompt？

### 下次学习重点
1. 实践：为 calculate 添加 Prompt 版本
2. 实践：在 Claude Code 中使用 Prompt
3. 深入：低级别 API 的使用

---

**学习时间**：约 2-3 小时
**学习方式**：苏格拉底式提问 + 实践 + 源代码分析
**学习效果**：从零基础到理解 MCP 核心概念 ✅
