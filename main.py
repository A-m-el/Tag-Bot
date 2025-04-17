from telethon import events
from utilities import client
from tagAll import run

# check if the sender is an admin
async def is_admin(event):
    if event.is_private:
        return False
    user = await event.client.get_permissions(event.chat_id, event.sender_id)
    return user.is_admin

# handle /all command
@client.on(events.NewMessage(pattern='/all'))
async def handler(event):
    if await is_admin(event):
        await run(event)
    else:
        await event.reply("🚫 المشرفون فقط من يمكنهم استخدام هذا البوت")

# running bot
print("Bot is running...")
client.run_until_disconnected()
