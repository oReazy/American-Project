import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Раздел с историей ников

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'historyNicks.Show'")
    data = await database.getUserData(message.from_id)
    if data[56] == '[]':
        await message.answer(
            message=f"🎯 » 📃 История ников\n\n❌ История ников пуста.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )
    else:
        list_nicks = ast.literal_eval(data[56])
        nicks_end = ''
        count = 0
        while count < len(list_nicks) or count >= 20:
            nicks_end = nicks_end + f'{list_nicks[count]}\n'
            count = count + 1
        await message.answer(
            message=f"🎯 » 📃 История ников\n\n{nicks_end}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )