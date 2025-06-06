from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
from datetime import datetime

# Загружаем переменные из .env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
target_group_id = int(os.getenv("TARGET_CHAT_ID"))
source_username = os.getenv("SOURCE_USERNAME")

client = TelegramClient('gift_signal_session', api_id, api_hash)

@client.on(events.NewMessage(from_users=source_username))
async def handler(event):
    message = event.message.message
    if "подарки" in message and "🎁" in message:
        await client.send_message(target_group_id, f"🎁 Обнаружено ({datetime.now().strftime('%H:%M:%S')}):\n\n{message}")
        print("📤 Переслано сообщение:", message)

client.start()
print("🤖 Бот запущен. Ожидаю сигналы от @giftuvedex_bot...")
client.run_until_disconnected()
