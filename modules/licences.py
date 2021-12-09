import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Лицензии у игрока

# -------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'licences.Show'")
    await message.answer(
        message=f"🎯 » 👤 » 📒 Мои лицензии\n\n"
                f"🚗 Лицензия на автомобили » {data[26]}\n"
                f"🏍 Лицензия на мотоциклы » {data[27]}\n"
                f"🚚 Лицензия на грузовой транспорт » {data[28]}\n"
                f"🔫 Лицензия на оружие » {data[29]}\n"
                f"🐠 Лицензия на ловлю рыбы » {data[30]}\n"
                f"🛩 Лицензия на воздушный транспорт » {data[31]}\n"
                f"🛥 Лицензия на водный транспорт » {data[32]}\n"
                f"🐅 Лицензия на охоту » {data[33]}\n\n"
                f"💬 Некоторые лицензии можно получить в центре лицензирования, но некоторые можно только "
                f"в полиции.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )