from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
API_ID = int(input("Enter API ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
