"""
测试官方 fetch MCP 服务器
可以获取网页内容，配合 AI 实现搜索和网页分析
"""

import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

async def test_fetch_server():
    """测试 fetch 服务器"""

    # 配置 fetch 服务器
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server_fetch"]
    )

    try:
        async with stdio_client(server_params) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                # 初始化会话
                await session.initialize()

                print("=" * 60)
                print("成功连接到 Fetch MCP 服务器!")
                print("=" * 60)

                # 1. 列出所有可用的工具
                print("\n可用的工具:")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")

                # 2. 测试 fetch 工具 - 获取网页内容
                print("\n测试工具 - 获取 GitHub README:")
                print("-" * 60)

                result = await session.call_tool("fetch", {
                    "url": "https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md"
                })

                if result.content:
                    content = result.content[0].text
                    lines = content.split('\n')[:20]  # 只显示前 20 行
                    print("前 20 行内容:")
                    for i, line in enumerate(lines, 1):
                        print(f"  {i:2d}. {line}")

                    print(f"\n... (总共 {len(content)} 字符)")

                print("\n" + "=" * 60)
                print("测试完成!")
                print("=" * 60)

    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        print("\n提示：如果遇到错误，可能需要:")
        print("1. 确保 Python 已安装")
        print("2. 网络连接正常")
        print("3. 第一次运行需要下载服务器包")

if __name__ == "__main__":
    asyncio.run(test_fetch_server())
