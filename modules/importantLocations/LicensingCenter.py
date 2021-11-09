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
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Доброго времени суток, добро пожаловать в центр лицензирования. Чем я могу вам помочь?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📒 Получение прав", {"cmd": "LicensingCenter.GetLicences"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 Узнать стоимость", {"cmd": "LicensingCenter.PricesLicences"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def GetLicences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.GetLicences'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 » 📒 Получение прав\n\n"
                f"👨 Какие права вы желаете получить. Как только вы выберите права, не забудьте их оплатить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🚗 Автомобильные права", {"cmd": "LicensingCenter.AutoCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏍 Лицензия на мотоциклы", {"cmd": "LicensingCenter.BikeCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def AutoCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[26] == '✅ Имеется':
        await message.answer(
            message=f"❌ У вас уже имеются данные права"
        )
        await GetLicences(message, bot, api)
        return
    if int(data[12]) >= 1500:
        new_balance = int(data[12]) - 1500
        await database.setUserData(message.from_id, 'dollars', f"'{new_balance}'")
        await message.answer(
            message=f"✅ Вы заплатили 1 500 долларов (💵) за права"
        )
        await AutoQuestion1(message, bot, api)
        return
    else:
        await message.answer(
            message=f"❌ У вас недостаточно денег (нужно 1 500 долларов (💵)) "
        )
        await GetLicences(message, bot, api)
        return




async def AutoQuestion1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion1'")
    await message.answer(
        message=f"👨 Инструктор » С какой скоростью можно ездить по городу?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("40", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("60", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("90", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def AutoQuestion2(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion2':
        if message.text == '60':
            await database.setUserData(message.from_id, 'temporary_var', "'1'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion2'")
    await message.answer(
        message=f"👨 Инструктор » Что нужно сделать при тумане?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Увеличить скорость и включить фары", {"cmd": "LicensingCenter.AutoQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Снизить скорость и включить фары", {"cmd": "LicensingCenter.AutoQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Остановиться и выключить фары", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def AutoQuestion3(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion3':
        if message.text == 'Снизить скорость и включить фары':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion3'")
    await message.answer(
        message=f"👨 Инструктор » На какой стороне дороги разрешена остановка?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("На правой стороне", {"cmd": "LicensingCenter.AutoQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("На левой стороне", {"cmd": "LicensingCenter.AutoQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def AutoQuestion4(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion4':
        if message.text == 'На правой стороне':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion4'")
    await message.answer(
        message=f"👨 Инструктор » Что необходимо сделать при повороте на нерегулируемом перекрестке?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Уступить дорогу проезжающим машинам", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Дождаться разрешающего сигнала", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Пропустить пешеходов", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def AutoQuestion5(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion5':
        if message.text == 'Пропустить пешеходов':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion5'")
    await message.answer(
        message=f"👨 Инструктор » Разрешена ли парковка на тротуаре?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Только в экстренных случаях", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Да", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Иногда", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Нет", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return




async def AutoQuestion6(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion6':
        if message.text == 'Только в экстренных случаях':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion6'")
    await message.answer(
        message=f"👨 Инструктор » В каком случае стоит пристегивать ремень безопасности?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("В любом случае", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Когда необходимо", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("При полицейских", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def AutoQuestion7(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion7':
        if message.text == 'В любом случае':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion7'")
    await message.answer(
        message=f"👨 Инструктор » Разрешено ли движение задним ходом на магистрали?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Запрещен", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Разрешен", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Только в экстренных ситуациях", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def AutoQuestion8(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[2] != 'LicensingCenter.AutoQuestion8':
        if message.text == 'В любом случае':
            new_ball = int(data[75]) + 1
            await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion8'")
    data = await database.getUserData(message.from_id)
    new_ball = int(data[75])
    if new_ball >= 4:
        await message.answer(
            message=f"👨 Инструктор » Вы успешно сдали экзамен на {new_ball} из 7 баллов.\nПолучите свои права, ждем вас снова в центре лицензирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Callback("📒 Получить права", payload={"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"👨 Инструктор »  Увы, вы не сдали на права. Вы набрали {new_ball} из 7 баллов. Попробуйте еще раз",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return

async def AutoOpen(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'LicensingCenter.Show'")
    await database.setUserData(from_id, 'license_auto', "'✅ Имеется'")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"📒 Вы взяли права на вождение автомобилей.\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Покупать автомобили в автосалонах и управлять ими\n"
                f"— Работать на работах: таксист, механиком\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def PricesLicences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.PricesLicences'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Мы являемся единственным местом лицензирования всех жителей штата. Здесь вы можете получить большинство лицензий. "
                f"Вот наш прайс-лист:\n\n"
                f"🚗 Лицензия на автомобили » 1 500 долларов (💵)\n"
                f"🏍 Лицензия на мотоциклы » 250 долларов (💵)\n"
                f"🚚 Лицензия на грузовой транспорт » 5 000 долларов (💵)\n"
                f"🔫 Лицензия на оружие » приобретается в полиции\n"
                f"🐠 Лицензия на ловлю рыбы » 500 долларов (💵)\n"
                f"🛩 Лицензия на воздушный транспорт » 50 000 (💵)\n"
                f"🛥 Лицензия на водный транспорт » 15 000 (💵)\n"
                f"🐅 Лицензия на охоту » приобретается в полиции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return
