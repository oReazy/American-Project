import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Склад

# -------------------------------------------------------------------------------------------




async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Show'")
    data = await database.getUserData(message.from_id)
    if data[27] == 'Безработный' or data[27] != 'Работник склада':
        await message.answer(
            message=f"📦 Склад\n\n"
                    f"🧑 Здраствуй, нам необходимы грузчики для того, чтобы разгрузить вагоны",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "warehouse.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "warehouse.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "warehouse.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
    else:
        await message.answer(
            message=f"📦 Склад\n\n"
                    f"🧑 Здраствуй, {data[3]}. Приехали новые вагоны с палетами, их необходимо разгрузить.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "warehouse.rab1_1"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "warehouse.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "warehouse.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "warehouse.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def Getting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Работник склада'")
    await message.answer(
        message=f"✅ Вы успешно устроились на завод"
        )
    await Show(message, bot, api)


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)


async def Info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Info1'")
    await message.answer(
        message=f"📦 » 📖 Информация по зарплатам\n\n"
                f"📦 За один перенесенный мешок вам заплатят » 20 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )



async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Info2'")
    await message.answer(
        message=f"📦 » 📖 Информация о работе\n\n"
                f"На складе вы будете работать грузчиком. Вашей основной задачей является перенос "
                f"мешков из вагонов на склад. За каждый перенесенный мешок вам дают зарплату",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )

# ---------------------------------------------------------------------------------------------------------