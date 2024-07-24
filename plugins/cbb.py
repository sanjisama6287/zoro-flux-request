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
            text =f"<b><blockquote>★ ᴏᴡɴᴇʀ : <a href='t.me/InkaLinks'>ɪɴᴋᴀ ᴄʜɪᴘs</a>\n★ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/publicfille'>ᴘᴜʙʟɪᴄ ғɪʟᴇ</a>\n★ ᴘᴀɪᴅ ʙᴏᴛ : <a href='https://t.me/ifeelscam'>ᴍʀ.sʜᴀɪᴋʜ</a>\n★ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/offchats'>ᴄᴏᴅᴇ ᴍᴏɴᴋᴇʏ's </a>\n★ ᴅᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/ifeelscam'>ʜᴀᴍᴢᴀ</a></blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/+NeqCUg-QDxo2Nzll"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , url= "https://t.me/publicfille")],
                 [InlineKeyboardButton("ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴀᴅs ɪɴ ᴏɴᴇ ᴄʟɪᴄᴋ ", callback_data = "buy")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ 𝟷𝟾+ sʜᴏʀᴛs ᴠɪᴅᴇᴏs ",url = "http://t.me/UnseenRobot/shorts")],
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
            text=f"👋 Hey {query.from_user.mention}\n\n<b><blockquote>I'm advance bot of providing videos from a certain Channel!!.</blockquote></b>",
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
                        [ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ",url = "t.me/Justchips")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
