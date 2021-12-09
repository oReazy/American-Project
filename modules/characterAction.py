import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Действия персонажа

# ------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'characterAction.Show'")
    await message.answer(
        message=f"🎯 » 👤 Действия персонажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📊 Моя статистика", {"cmd": "characterAction.Statistics"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💼 Инвентарь", {"cmd": "inventory.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚗 Меню автомобиля", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🏠 Меню дома", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏪 Меню бизнеса", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🤠 Меню лидера", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("⏏ Улучшения", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📕 Мой паспорт", {"cmd": "passport.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📒 Мои лицензии", {"cmd": "licences.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🐯 Татуировки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("👥 Меню семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def Statistics(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'characterAction.Statistics'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 👤 » 📊 Моя статистика\n\n"
                f"😀 Ник » {data[3]}\n"
                f"🌐 Уровень » {data[6]}\n"
                f"🌐 Очки опыта » {data[7]} / {server_settings[16] * data[6]}\n"
                f"🚻 Пол » {data[8]}\n"
                f"🔢 Возраст » {data[9]} лет\n"
                f"🏳 Национальность » {data[10]}\n\n"
                f"💵 Доллары на руках » {await database.pretty(data[12])}\n"
                f"💶 Евро на руках » {await database.pretty(data[13])}\n"
                f"💴 Иены на руках » {await database.pretty(data[14])}\n"
                f"💷 Фунты на руках » {await database.pretty(data[15])}\n\n"
                f"🛠 Работа » {data[43]}\n"
                f"🏢 Организация » {data[24]}\n"
                f"⭐ Уровень розыска » {data[20]}\n\n"
                f"🅰️ Предупреждения » {data[34]}\n"
                f"💳 Банковская карта » {data[69]}\n"
                f"📱 Телефон » {data[5]}\n"
                f"👑 VIP » {data[22]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )