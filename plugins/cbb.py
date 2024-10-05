#TELEGRAM > @ifeelscam

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =f"<b>○ ᴏᴡɴᴇʀ : <a href='t.me/Urr_Sanjiii'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Straw_Hat_Bots'>Cʟɪᴄᴋ Hᴇʀᴇ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/+Euuw_DXNxhxkMjFl'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ Gʀᴏᴜᴘ</a>\n○ ᴅᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/Urr_Sanjiii'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"Kᴏɴɴɪᴄʜɪᴡᴀ!! 𝐎ᴛᴀᴋᴜ⚡,\n\n<b>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Flux'>𝐀ɴɪᴍᴇ 𝐅ʟᴜx...</a></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>sᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ʙᴏᴛ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ",url = "https://t.me/Straw_Hat_Bots")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
