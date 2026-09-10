# =============================================================================
# publicar_telegram.py — Publica o último .md gerado no canal Telegram
# =============================================================================
# Uso: uv run publicar_telegram.py
#
# Lê o arquivo bsb_weekend_*.md mais recente da pasta output/BSB/
# e publica no canal configurado no .env.
# =============================================================================

import os, asyncio
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

output_dir = Path(__file__).parent / "output/BSB/"

async def main():
    try:
        from telegram import Bot
    except ImportError:
        print("⚠️  Execute primeiro: uv add python-telegram-bot")
        return

    token   = os.getenv("TELEGRAM_BOT_TOKEN")
    channel = os.getenv("TELEGRAM_CHANNEL_ID")

    if not token or not channel:
        print("⚠️  Configure TELEGRAM_BOT_TOKEN e TELEGRAM_CHANNEL_ID no .env")
        return

    # Pega o .md mais recente
    arquivos = sorted(output_dir.glob("fdsnodf_*.md"), reverse=True)
    if not arquivos:
        print("⚠️  Nenhum arquivo bsb_weekend_*.md encontrado em output/BSB/")
        return

    arquivo = arquivos[0]
    conteudo = arquivo.read_text(encoding="utf-8")

    print(f"📄 Arquivo: {arquivo.name}")
    print(f"📏 Tamanho: {len(conteudo)} caracteres")
    print(f"📣 Canal  : {channel}")
    print()

    confirmar = input("Confirma publicação? (s/n): ").strip().lower()
    if confirmar != "s":
        print("❌ Publicação cancelada.")
        return

    bot = Bot(token=token)
    LIMITE = 4096
    partes = [conteudo[i:i+LIMITE] for i in range(0, len(conteudo), LIMITE)]

    for i, parte in enumerate(partes, 1):
        await bot.send_message(
            chat_id=channel,
            text=parte,
            parse_mode="Markdown",
        )
        print(f"✅ Parte {i}/{len(partes)} enviada")

    print(f"\n🎉 Publicado com sucesso em {channel}!")

asyncio.run(main())