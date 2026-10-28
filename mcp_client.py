import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    # إعدادات تشغيل السيرفر تلقائياً بواسطة العميل
    # إعدادات تشغيل السيرفر تلقائياً بواسطة العميل باستخدام المسار الكامل
    server_params = StdioServerParameters(
        command=r"C:\Users\Elite\AppData\Local\Programs\Python\Python313\python.exe",
        args=["mcp_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # تهيئة الاتصال مع السيرفر
            await session.initialize()
            print(" Connected to MCP Server successfully!\n")

            # استعراض الأدوات المتوفرة في السيرفر
            tools_result = await session.list_tools()
            print("Available Tools:")
            for tool in tools_result.tools:
                print(f" - {tool.name}: {tool.description}")

            print("\n-----------------------------------\n")

            # اختبار أداة استعراض المجلدات (مثلاً استعراض المجلد الحالي)
            print("Testing 'list_directory' tool...")
            result = await session.call_tool("list_directory", {"dir_path": "."})
            print(result.content[0].text)

def main():
    asyncio.run(run_client())

if __name__ == "__main__":
    main()