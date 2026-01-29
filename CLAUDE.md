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

---

## 📅 日期：2025-01-29 (第二天)

## 🎯 学习主题：Agent Skills 入门与 MCP + Skills 整合

---

## 📝 对话大纲

### 1. Agent Skills 学习
- 理解 Agent Skills 的概念
- 创建第一个 Agent Skill
- 测试 Skill 调用 MCP 服务器

### 2. MCP vs Agent Skills 深入对比
- 理解两者的本质区别
- 学习使用场景判断
- 理解 Vibe Coding 的工作原理

### 3. 实践项目
- 创建 calc.py Skill
- 测试成功调用 MCP 服务器
- 创建 Agent Skills 学习文档

---

## 🔑 关键知识点总结

### 1. Agent Skills 是什么？

**定义**：Agent Skills = Claude Code CLI 的可扩展功能模块

**本质**：
- Agent Skills = **可执行脚本**
- 可以是任何编程语言
- 可以调用 MCP 服务器
- 提供用户友好的接口

**与 MCP 的关系**：
- MCP = 后端（提供数据和功能）
- Skills = 前端（用户交互和工作流）
- Skills 可以调用 MCP

---

### 2. Agent Skills 调用 MCP 的完整流程

```
用户命令
  ↓
Agent Skill (可执行脚本)
  ↓
MCP 客户端（在 Skill 内部启动）
  ↓
MCP 服务器（通过 stdio 通信）
  ↓
返回结果
```

**关键代码**（calc.py）：
```python
async def call_calculate(operation: str, a: float, b: float):
    # 1. 创建 MCP 客户端
    server_params = StdioServerParameters(
        command="python",
        args=["my_first_server.py"]
    )

    # 2. 连接到服务器
    async with stdio_client(server_params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()

            # 3. 调用 Tool
            result = await session.call_tool("calculate", {
                "operation": operation,
                "a": a,
                "b": b
            })

            return result.content[0].text
```

**关键理解**：
- Agent Skill **本身就是**一个 MCP 客户端
- 和 test_client.py 本质相同
- 唯一区别是它被包装成可执行脚本

---

### 3. MCP vs Agent Skills 的使用场景

#### 使用 MCP 的场景（90%）

| 场景 | 例子 | 原因 |
|------|------|------|
| **需求不固定** | "搜索今天的科技新闻" | 每次需求不同，需要 AI 灵活调整 |
| **需要 AI 智能决策** | "分析这个代码" | AI 需要根据内容决定 |
| **简单查询** | "读取文件内容" | 直接调用更快 |
| **组合调用** | "获取网页 + 分析内容" | AI 可以动态组合 |

#### 使用 Agent Skills 的场景（10%）

| 场景 | 例子 | 原因 |
|------|------|------|
| **固定流程** | `/deploy` 部署应用 | 每次步骤都一样 |
| **重复性任务** | `/backup` 备份数据库 | 预定义的工作流 |
| **多步骤操作** | `/review` 代码审查 | 组合多个 MCP 调用 |
| **特殊权限控制** | `/prod_deploy` | 需要管理员权限 |

---

### 4. 实际调用路径对比

#### 场景：你说"10加5等于多少"

**路径 1：直接 MCP（我会用的）**
```
你："10加5等于多少"
  ↓
Claude AI（我）
  ↓
我看到 calculate MCP 服务器
  ↓
我启动 MCP 客户端
  ↓
调用 calculate Tool
  ↓
MCP 服务器返回："15"
  ↓
我告诉你："10加5等于15"

特点：
✅ 路径短（1 层）
✅ 我有完全控制
✅ 更快、更灵活
```

**路径 2：通过 Agent Skills（我不会用的）**
```
你："10加5等于多少"
  ↓
Claude AI（我）
  ↓
调用 calc.py Skill
  ↓
calc.py 启动 MCP 客户端
  ↓
调用 calculate Tool
  ↓
MCP 服务器返回："15"
  ↓
calc.py 输出结果
  ↓
我告诉你："10加5等于15"

特点：
❌ 路径长（2 层）
❌ 受限于 Skill 接口
❌ 更慢
```

**我的选择**：**直接调用 MCP** ✅

---

#### 场景：你说"部署应用"

**我会用的方式**：
```
你："部署应用"
  ↓
Claude AI（我）
  ↓
我看到有 /deploy Skill
  ↓
调用 deploy Skill
  ↓
Skill 内部：
  1. 运行测试
  2. 构建
  3. 部署
  4. 验证
  5. 发送通知
  ↓
返回结果
  ↓
我告诉你："部署成功"

特点：
✅ Skill 封装了复杂流程
✅ 我不需要关心细节
✅ 有更好的错误处理
```

---

### 5. 为什么新闻搜索用 MCP？

**你的疑问**："搜索当天关注的板块新闻"为什么都用 MCP？

**答案**：

| 原因 | 说明 |
|------|------|
| **需求不固定** | 今天科技，明天医疗，后天 AI |
| **需要 AI 决策** | 过滤广告、排序、总结 |
| **更灵活** | 我可以根据需求调整搜索策略 |
| **更直接** | 少一层，更快 |

**如果用 Skill**：
```
/search_tech_news
/search_medical_news
/search_ai_news
...需要无穷多个 Skill
```

**用 MCP**：
```
只需要一个 fetch + brave-search
我根据你的需求动态调用
```

---

### 6. Vibe Coding 时我用的技能

**问题**：Vibe Coding 时我用的是什么技能？

**答案**：**Claude Code CLI 内置能力 + MCP 服务器**

```
┌─────────────────────────────────┐
│  我的内置能力（90% 的时间）      │
│  - Read, Write, Edit            │
│  - Bash, Glob, Grep             │
│  - 理解、分析、解释             │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│  MCP 服务器（10% 的时间）       │
│  - filesystem (读写文件)        │
│  - fetch (获取网页)             │
│  - git (Git 操作)               │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│  Agent Skills（很少）           │
│  - /deploy (固定工作流)         │
└─────────────────────────────────┘
```

**例子**：

| 你的需求 | 我用的技能 |
|---------|-----------|
| "更新学习计划" | Read + Edit + Bash（内置） |
| "分析源代码" | Read + 理解能力（内置） |
| "获取网页内容" | fetch MCP |
| "部署应用" | deploy Agent Skill |

---

## ✅ 学习成果

### 已完成
- [x] 理解 Agent Skills 的概念
- [x] 创建第一个 Agent Skill（hello.py）
- [x] 创建调用 MCP 的 Skill（calc.py）
- [x] 成功测试 Skill 调用 MCP 服务器
- [x] 理解 MCP vs Agent Skills 的使用场景
- [x] 理解 Vibe Coding 的工作原理

### 实践文件
- `.claude/skills/hello.py` - 最简单的 Skill
- `.claude/skills/calc.py` - 调用 MCP 的 Skill
- `.claude/skills/math_tutor.py` - 数学辅导 Skill
- `.claude/skills/README.md` - Agent Skills 学习文档

### 测试结果
```bash
# 所有测试都成功！
python calc.py add 10 5      # 15.0
python calc.py multiply 7 6  # 42.0
python calc.py divide 20 4   # 5.0
```

---

## 🤔 核心理解

### 1. Agent Skills 的本质

**Agent Skill = 可执行脚本**
- 和任何 Python 脚本一样
- 可以调用 MCP 服务器
- 提供更友好的用户接口

**类比**：
- **MCP 服务器** = 厨房（提供烹饪能力）
- **Agent Skills** = 自动点餐机（用户友好的界面）
- **本质相同，但 Skills 更方便**

---

### 2. 什么时候用 MCP，什么时候用 Skills？

**判断标准**：

| 需求特点 | 使用 |
|---------|------|
| 每次都不一样 | MCP ✅ |
| 需要 AI 智能决策 | MCP ✅ |
| 简单查询 | MCP ✅ |
| 固定流程 | Skills ✅ |
| 重复性任务 | Skills ✅ |
| 复杂工作流 | Skills ✅ |

---

### 3. MCP → Agent Skills 的调用链路

**完整流程**：
```
用户："搜索今天的科技新闻"
  ↓
Claude AI
  ↓
决策：这个需求灵活，用 MCP
  ↓
调用 brave-search MCP
  ↓
调用 fetch MCP
  ↓
分析结果
  ↓
告诉用户
```

**如果用 Skills**：
```
用户："搜索今天的科技新闻"
  ↓
Claude AI
  ↓
调用 /search_news Skill
  ↓
Skill 内部：
  - 调用 brave-search MCP
  - 调用 fetch MCP
  - 过滤、排序
  ↓
返回给 Claude AI
  ↓
告诉用户
```

**区别**：
- **MCP**：我直接控制每个步骤
- **Skills**：Skill 控制流程，我只需调用

---

## 💡 重要理解

### Agent Skills 不是用来替代 MCP 的

**正确的理解**：
- **MCP 提供能力**（数据和功能）
- **Skills 提供体验**（交互和工作流）
- **Skills 可以调用 MCP**
- **它们互补而非竞争**

### 类比：开车 vs 出租车

**直接 MCP（我自己开车）**：
- 我控制一切
- 我决定路线
- 我处理所有细节
- 适合：灵活、简单的场景

**通过 Agent Skills（坐出租车）**：
- 司机（Skill）控制一切
- 我告诉目的地
- 司机处理细节
- 适合：复杂、不熟悉的场景

---

## 📝 待实践的任务

### 短期
- [ ] 创建更复杂的 Agent Skills
- [ ] 学习 Skills 的错误处理
- [ ] 实践 Skills 调用多个 MCP

### 中期
- [ ] 创建数据库操作 MCP 服务器
- [ ] 创建对应的 Agent Skills
- [ ] 实现完整的工具链

### 长期
- [ ] 开发生产级的应用
- [ ] 整合 MCP + Skills
- [ ] 分享到社区

---

## 🎓 今天的学习心得

### 最大的收获

1. **理解了 Agent Skills 的本质**
   - 就是可执行脚本
   - 可以调用 MCP
   - 提供简化的接口

2. **理解了 MCP vs Skills 的使用场景**
   - 灵活需求 → MCP
   - 固定流程 → Skills

3. **理解了 Vibe Coding 的工作原理**
   - 主要用内置能力
   - 有时用 MCP
   - 很少用 Skills

### 需要改进的地方

1. **实践还不够**
   - 需要创建更多 Skills
   - 需要实践调用多个 MCP

2. **对 Claude Code 的配置理解不够**
   - Skills 如何在 CLI 中注册
   - 如何通过 `/command` 调用

3. **复杂工作流的设计**
   - 如何设计多步骤的 Skill
   - 如何处理错误和重试

---

## 📚 参考资料

### Agent Skills
- `.claude/skills/README.md` - Agent Skills 学习文档
- `calc.py` - 调用 MCP 的 Skill 示例

### 学习对话
- 今天的完整对话（已记录）

---

**学习时间**：约 1 小时
**学习方式**：实践 + 对话 + 苏格拉底式提问
**学习效果**：理解 Agent Skills 的概念和使用场景 ✅
