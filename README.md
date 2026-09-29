# AI Roadmap

A collection of small, hands-on projects for learning AI and software development. Each project lives in its own folder and has a dedicated README for setup instructions, implementation notes, and learning takeaways.

## Project index

| Project | Focus | Status | Documentation |
| --- | --- | --- | --- |
| Token-Aware Multi-Model Chatbot | Python, token counting, model selection, streaming APIs | In progress | [Project README](token-aware-multi-model-chatbot/README.md) |

New projects will be added to this index as they are created. Keep project-specific setup and learning notes in that project's README; use this file as the repository overview and navigation page.

## Repository layout

```text
ai_roadmap/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
└── token-aware-multi-model-chatbot/
    ├── README.md
    └── multi_bot.py
```

Local-only files such as `.env` and Python virtual environments are intentionally excluded from Git. See [Environment setup](#environment-setup) before running projects that require credentials.

## Environment setup

Python projects in this repository share the root `requirements.txt` for now. From the repository root, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, use `python3 -m venv .venv` and `source .venv/bin/activate` instead.

For projects that use API credentials, copy `.env.example` to `.env` at the repository root and fill in your own keys. Never commit `.env`, API keys, tokens, or other credentials. See the individual project README for the variables it needs.

