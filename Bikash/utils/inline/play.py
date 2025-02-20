import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bikash = math.floor(percentage)
    if 0 < bikash <= 10:
        bar = "𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿════════"
    elif 10 < bikash < 20:
        bar = "═𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═══════"
    elif 20 <= bikash < 30:
        bar = "══𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿══════"
    elif 30 <= bikash < 40:
        bar = "═══𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═════"
    elif 40 <= bikash < 50:
        bar = "════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿════"
    elif 50 <= bikash < 60:
        bar = "═════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═══"
    elif 60 <= bikash < 70:
        bar = "══════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿══"
    elif 70 <= bikash < 80:
        bar = "═══════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═"
    elif 80 <= bikash < 95:
        bar = "════════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿"
    else:
        bar = "════════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bikash = math.floor(percentage)
    if 0 < bikash <= 10:
        bar = "𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿════════"
    elif 10 < bikash < 20:
        bar = "═══𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═════"
    elif 20 <= bikash < 30:
        bar = "══𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿══════"
    elif 30 <= bikash < 40:
        bar = "═══𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═════"
    elif 40 <= bikash < 50:
        bar = "════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿════"
    elif 50 <= bikash < 60:
        bar = "═════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═══"
    elif 60 <= bikash < 70:
        bar = "══════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿══"
    elif 70 <= bikash < 80:
        bar = "═══════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿═"
    elif 80 <= bikash < 95:
        bar = "════════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿"
    else:
        bar = "════════𝐈𝐧𝐧𝐨𝐜𝐞𝐧𝐭 𝗦𝗲𝗿𝘃𝗲𝗿"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"innocentPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"innocentPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗢𝘄𝗻𝗲𝗿 📱", url=f"https://t.me/massomop"
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏸️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏏️",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹️",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            )
        ],
    ]
    return buttons
