import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database, characterAction

# ------------------------------------------------------------------------------------------

# Центр лицензирования

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.Show'")
    data = await database.getUserData(message.from_id)
    if int(data[81]) == 0:
        await message.answer(
            message=f"❌ Вы не состоите в семье",
        )
        await characterAction.Show(message, bot, api)
    else:
        family_data = await database.getBdData('familys', 'id', f"'{int(data[81])}'")

        FounderData = await database.getUserData(int(family_data[5]))
        Founder = FounderData[3]

        if int(family_data[6]) == 0:
            Vice1 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[6]))
            Vice1 = ViceData[3]

        if int(family_data[7]) == 0:
            Vice2 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[7]))
            Vice2 = ViceData[3]


        if int(family_data[8]) == 0:
            Vice3 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[8]))
            Vice3 = ViceData[3]

        if int(family_data[8]) == 0:
            home = '❌ Отсутствует'
        else:
            home = '✅ Имеется'


        await message.answer(
            message=f"👥 Меню семьи » {family_data[1]} {family_data[3]} {family_data[4]}\n\n"
                    f"🏘 Семейная квартира » {home}\n\n"
                    f"🅾️ Основатель семьи » {Founder}\n"
                    f"🛃 Заместитель №1 » {Vice1}\n"
                    f"🛃 Заместитель №2 » {Vice2}\n"
                    f"🛃 Заместитель №3 » {Vice3}\n\n"
                    f"❗ Слоган » {family_data[10]}\n"
                    f"💬 Описание семьи » {family_data[2]}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "family.Show2"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👥 Управление семьей", {"cmd": "family.Control"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👥 Информация о семье", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👥 Члены семьи онлайн", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👥 Члены семьи оффлайн", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👥 Рейтинг", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("👥 Помощь", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🏘 Семейная квартира", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("✔ Галочка", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("⭐ Бренд", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )



async def Show2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.Show2'")
    data = await database.getUserData(message.from_id)
    if int(data[81]) == 0:
        await message.answer(
            message=f"❌ Вы не состоите в семье",
        )
        await characterAction.Show(message, bot, api)
    else:
        family_data = await database.getBdData('familys', 'id', f"'{int(data[81])}'")

        FounderData = await database.getUserData(int(family_data[5]))
        Founder = FounderData[3]

        if int(family_data[6]) == 0:
            Vice1 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[6]))
            Vice1 = ViceData[3]

        if int(family_data[7]) == 0:
            Vice2 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[7]))
            Vice2 = ViceData[3]


        if int(family_data[8]) == 0:
            Vice3 = 'Свободно'
        else:
            ViceData = await database.getUserData(int(family_data[8]))
            Vice3 = ViceData[3]

        if int(family_data[8]) == 0:
            home = '❌ Отсутствует'
        else:
            home = '✅ Имеется'


        await message.answer(
            message=f"👥 Меню семьи » {family_data[1]} {family_data[3]} {family_data[4]}\n\n"
                    f"🏘 Семейная квартира » {home}\n\n"
                    f"🅾️ Основатель семьи » {Founder}\n"
                    f"🛃 Заместитель №1 » {Vice1}\n"
                    f"🛃 Заместитель №2 » {Vice2}\n"
                    f"🛃 Заместитель №3 » {Vice3}\n\n"
                    f"❗ {family_data[10]}\n"
                    f"💬 Описание семьи » {family_data[2]}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "family.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🏃🏻 Покинуть семью", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🛒 Семейный магазин", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )


async def Control(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.Control'")
    data = await database.getUserData(message.from_id)
    family_data = await database.getBdData('familys', 'id', f"'{int(data[81])}'")
    await message.answer(
        message=f"👥 Меню семьи » {family_data[1]} {family_data[3]} {family_data[4]} » 👥 Управление семьей\n\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "Control2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("➕ Пригласить в семью", {"cmd": "family.ControlAddFamily"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("➖ Выгнать из семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Описание семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❗ Слоган семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💳 Пополнить бюджет семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💳 Снять с бюджета семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💳 Выдать премию семье", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def Control2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.Control2'")
    data = await database.getUserData(message.from_id)
    family_data = await database.getBdData('familys', 'id', f"'{int(data[81])}'")
    await message.answer(
        message=f"👥 Меню семьи » {family_data[1]} {family_data[3]} {family_data[4]} » 👥 Управление семьей (2-ой лист)\n\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "family.Control"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Заместитель №1", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Заместитель №2", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Заместитель №3", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("➡ Передать права лидера", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def ControlAddFamily(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.ControlAddFamily'")
    await message.answer(
        message=f"⤵ Выберите, как будем добавлять человека в семью",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.Control"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🆔 Через ID в чат-боте", {"cmd": "family.ControlAddFamily1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🆔 Через ID во ВКонтакте", {"cmd": "family.ControlAddFamily2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Через ссылку ВКонтакте", {"cmd": "family.ControlAddFamily3"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ControlAddFamily1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.ControlAddFamily1Check'")
    await message.answer(
        message=f"📝 Введите ID игрока в чат-боте\n\n"
                f"⚠ ID человека, которого вы пытаетесь ввести, должен находится на пирсе, в разделе поиска семей",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.ControlAddFamily"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def ControlAddFamily2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.ControlAddFamily2Check'")
    await message.answer(
        message=f"📝 Введите ID игрока во ВКонтакте\n\n"
                f"⚠ ID человека, которого вы пытаетесь ввести, должен находится на пирсе, в разделе поиска семей",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.ControlAddFamily"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def ControlAddFamily3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.ControlAddFamily3Check'")
    await message.answer(
        message=f"📝 Введите ссылку на игрока во ВКонтакте\n\n"
                f"⚠ Ссылку на человека, которого вы пытаетесь ввести, должен находится на пирсе, в разделе поиска семей",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "family.ControlAddFamily"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )