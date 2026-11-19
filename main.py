import asyncio
import random
import sys

from copilot import CopilotClient
from copilot.session import PermissionHandler
from copilot.session_events import SessionEventType
from copilot.tools import define_tool
from pydantic import BaseModel, Field


class GetWeatherParams(BaseModel):
    city: str = Field(description="The name of the city to get weather for")


@define_tool(description="Get the current weather for a city")
async def get_weather(params: GetWeatherParams) -> dict:
    city = params.city

    # In a real app, this would call a weather API.
    conditions = ["sunny", "cloudy", "rainy", "partly cloudy"]
    temperature = random.randint(50, 80)
    condition = random.choice(conditions)

    return {
        "city": city,
        "temperature": f"{temperature}°F",
        "condition": condition,
    }


async def main():
    async with CopilotClient(mode="coding-agent") as client:
        async with await client.create_session(
            model="auto",
            permissions={
                "on_request": PermissionHandler.approve_all,
            },
            events={
                "streaming": True,
            },
            tools={
                "definitions": [get_weather],
            },
        ) as session:
            def handle_event(event):
                if event.type == SessionEventType.ASSISTANT_MESSAGE_DELTA:
                    sys.stdout.write(event.data.delta_content)
                    sys.stdout.flush()

                if event.type == SessionEventType.SESSION_IDLE:
                    print()

            unsubscribe = session.on(handle_event)

            try:
                await session.send_and_wait(
                    "What's the weather like in Seattle and Tokyo?"
                )
            finally:
                unsubscribe()


if __name__ == "__main__":
    asyncio.run(main())
