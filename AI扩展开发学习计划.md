# AI 扩展开发学习计划：MCP + Agent Skills

## 学习者档案
- **当前水平**: 了解基本概念，知道 MCP 的用途
- **学习目标**: 开发自己的 MCP 服务器和 Agent Skills
- **技术背景**: Python 开发者
- **学习方法**: 苏格拉底式学习法（通过提问引导思考）
- **学习节奏**: 每天晚上学习 1-2 小时
- **学习偏好**: 边实践边学习（项目驱动）
- **兴趣方向**: 数据库操作、API 集成

---

## 📖 核心概念对比：MCP vs Agent Skills

在开始学习之前，先理解这两个技术的定位和关系：

### MCP (Model Context Protocol)
**定位**：通用的 AI 助手扩展协议

**特点**：
- 🔌 **协议层**：标准化的通信协议，不绑定特定的 AI 助手
- 🏗️ **架构**：客户端-服务器模式（Client-Server）
- 🌐 **通用性**：任何支持 MCP 的 AI 助手都可以使用
- 📦 **核心要素**：
  - **Tools（工具）**：可执行的功能（如：计算、查询数据库）
  - **Resources（资源）**：静态或动态数据（如：文件内容、配置信息）
  - **Prompts（提示词）**：可重用的提示词模板（如：代码生成模板）

**使用场景**：
- 需要被多个不同的 AI 助手访问
- 需要提供复杂的数据和功能
- 需要标准化的接口

**示例**：
```
用户 → Claude/ChatGPT/Cursor → MCP 客户端 → MCP 服务器 → 数据库/API
```

---

### Agent Skills (Claude Code Skills)
**定位**：Claude Code CLI 的功能扩展

**特点**：
- 🛠️ **工具层**：Claude Code CLI 的插件系统
- 🎯 **特定性**：专门为 Claude Code 设计
- 💬 **交互性**：通过斜杠命令（如 `/commit`）调用
- 🎨 **灵活性**：可以调用 MCP 服务器、执行本地命令、处理复杂工作流

**使用场景**：
- 增强 Claude Code CLI 的功能
- 创建自定义的快捷命令
- 封装复杂的多步骤工作流
- 集成 MCP 服务器提供更友好的接口

**示例**：
```
用户 → Claude Code CLI → Agent Skill → (可选) MCP 服务器 → 外部服务
```

---

### 两者的关系与区别

| 维度 | MCP | Agent Skills |
|------|-----|--------------|
| **抽象层次** | 底层协议 | 高层接口 |
| **适用范围** | 所有 MCP 兼容的 AI 助手 | 仅 Claude Code CLI |
| **主要作用** | 提供数据和功能 | 提供交互和工作流 |
| **开发复杂度** | 较低（定义接口） | 较高（处理逻辑） |
| **部署方式** | 独立服务器 | Claude Code 配置 |
| **通信方式** | stdio/SSE/HTTP | 直接函数调用 |

**关键理解**：
- **MCP 是"做什么"**（What）：定义了数据和功能的接口
- **Skills 是"怎么做"**（How）：定义了用户交互和工作流
- **Skills 可以使用 MCP**：一个 Skill 可以调用多个 MCP 服务器来完成任务
- **它们互补而非竞争**：MCP 提供能力，Skills 提供体验

---

### 🍽️ 类比理解

想象你在一个餐厅：

- **MCP 服务器** = 厨房的后台系统
  - 提供食材（Resources）
  - 提供烹饪能力（Tools）
  - 提供菜谱模板（Prompts）
  - 任何餐厅都可以使用这个系统

- **Agent Skills** = 餐厅的前台服务员
  - 接待客人（用户交互）
  - 根据客人需求调用后台（MCP）
  - 组合多个菜品完成一顿大餐（工作流）
  - 只在这个特定餐厅工作

**完美的一餐** = 友好的服务员（Skills）+ 强大的厨房系统（MCP）

---

## 🗺️ 学习路径概览

我们将采用**并行学习、逐步整合**的方式：

### 📘 第一部分：MCP 基础（2-3周）
- 理解 MCP 核心概念
- 开发简单的 MCP 服务器
- 掌握 FastMCP SDK

### 📙 第二部分：Agent Skills 入门（1-2周）
- 理解 Skills 的工作原理
- 开发简单的 Skill
- 学习 Skill 的配置和调用

### 📗 第三部分：整合实践（3-4周）
- Skills 调用 MCP 服务器
- 开发完整的工具链
- 实际项目应用

### 📕 第四部分：高级主题（2-3周）
- 最佳实践
- 性能优化
- 部署和分发

---

## 📘 第一部分：MCP 基础（2-3周）

### ✅ 第一阶段：深入理解 MCP 核心概念

#### 已完成内容
- 创建了第一个 MCP 服务器（计算器示例）
- 理解了 Tool 和 Resource 的概念
- 成功运行了客户端-服务器通信

#### 📝 学习成果
- [x] 安装 Python 3.12 和 MCP SDK
- [x] 创建 FastMCP 服务器
- [x] 实现 Tool（calculate）
- [x] 实现 Resource（server_info）
- [x] 理解 stdio 通信方式

#### 🤔 需要回答的问题
1. **MCP vs 普通API**：MCP 服务器和 Flask/FastAPI API 有什么本质区别？
2. **Tool vs Resource**：什么时候用 Tool，什么时候用 Resource？
3. **AI 如何使用**：AI 助手如何知道该调用哪个工具、传什么参数？

#### 📋 下一步
- [ ] 思考并回答上述问题
- [ ] 扩展第一个服务器，添加新功能

---

### 🚧 第二阶段：MCP 协议详解与进阶开发

#### 学习目标
- 深入理解 MCP 的三种核心要素
- 掌握 FastMCP SDK 的高级特性
- 实现数据库操作和 API 集成服务器

#### 实践项目 A：数据库操作服务器

**项目目标**：创建一个可以操作 SQLite 数据库的 MCP 服务器

**功能需求**：
1. **Tools（工具）**：
   - `execute_query` - 执行 SQL 查询
   - `list_tables` - 列出所有表
   - `get_schema` - 获取表结构
   - `insert_data` - 插入数据
   - `update_data` - 更新数据

2. **Resources（资源）**：
   - `table://{table_name}` - 获取表内容
   - `schema://` - 获取数据库模式
   - `stats://` - 获取数据库统计信息

3. **Prompts（提示词）**：
   - `query_generator` - 根据自然语言生成 SQL
   - `data_analyzer` - 分析查询结果

**引导问题**：
1. **安全考虑**：
   - 如何防止 SQL 注入？
   - 是否应该允许 DROP TABLE 等危险操作？
   - 如何限制查询返回的行数？

2. **设计决策**：
   - "列出所有表"应该是 Tool 还是 Resource？
   - 表数据量大时如何处理分页？
   - 如何处理查询错误？

#### 实践项目 B：API 集成服务器

**项目目标**：封装一个或多个第三方 API（如天气、新闻、GitHub等）

**功能需求**：
1. **Tools**：
   - `fetch_weather` - 获取天气信息
   - `search_news` - 搜索新闻
   - `github_repo_info` - 获取 GitHub 仓库信息

2. **Resources**：
   - `weather://{city}` - 获取特定城市天气
   - `news://{category}` - 获取分类新闻
   - `cache://` - 查看已缓存的数据

3. **特性**：
   - 请求缓存
   - 错误重试
   - 速率限制
   - API 密钥管理

**引导问题**：
1. **缓存策略**：
   - 哪些数据应该缓存？缓存多久？
   - 如何处理缓存失效？
   - 如何清理旧缓存？

2. **错误处理**：
   - API 限流时如何处理？
   - 网络错误如何重试？
   - 如何向 AI 报告错误？

---

## 📙 第二部分：Agent Skills 入门（1-2周）

### 第三阶段：理解 Agent Skills

#### 学习目标
- 理解 Skills 的工作原理
- 掌握 Skills 的配置方式
- 开发自定义 Skills

#### 核心概念

**什么是 Skill？**
- Skills 是 Claude Code CLI 的可扩展功能模块
- 通过配置文件定义
- 可以调用 MCP 服务器、执行命令、处理复杂逻辑

**Skill 的组成部分**：
1. **元数据**：名称、描述、参数
2. **执行逻辑**：如何完成任务
3. **参数处理**：解析和验证用户输入
4. **结果呈现**：如何展示结果

#### 实践项目：创建第一个 Skill

**项目目标**：创建一个 `/db` Skill，用于简化数据库操作

**功能需求**：
- `/db query "SELECT * FROM users"` - 执行查询
- `/db tables` - 列出所有表
- `/db schema users` - 查看表结构
- `/db analyze` - 分析数据库

**实现方式**：
1. **方式1**：直接调用 MCP 数据库服务器
2. **方式2**：执行本地命令（如 sqlite3）
3. **方式3**：混合方式

**引导问题**：
1. **设计选择**：
   - 为什么用 Skill 而不是直接让 AI 调用 MCP？
   - Skill 提供了什么额外价值？

2. **用户体验**：
   - 如何设计命令参数？
   - 错误信息如何显示？
   - 如何提供帮助文档？

#### 实践项目：创建工作流 Skill

**项目目标**：创建一个多步骤的工作流 Skill

**示例：`/deploy` Skill**
1. 运行测试
2. 构建项目
3. 部署到服务器
4. 验证部署
5. 发送通知

**功能需求**：
- 支持自定义部署流程
- 每个步骤失败时的处理
- 进度显示
- 日志记录

**引导问题**：
1. **工作流设计**：
   - 如何定义步骤？
   - 如何处理步骤间的依赖？
   - 如何支持并行执行？

2. **错误恢复**：
   - 某个步骤失败后如何处理？
   - 是否支持重试？
   - 如何从断点恢复？

---

## 📗 第三部分：整合实践（3-4周）

### 第四阶段：Skills + MCP 整合

#### 学习目标
- 理解如何让 Skills 调用 MCP 服务器
- 设计完整的工具链
- 实现复杂的应用场景

#### 综合项目 1：智能数据库助手

**架构**：
```
用户
  ↓
Agent Skill (/dba)
  ↓
MCP 数据库服务器
  ↓
SQLite/PostgreSQL/MySQL
```

**功能**：
- 自然语言查询（Skill 调用 MCP 的 query_generator Prompt）
- 智能建议（基于数据库模式提供建议）
- 自动化任务（备份、优化、分析）

#### 综合项目 2：API 聚合平台

**架构**：
```
用户
  ↓
Agent Skill (/api)
  ↓
MCP API 网关服务器
  ↓
多个第三方 API（天气、新闻、GitHub等）
```

**功能**：
- 统一的接口访问多个 API
- 智能缓存和速率控制
- 数据转换和聚合
- 错误处理和重试

#### 综合项目 3：开发工具集

**组件**：
1. **MCP 服务器**：
   - Git 操作服务器
   - 文件分析服务器
   - 测试执行服务器

2. **Agent Skills**：
   - `/review` - 代码审查（调用多个 MCP 服务器）
   - `/refactor` - 代码重构
   - `/test` - 测试和覆盖率分析
   - `/docs` - 生成文档

---

## 📕 第四部分：高级主题（2-3周）

### 第五阶段：最佳实践与优化

#### 1. 安全性
- **MCP 层面**：
  - 认证和授权
  - 敏感数据保护
  - 输入验证

- **Skills 层面**：
  - 权限检查
  - 危险操作确认
  - 审计日志

#### 2. 性能优化
- **缓存策略**：
  - MCP 服务器端缓存
  - Skill 层缓存
  - 缓存失效策略

- **并发处理**：
  - 异步操作
  - 批量请求
  - 连接池

#### 3. 可观测性
- **日志记录**：
  - 结构化日志
  - 日志级别管理
  - 敏感信息过滤

- **监控指标**：
  - 请求计数
  - 响应时间
  - 错误率

#### 4. 部署和分发
- **MCP 服务器**：
  - 打包和发布
  - 版本管理
  - 配置管理

- **Agent Skills**：
  - 配置文件管理
  - 依赖管理
  - 文档和示例

---

## 📊 学习进度追踪

| 部分 | 阶段 | 状态 | 完成日期 | 主要收获 | 需要改进 |
|------|------|------|----------|----------|----------|
| MCP | 第一阶段 | ✅ 已完成 | 2025-01-25 | 创建了第一个 MCP 服务器 | 需要深入理解 Tool vs Resource |
| MCP | 第二阶段 | ✅ 已完成 | 2025-01-26 | 理解 FastMCP vs 低级别 API，配置官方服务器 | 需要更多实践 |
| Skills | 第三阶段 | 待开始 | | | |
| 整合 | 第四阶段 | 待开始 | | | |
| 高级 | 第五阶段 | 待开始 | | | |

---

## 📚 学习资源

### MCP 相关
- [MCP 官方文档](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP 文档](https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp/server/fastmcp)

### Agent Skills 相关
- [Claude Code 文档](https://docs.anthropic.com/claude-code)
- [Skills 配置指南](https://docs.anthropic.com/claude-code/skills)

---

## 📓 学习笔记

### 第一部分：MCP 基础笔记

#### 第一阶段：第一次实践 ✅

**已完成**：
- ✅ 创建计算器 MCP 服务器
- ✅ 理解 Tool 和 Resource 概念
- ✅ 成功运行客户端-服务器通信

**核心理解**：
- MCP 使用 stdio 进行通信（标准输入/输出）
- Tool 是可执行的功能，Resource 是数据
- FastMCP 提供了简单的装饰器语法

**待回答的问题**：
1. MCP 和普通 API 的区别？
2. Tool vs Resource 的使用场景？
3. AI 如何知道调用什么？

#### 第二阶段：深入理解 MCP 协议与官方服务器 ✅

**日期**：2025-01-26

**已完成**：
- ✅ 理解 MCP vs 普通 API 的本质区别
- ✅ 理解 Tool vs Resource vs Prompt 的区别
- ✅ 学习 FastMCP vs 低级别 API 的使用场景
- ✅ 配置并测试官方 MCP 服务器（filesystem, fetch）
- ✅ 分析 Fetch 服务器的源代码

**核心知识点**：

**1. MCP vs 普通 API**
- MCP 使用 stdio（进程间通信），不是 HTTP
- 客户端启动服务器为子进程
- 通过 stdin/stdout 传递 JSON-RPC 消息
- 浏览器无法直接访问 MCP 服务器

**2. Tool vs Resource vs Prompt**

| 类型 | 用途 | 返回值 | 使用场景 | 例子 |
|------|------|--------|----------|------|
| **Tool** | 可执行的功能 | 具体结果（字符串、数字等） | AI 自动调用 | calculate, fetch, execute_query |
| **Resource** | 静态/动态数据 | 数据内容 | AI 访问数据源 | file://config.json, database://tables |
| **Prompt** | 预定义的提示模板 | 消息列表（提示模板） | 用户主动选择 | code_review, math_tutor |

**判断标准**：
- ✅ 用 Tool：执行操作、有副作用、需要参数
- ✅ 用 Resource：提供数据、只读操作、URI 友好
- ✅ 用 Prompt：复杂工作流、需要步骤说明、用户主动触发

**3. FastMCP vs 低级别 API**

| API | 适用场景 | 优势 | 劣势 |
|-----|---------|------|------|
| **FastMCP** | 快速开发、简单工具 | 自动处理签名、JSON Schema、调用 | 灵活性较低 |
| **低级别 API** | 复杂需求、完全控制 | 可实现任何逻辑 | 需要手动处理细节 |

**FastMCP 自动帮你做**：
- 提取函数签名
- 生成 JSON Schema
- 注册工具到服务器
- 处理函数调用

**低级别 API 需要手动做**：
- 定义 BaseModel
- 手动注册工具
- 手动解析参数
- 处理错误和验证

**4. 已配置的 MCP 服务器**

| 服务器 | 命令 | 功能 | 状态 |
|--------|------|------|------|
| filesystem | npx | 文件系统操作（13个工具） | ✅ 已测试 |
| fetch | python | 获取网页内容 | ✅ 已测试 |
| git | npx | Git 操作 | ✅ 已配置 |
| brave-search | npx | 网页搜索（需 API Key） | ⚠️ 需配置 |

**5. Fetch 服务器的设计亮点**

**为什么不用 FastMCP？**
- 需要同时实现 Tool 和 Prompt
- 需要 robots.txt 检查（前置验证）
- 复杂的错误处理
- 支持分页（start_index, max_length）

**Tool vs Prompt 的差异**：
- **Tool**：检查 robots.txt（AI 自动访问），使用 `user_agent_autonomous`
- **Prompt**：不检查 robots.txt（用户主动选择），使用 `user_agent_manual`

**实践文件**：
- `mcp-learning/my_first_server.py` - 第一个 MCP 服务器
- `mcp-learning/test_client.py` - 测试客户端
- `mcp-learning/test_filesystem_server.py` - 测试 filesystem 服务器
- `mcp-learning/test_fetch_server.py` - 测试 fetch 服务器
- `.claude/mcp_servers.json` - MCP 服务器配置

**待实践**：
- [ ] 为 calculate 服务器添加 Prompt 版本（math_tutor）
- [ ] 创建数据库操作 MCP 服务器
- [ ] 创建 API 集成 MCP 服务器

### 第二部分：Agent Skills 笔记

### 第三部分：整合实践笔记

### 第四部分：高级主题笔记

---

## 🎯 下一步行动

### 当前任务
1. 🎯 **立即行动**：回答第一阶段的思考问题
2. 📝 **开始设计**：数据库操作 MCP 服务器的架构
3. 🚀 **开始编码**：实现第一个数据库工具

### 需要做的选择
1. **数据库选择**：
   - SQLite（简单，单文件）
   - PostgreSQL（功能强大）
   - MySQL（常见）

2. **功能优先级**：
   - A) 先实现基本查询功能
   - B) 先实现表结构查看
   - C) 先实现数据插入/更新

3. **学习方式**：
   - A) 我先设计，你帮我审查
   - B) 你给示例，我模仿学习
   - C) 并行进行，边做边学

---

## 💡 使用说明

这个学习计划会随着你的学习进度不断更新。每完成一个阶段，我们：
1. 回顾学习成果
2. 更新进度追踪表
3. 根据实际情况调整后续计划
4. 添加更多针对性的练习和资源

**核心理念**：
- **边做边学**：通过实践理解概念
- **苏格拉底式**：通过提问引导思考
- **循序渐进**：从简单到复杂
- **整合应用**：MCP 和 Skills 相互配合

记住：**学习不是线性的，遇到问题随时回溯，深入理解后再继续前进。**
