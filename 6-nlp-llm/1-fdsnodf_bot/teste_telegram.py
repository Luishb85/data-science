# teste_telegram.py
import os, asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    from telegram import Bot
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    
    await bot.send_message(
        chat_id=os.getenv("TELEGRAM_CHANNEL_ID"),
        text="🧪 Teste do bot *FDS no DF* — tudo funcionando! 🎉",
        parse_mode="Markdown"
    )
    print("✅ Mensagem enviada com sucesso!")

asyncio.run(main())