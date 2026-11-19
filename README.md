# Copilot SDK Learning Lab

A hands-on Python learning repository that follows the [official GitHub Copilot SDK quickstart](https://docs.github.com/en/copilot/get-started/sdk-quickstart).

The project progresses incrementally through the five official quickstart stages. `main.py` preserves the completed Step 4 custom-tool and streaming example, while `weather_assistant.py` implements Step 5 as an interactive weather assistant.

## What This Project Demonstrates

- Creating and cleaning up a Copilot SDK client
- Creating a conversation session
- Sending prompts asynchronously
- Streaming assistant response text
- Defining a custom tool with Pydantic
- Passing tool definitions and session options to SDK 2.0.1
- Maintaining one session across multiple terminal prompts
- Handling normal exits as well as `Ctrl+C` and `Ctrl+D`

## The Examples

| File | Purpose |
| --- | --- |
| [`main.py`](main.py) | Step 4: demonstrates the custom-tool and streaming example with a single prompt asking about Seattle and Tokyo |
| [`weather_assistant.py`](weather_assistant.py) | Step 5: adds an interactive terminal loop to the same streaming, custom-tool session |
| [`requirements.txt`](requirements.txt) | Pins the Python dependencies used by the project |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Repository-specific guidance for continuing the learning project |

The virtual environment and local cache directories are intentionally excluded from version control.

## SDK Compatibility

The project uses:

```text
microsoft-copilot-sdk==2.0.1
```

The earlier tutorial package and API examples use some 1.x-style names and parameters. During the original dependency migration, the project encountered this SDK protocol mismatch:

```text
SDK protocol version mismatch: SDK supports versions 3-3, but server reports version 4
```

The dependency was migrated to `microsoft-copilot-sdk==2.0.1`, and the implementation was updated to its supported APIs.

The implementation was adapted rather than assuming every tutorial line works unchanged:

| Tutorial concept | SDK 2.0.1 implementation |
| --- | --- |
| Constructing a client | `CopilotClient(mode="coding-agent")` |
| Approving permissions | `permissions={"on_request": PermissionHandler.approve_all}` |
| Enabling streaming | `events={"streaming": True}` |
| Registering custom tools | `tools={"definitions": [get_weather]}` |
| Stopping the client/session | `async with` context managers |
| Reusing one session | The interactive loop calls `send_and_wait()` repeatedly |

The original tutorial examples do not become universally invalid: the mismatch depends on the SDK package and release being used. This repository documents and implements the APIs verified for `microsoft-copilot-sdk==2.0.1`.

## How the Custom Weather Tool Works

`GetWeatherParams` is a Pydantic model that defines the tool input:

- `city` is a required string
- Pydantic and `define_tool` generate the JSON Schema exposed to Copilot
- `get_weather` receives the validated city name
- The function returns a city, simulated temperature, and simulated condition
- Copilot may call the tool while answering a user's weather prompt

The weather values are intentionally random. They demonstrate custom-tool execution and do not represent real weather observations or forecast data.

## Prerequisites

- Python 3.11 or newer, as required by the official quickstart
- A virtual environment
- GitHub Copilot CLI installed and authenticated
- Network access for requests to the Copilot service

The official SDK package for Python is `microsoft-copilot-sdk==2.0.1` in this repository. The SDK uses the Copilot CLI/runtime required by the quickstart.

Follow the official [GitHub Copilot CLI installation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) to install and authenticate the CLI.

## Installation

Clone the repository and enter it:

```bash
git clone https://github.com/jenkauppila/copilot_sdk_learning_lab.git
cd copilot_sdk_learning_lab
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the pinned dependencies:

```bash
python -m pip install -r requirements.txt
```

Confirm that the GitHub Copilot CLI is installed and authenticated before running an example.

## Running the Examples

### Single-prompt Step 4 example

From the repository root:

```bash
python main.py
```

This creates a session, streams the response to a question about Seattle and Tokyo, and closes the session.

### Interactive Step 5 assistant

```bash
python weather_assistant.py
```

The assistant supports repeated prompts in the same session:

```text
You: What's the weather in Paris?
You: Compare weather in NYC and LA
You: exit
```

Type `exit`, press `Ctrl+D`, or press `Ctrl+C` to leave the interactive program.

## Limitations

- Weather data is simulated and should not be used for real decisions.
- This project is an educational implementation, not a production weather service.
- It may contact the Copilot service and requires an authenticated environment.
- The approval handler used in these examples automatically approves permission requests. Production code should apply an appropriate permission policy.
- The repository does not currently include an automated test suite.

## Reference

- [Official GitHub Copilot SDK quickstart](https://docs.github.com/en/copilot/get-started/sdk-quickstart)
