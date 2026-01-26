"""
我的第一个 MCP 服务器
使用 FastMCP - 一个更简单的高级 API
"""

from mcp.server.fastmcp import FastMCP
import json

# 创建 FastMCP 服务器实例
mcp = FastMCP("my-first-server")

# 定义一个工具 - 计算
@mcp.tool()
def calculate(operation: str, a: float, b: float) -> str:
    """执行基本的数学运算

    Args:
        operation: 运算类型 (add, subtract, multiply, divide)
        a: 第一个数字
        b: 第二个数字
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }

    if operation not in operations:
        return f"Error: Unknown operation '{operation}'"

    result = operations[operation](a, b)
    return f"计算结果: {a} {operation} {b} = {result}"

# 定义一个资源 - 服务器信息
@mcp.resource("uri://info")
def server_info() -> str:
    """返回服务器信息"""
    info = {
        "name": "My First MCP Server",
        "version": "1.0.0",
        "description": "一个简单的示例服务器，用于学习 MCP",
        "author": "MCP 学习者"
    }
    return json.dumps(info, ensure_ascii=False, indent=2)

# 运行服务器
if __name__ == "__main__":
    mcp.run()
