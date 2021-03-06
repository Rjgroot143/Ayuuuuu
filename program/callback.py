# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ง๐ต๐ถ๐ ๐ถ๐ ๐๐ต๐ฒ ๐๐๐๐๐ ๐๐๐ง  ๐ ๐๐๐ถ๐ฐ...!**
๐ง๐ต๐ถ๐ ๐ถ๐ ๐๐ต๐ฒ ๐ฝ๐ก๐๐๐  ๐๐๐ฉ...!

โโโโโโโโโโโโโโโโโโโ

โฃยป แดแด แดแด๊ฑษชแด แดสแดสแดส สแดแด. 

โฃยป สษชษขส วซแดแดสษชแดส แดแด๊ฑษชแด.

โฃยป แด ษชแดแดแด แดสแดส ๊ฑแดแดแดแดสแดแดแด.

โฃยป แดแดแด แดษดแดแดแด ๊ฐแดแดแดแดสแด๊ฑ.

โฃยป ๊ฑแดแดแดส๊ฐแด๊ฑแด ๊ฑแดแดแดแด.

โโโโโโโโโโโโโโโโโโโ
แดแด๊ฑษชษขษดแดแด สส :** [๐ฏ๐น๐ฎ๐ฐ๐ธ ๐ฐ๐ฎ๐ ](https://t.me/The_cat_lover0)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("แดแดแดแดแดษดแด สษช๊ฑแด", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "๊ฑแดแดแดแดสแด", url=f"https://t.me/catmusicworld"
                    ),
                    InlineKeyboardButton(
                        "แดแดแดแดแดแด๊ฑ", url=f"https://t.me/catmusicworld"
                    ),
                ],[
                    InlineKeyboardButton(
                        "๐ แดแดแด  สแดสส ๐",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐  สแดแดแด", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ **สแดสสแดแดก [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป ๊ฐแดส แดษดแดแดกษชษดษข แด แดแดแดแดแดษดแด สษช๊ฑแด แด๊ฐ ๊ฐแดสสแดษด แดแด๊ฑแด แดสแด๊ฑ๊ฑ แดสแด สแดแดแดแดษด๊ฑ ษขษชแด แดษด สแดสแดแดก แดษดแด สแดแดแด แดแดแดแดแดษดแด๊ฑ แดxแดสแดษดแดแดษชแดษด.

**แดสษช๊ฑ แดแด สแดแด ษช๊ฑ ๊ฑแดแดแดษชแดสสส แดแด๊ฑษชษขษดแดแด สส สสแดแดแด แดแดแด .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("แดแดแดษชษด แดแดแด", callback_data="cbadmin"),
                    InlineKeyboardButton("๊ฑแดแดแด แดแดแด", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("สแด๊ฑษชแด แดแดแด", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐  สแดแดแด", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" สแด๊ฑษชแด แดแดแดแดแดษดแด๊ฑ :

ยป /play [๊ฑแดษดษข ษดแดแดแด/สษชษดแด] - แดสแดส แดแด๊ฑษชแด แดษด แด ษชแดแดแด แดสแดแด 
ยป /stream [Qแดแดสส/สษชษดแด] - ๊ฑแดสแดแดแด แดสแด สแด สษชแด แด/สแดแดษชแด สษชแด แด แดแด๊ฑษชแด 
ยป /vplay [แด ษชแดแดแด ษดแดแดแด/สษชษดแด] - แดสแดส แด ษชแดแดแด แดษด แด ษชแดแดแด แดสแดแด 
ยป /vstream - แดสแดส สษชแด แด แด ษชแดแดแด ๊ฐสแดแด สแด สษชแด แด/แด3แด8 
ยป /playlist - ๊ฑสแดแดก สแดแด แดสแด แดสแดสสษช๊ฑแด 
ยป /video [Qแดแดสส] - แดแดแดกษดสแดแดแด แด ษชแดแดแด ๊ฐสแดแด สแดแดแดแดสแด 
ยป /song [Qแดแดสส] - แดแดแดกษดสแดแดแด ๊ฑแดษดษข ๊ฐสแดแด สแดแดแดแดสแด 
ยป /lyrics [Qแดแดสส] - ๊ฑแดสแดแด แดสแด ๊ฑแดษดษข สสสษชแด 
ยป /search [Qแดแดสส] - ๊ฑแดแดสแดส แด สแดแดแดแดสแด แด ษชแดแดแด สษชษดแด  
ยป /ping - ๊ฑสแดแดก แดสแด สแดแด แดษชษดษข ๊ฑแดแดแดแด๊ฑ 
ยป /uptime - ๊ฑสแดแดก แดสแด สแดแด แดแดแดษชแดแด ๊ฑแดแดแดแด๊ฑ 
ยป /alive - ๊ฑสแดแดก แดสแด สแดแด แดสษชแด แด ษชษด๊ฐแด [ษชษด ษขสแดแดแด]

**แดสษช๊ฑ แดแด สแดแด ษช๊ฑ ๊ฑแดแดแดษชแดสสส แดแด๊ฑษชษขษดแดแด สส สสแดแดแด แดแดแด.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐  สแดแดแด", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""แดแดแดษชษด แดแดแดแดแดษดแด๊ฑ :

ยป /pause - แดแดแด๊ฑแด แดสแด ๊ฑแดสแดแดแด 
ยป /resume - สแด๊ฑแดแดแด แดสแด ๊ฑแดสแดแดแด 
ยป /skip - ๊ฑแดกษชแดแดส แดแด ษดแดxแด ๊ฑแดสแดแดแด 
ยป /stop - ๊ฑแดแดแด แดสแด ๊ฑแดสแดแดแดษชษดษข 
ยป /vmute - แดแดแดแด แดสแด แด๊ฑแดสสแดแด แดษด แด แดษชแดแด แดสแดแด 
ยป /vunmute - แดษดแดแดแดแด แดสแด แด๊ฑแดสสแดแด แดษด แด แดษชแดแด แดสแดแด 
ยป /volume 1-200 - แดแดแดแด๊ฑแด แดสแด แด แดสแดแดแด แด๊ฐ แดแด๊ฑษชแด (แด๊ฑแดสสแดแด แดแด๊ฑแด สแด แดแดแดษชษด) 
ยป /reload - สแดสแดแดแด สแดแด แดษดแด สแด๊ฐสแด๊ฑส แดสแด แดแดแดษชษด แดแดแดแด 
ยป /userbotjoin - ษชษดแด ษชแดแด แดสแด แด๊ฑแดสสแดแด แดแด แดแดษชษด ษขสแดแดแด 
ยป /userbotleave - แดสแดแดส แด๊ฑแดสสแดแด แดแด สแดแดแด แด ๊ฐสแดแด ษขสแดแดแด

**แดสษช๊ฑ แดแด สแดแด ษช๊ฑ ๊ฑแดแดแดษชแดสสส แดแด๊ฑษชษขษดแดแด สส สสแดแดแด แดแดแด.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐  สแดแดแด", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ๊ฑแดแดแด แดแดแดแดแดษดแด๊ฑ :

ยป /rmw - แดสแดแดษด แดสส สแดแดก ๊ฐษชสแด๊ฑ 
ยป /rmd - แดสแดแดษด แดสส แดแดแดกษดสแดแดแดแดแด ๊ฐษชสแด๊ฑ 
ยป /sysinfo - ๊ฑสแดแดก แดสแด ๊ฑส๊ฑแดแดแด ษชษด๊ฐแดสแดแดแดษชแดษด 
ยป /update - แดแดแดแดแดแด สแดแดส สแดแด แดแด สแดแดแด๊ฑแด แด แดส๊ฑษชแดษด 
ยป /restart - สแด๊ฑแดแดสแด สแดแดส สแดแด 
ยป /leaveall - แดสแดแดส แด๊ฑแดสสแดแด แดแด สแดแดแด แด ๊ฐสแดแด แดสส ษขสแดแดแด

**แดสษช๊ฑ แดแด สแดแด ษช๊ฑ ๊ฑแดแดแดษชแดสสส แดแด๊ฑษชษขษดแดแด สส สสแดแดแด แดแดแด.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐  สแดแดแด", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ ** ๊ฑแดแดแดษชษดษข๊ฑ ๊ฐแดส** {query.message.chat.title}\n\nโธ : แดแดแด แดแดแด๊ฑแด\nโถ๏ธ : แดแดแด สแด๊ฑแดแดแด\n๐ : แดแดแด แดแดแดแด\n๐ : แดแดแด แดษดแดแดแดแด\nโน : แดแดแด ๊ฑแดสแดแดแด ๊ฑแดแดแด\n\nยฉ @The_cat_lover0",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐  แดสแด๊ฑแด", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
