"""
测试客户端 - 用于测试我们的 MCP 服务器
"""

import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

async def test_server():
    """连接并测试服务器"""

    # 连接到服务器（使用绝对路径）
    import os
    server_path = os.path.join(os.path.dirname(__file__), "my_first_server.py")
    server_params = StdioServerParameters(
        command="python",
        args=[server_path]
    )

    async with stdio_client(server_params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            # 初始化会话
            await session.initialize()

            print("=" * 50)
            print("成功连接到 MCP 服务器!")
            print("=" * 50)

            # 1. 列出所有可用的工具
            print("\n可用的工具:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # 2. 列出所有可用的资源
            print("\n可用的资源:")
            resources = await session.list_resources()
            for resource in resources.resources:
                print(f"  - {resource.uri}")

            # 3. 调用计算工具
            print("\n测试计算工具:")
            result = await session.call_tool("calculate", {
                "operation": "add",
                "a": 10,
                "b": 5
            })
            print(f"  10 + 5 = {result.content[0].text}")

            result = await session.call_tool("calculate", {
                "operation": "multiply",
                "a": 7,
                "b": 6
            })
            print(f"  7 × 6 = {result.content[0].text}")

            # 4. 读取资源
            print("\n读取服务器信息资源:")
            resource = await session.read_resource("uri://info")
            print(f"  {resource.contents[0].text}")

            print("\n" + "=" * 50)
            print("测试完成!")
            print("=" * 50)

if __name__ == "__main__":
    asyncio.run(test_server())
