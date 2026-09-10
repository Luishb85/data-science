# 🗓️ FDS no DF — Local Events Agent (Telegram Bot)

An automated agent that searches the web for weekend cultural and entertainment events happening in Brasília (DF, Brazil) and delivers a curated, formatted agenda directly to Telegram.

## 🎯 What it does

Every week, the bot:
1. **Collects** upcoming weekend events in Brasília and the surrounding metropolitan area from web sources (shows, festivals, exhibitions, theater, fairs, etc.)
2. **Curates** the results, filtering for relevance and quality
3. **Validates** the collected information before publishing
4. **Formats** the content into a structured, emoji-tagged message
5. **Publishes** the final agenda to a Telegram channel/chat

The output is a ready-to-read weekend guide, organized by category (highlight of the week, live shows, theater & culture, parties & fairs), each entry including date, time, location, admission info, and a source link.

## 🧩 Architecture

The project is built around a set of **skills** (agent instructions/prompts), each responsible for one stage of the pipeline:

| Skill | Responsibility |
|---|---|
| `coleta_eventos.md` | Searches and collects raw event information from the web |
| `curadoria.md` | Curates and filters the collected events |
| `validacao.md` | Validates the accuracy/completeness of the information |
| `formatacao_telegram.md` | Formats the final message for Telegram delivery |

## 📁 Project structure

```
1-fdsnodf_bot/
├── skills/                    # Agent skill definitions (prompts/instructions)
│   ├── coleta_eventos.md
│   ├── curadoria.md
│   ├── formatacao_telegram.md
│   └── validacao.md
├── fdsnodf.py                 # Main orchestration script
├── publicar_telegram.py       # Telegram publishing logic
├── teste_telegram.py          # Telegram integration test script
├── rodar.bat                  # Batch script to run/schedule execution
├── pyproject.toml             # Project dependencies (managed with uv)
├── uv.lock                    # Locked dependency versions
├── .env                       # Environment variables / credentials (not versioned)
└── output/                    # Generated weekly agenda files (not versioned)
```

## 🛠️ Tech stack

Python · uv (dependency management) · Telegram Bot API · web search / LLM-based agent pipeline

## ⚙️ How it runs

The project appears to run on a scheduled basis (see `agendador_exec.log`), triggered via `rodar.bat`, executing the full pipeline from event collection to Telegram publication automatically.

## 📌 Example output

See [`examples/`](./examples) for a sample of a generated weekend agenda.

---

*Note: this README was drafted based on the project's file structure and a sample output shared during development — please review and adjust any inaccurate assumptions about the pipeline before publishing.*
