# Copilot instructions

## Project overview

This repository is a hands-on Python learning project following the official GitHub Copilot SDK quickstart:
https://docs.github.com/en/copilot/get-started/sdk-quickstart

The goal is to understand the SDK incrementally, beginning with a simple prompt and progressing to streaming responses, custom tools, and an interactive assistant.

The project currently uses `microsoft-copilot-sdk==2.0.1` (see `requirements.txt`). The original `github-copilot-sdk` package was replaced after a protocol version mismatch. Do not reintroduce the deprecated dependency or assume that code from an older tutorial works unchanged with the installed SDK.

Keep the project small and learning-focused. `main.py` is the current executable entrypoint. Introduce additional files, abstractions, or dependencies only when a lesson or clear practical need justifies them.

## Setup and commands

Use the repository's virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the current example from the repository root:

```bash
python main.py
```

Optional checks:

```bash
python -m pip check
python -m py_compile main.py
```

These checks do not replace running the application. The example requires a working GitHub Copilot environment and may contact the Copilot service.

There is currently no configured automated test suite, test runner, linter, or formatter. If tests are added later, keep them focused and explain how to run them.

## Implementation conventions

- Use asynchronous Python consistently. Keep `asyncio.run(main())` as the executable entrypoint unless a lesson requires a different structure.
- Follow the APIs and lifecycle patterns supported by the installed SDK version. The current working example uses asynchronous context managers for client and session cleanup; future lessons may introduce other supported patterns.
- Treat the official quickstart as a learning sequence, not as a requirement to preserve every line of its sample code. Adapt examples to the installed SDK when necessary and explain the differences.
- Configure models, permissions, and available tools deliberately for each lesson. Do not assume that tools must always be disabled or that all permission requests should be approved.
- For streaming lessons, explain event subscriptions, message-delta events, and completion behavior. Verify event names and response fields against the installed SDK before changing code.
- For custom-tool lessons, explain what each tool can do, what inputs it receives, and any permission or safety implications.
- Handle SDK responses defensively when fields or content may be absent.
- Keep `requirements.txt` aligned with the dependencies actually used by the project. Avoid unrelated dependency upgrades.
- Do not commit `.venv`, bytecode or cache files, `.env`, credentials, tokens, or macOS metadata. Respect `.gitignore`.

## Learning and collaboration preferences

- Explain the purpose of a proposed change before making it, using clear language and a small practical example when useful.
- Work through the tutorial one step at a time. Prefer small, testable changes over large rewrites.
- Distinguish required tutorial changes from optional improvements or alternative approaches.
- When troubleshooting, identify the observed error and likely cause before suggesting a fix. Do not guess at SDK APIs when they can be verified.
- Preserve working code and previously completed learning milestones when practical.
- Explain unfamiliar Python, SDK, Git, and GitHub concepts without assuming advanced experience.
- Do not introduce frameworks, project restructuring, or unrelated features without a clear reason.
- Do not automatically commit, push, open or close issues, or otherwise modify GitHub without explicit approval.
- When suggesting commits, use descriptive messages reflecting the actual changes. Link to an existing issue when appropriate, rather than creating duplicate issues.

## Documentation and progress

Use Git commits to record meaningful milestones in the learning process. Keep explanations of SDK migrations, troubleshooting, and lesson-specific changes accurate to what has actually been tested. Update project documentation when the implementation materially changes, but do not rewrite these instructions for every small tutorial step.
