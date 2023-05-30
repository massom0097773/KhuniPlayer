from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def owner(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9c816d97efbbfc8a032dd.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 [𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭](https://t.me/about_meeBachaa) & 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫'𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿 🥀", url=f"https://t.me/about_meeBachaa")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝗠𝗿 𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 🥀", url=f"https://t.me/massomop")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/innocentop"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/about_meeBachaa")
                ]
            ]
        ),
    )
