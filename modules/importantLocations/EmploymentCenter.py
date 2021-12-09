import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Центр лицензирования

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'EmploymentCenter.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » ⚒ Центр занятости",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🛠 Найти работу", {"cmd": "EmploymentCenter.none"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )