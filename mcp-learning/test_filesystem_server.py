"""
测试官方 filesystem MCP 服务器
"""

import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

async def test_filesystem_server():
    """测试 filesystem 服务器"""

    # 配置 filesystem 服务器
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "D:\\code\\claude"]
    )

    try:
        async with stdio_client(server_params) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                # 初始化会话
                await session.initialize()

                print("=" * 60)
                print("成功连接到 Filesystem MCP 服务器!")
                print("=" * 60)

                # 1. 列出所有可用的工具
                print("\n可用的工具:")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")

                # 2. 列出所有可用的资源
                print("\n可用的资源:")
                resources = await session.list_resources()
                for resource in resources.resources[:10]:  # 只显示前 10 个
                    print(f"  - {resource.uri}")
                print(f"  ... (总共 {len(resources.resources)} 个资源)")

                # 3. 测试一个工具：列出文件
                print("\n测试工具 - 列出目录文件:")
                result = await session.call_tool("list_directory", {
                    "path": "mcp-learning"
                })
                if result.content:
                    print(f"  {result.content[0].text}")

                # 4. 测试读取资源
                print("\n测试资源 - 读取 README.md:")
                resource = await session.read_resource("file://mcp-learning/README.md")
                if resource.contents:
                    text = resource.contents[0].text
                    lines = text.split('\n')[:5]  # 只显示前 5 行
                    print("  前 5 行内容:")
                    for line in lines:
                        print(f"    {line}")

                print("\n" + "=" * 60)
                print("测试完成!")
                print("=" * 60)

    except Exception as e:
        print(f"\n错误: {e}")
        print("\n提示：如果遇到错误，可能需要:")
        print("1. 确保 Node.js 已安装")
        print("2. 网络连接正常（第一次运行需要下载服务器）")
        print("3. 路径 D:\\code\\claude 存在")

if __name__ == "__main__":
    asyncio.run(test_filesystem_server())
