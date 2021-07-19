import asyncio

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re, ast, datetime
from modules import database
from modules import mainMenu


# ------------------------------------------------------------------------------------------

async def Check(message: Message):
    data = database.getUserData(message.from_id)
    if data[5] == '❌ Отсутствует':
        await message.answer(
            message=f"❌ У вас нет мобильного телефона. Купить вы его можете в магазине электроники",
        )
        await mainMenu.Show(message)
    else:
        await Show(message)
        return


async def Show(message: Message):
    database.setUserData(message.from_id, 'state', "'block.Show'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"📱 Вы достали телефон из кормана"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📱 Вы включили телефон"
    )
    await asyncio.sleep(2)
    await ShowMenu(message)
    return


async def PowerOff(message: Message):
    database.setUserData(message.from_id, 'state', "'block.Show'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"📱 Вы выключили телефон"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📱 Вы убрали телефон в корман"
    )
    await asyncio.sleep(2)
    await mainMenu.Show(message)
    return



async def ShowMenu(message: Message):
    database.setUserData(message.from_id, 'state', "'telephone.ShowMenu'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 📱 Телефон",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔴 Выключить телефон", {"cmd": "telephone.PowerOff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("⏰ Служба точного времени", {"cmd": "telephone.Time"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📌 Заметки", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Time(message: Message):
    database.setUserData(message.from_id, 'state', "'telephone.ShowMenu'")
    data = database.getUserData(message.from_id)
    real_time = datetime.datetime.now()
    real_day = datetime.date.today()
    await message.answer(
        message=f"⏰ Служба точного времени — на страже ваших секунд\n\n"
                f"⏰ Точное время: {real_time.hour}:{real_time.minute}:{real_time.second}\n"
                f"📅 Сегодня: {real_day.day}.{real_day.month}.{real_day.year}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔄 Обновить", {"cmd": "telephone.Time"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return