import asyncio

from copilot import CopilotClient


async def main():
    async with CopilotClient(mode="coding-agent") as client:
        async with await client.create_session(
            model="auto",
            tools={"available_tools": []},
        ) as session:
            response = await session.send_and_wait("What is 2 + 2?")

            if response and response.data.content:
                print("Copilot:", response.data.content)
            else:
                print("No text response received.")


if __name__ == "__main__":
    asyncio.run(main())
