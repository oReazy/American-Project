import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys
from modules import database


# ------------------------------------------------------------------------------------------

async def registration_1(message: Message):
    await database.registerNewAccaunt(message.from_id)
    await database.setUserData(message.from_id, 'state', "'registration.registration_1_check'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"👋🏻 Добро пожаловать на проект {server_settings[8]} на сервер {server_settings[9]}\n\n"
                f"❌ Ваш аккаунт не зарегистрирован на данном сервере.\n"
                f"📝 Придумайте ник вашего персонажа (от 3 до 15 символов)"
    )
    return


async def registration_1_check(message: Message):
    if 3 <= len(message.text) <= 15:
        if await database.findBaseData('nick', f"'{message.text}'") == 0:
            await database.setUserData(message.from_id, 'state', "'registration.registration_2'")
            await database.setUserData(message.from_id, 'nick', f"'{message.text}'")
            await registration_2(message)
        else:
            await message.answer(
                message='❌ Ошибка. Данный ник уже занят. Попробуйте другой'
            )
            await registration_1(message)
    else:
        await message.answer(
            message=f'❌ Ошибка. Вы ввели либо короткий ник, либо слишком длинный.'
        )
        await registration_1(message)


async def registration_2(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_2'")
    await message.answer(
        message=f"🚻 Выберите пол вашего персонажа\n\n"
                f"⤵ Для выбора нажмите на одну из кнопок ниже",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("👨 Мужчина", {"cmd": "registration.registration_2_man"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("👩 Девушка", {"cmd": "registration.registration_2_woman"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )
    return


async def registration_2_man(message: Message):
    await database.setMultiUserData(message.from_id, "sex = 'Мужчина', state = 'registration.registration_3'")
    await registration_3(message)
    return


async def registration_2_woman(message: Message):
    await database.setMultiUserData(message.from_id, "sex = 'Женщина', state = 'registration.registration_3'")
    await registration_3(message)
    return


async def registration_3(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_3'")
    await message.answer(
        message=f"⤵️ Выберите национальность вашему персонажу",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("Американец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Канадец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Итальянец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Ирландец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Китаец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Японец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Русский", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Украинец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Серб", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Вьетнамец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Гаитянин", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Араб", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Еврей", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Афроамериканец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )
    return


async def registration_3_check(message: Message):
    await database.setMultiUserData(message.from_id, f"nationality = '{message.text}', state = 'registration.registration_4'")
    await registration_4(message)
    return


async def registration_4(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_4_check'")
    await message.answer(
        message=f"📝 Введите возраст персонажа (от 18 до 70 лет)"
    )
    return


async def registration_4_check(message: Message):
    if message.text.isdigit():
        age = int(message.text)
        if 18 <= age <= 70:
            await database.setMultiUserData(message.from_id, f"age = '{age}', state = 'registration.registration_5'")
            await registration_5(message)
        else:
            await message.answer(
                message=f"❌ Введите возраст в пределах от 18 до 70"
            )
            await registration_4(message)
            return
    else:
        await message.answer(
            message=f"❌ Введите возраст цифрами"
        )
        await registration_4(message)
        return


async def registration_5(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_5'")
    await message.answer(
        message=f"🏃 Откуда вы узнали о нашем сервере?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("👥 Узнал от друзей", {"cmd": "registration.registration_5_friend"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("📄 Узнал из списка чат-ботов", {"cmd": "registration.registration_5_list_chatbot"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("🔎 Узнал из поисковой системы", {"cmd": "registration.registration_5_search"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("📺 Узнал от ютубера", {"cmd": "registration.registration_5_youtube"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("🔘 Другое", {"cmd": "registration.registration_5_other"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )
    return


async def registration_5_friend(message: Message):
    server_settings = await database.getBdData('settings', 'id', '1')
    update = server_settings[20] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_friend', f"'{update}'")
    await registration_6(message)
    return


async def registration_5_list_chatbot(message: Message):
    server_settings = await database.getBdData('settings', 'id', '1')
    update = server_settings[21] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_list_chatbot', f"'{update}'")
    await registration_6(message)
    return


async def registration_5_search(message: Message):
    server_settings = await database.getBdData('settings', 'id', '1')
    update = server_settings[22] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_search', f"'{update}'")
    await registration_6(message)
    return


async def registration_5_youtube(message: Message):
    server_settings = await database.getBdData('settings', 'id', '1')
    update = server_settings[23] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_youtube', f"'{update}'")
    await registration_6(message)
    return


async def registration_5_other(message: Message):
    server_settings = await database.getBdData('settings', 'id', '1')
    update = server_settings[24] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_other', f"'{update}'")
    await registration_6(message)
    return


async def registration_6(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_6'")
    server_settings = await database.getBdData('settings', 'id', '1')
    await message.answer(
        message=f"📬 Не желаете подписаться на новостную рассылку проекта?\n\n"
                f"Если вы согласитесь, то при каждой рассылке вы будете получать {await database.pretty(server_settings[12])} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("Подписаться", {"cmd": "registration.registration_6_accept"}), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("❌ Отказаться", {"cmd": "registration.registration_6_denial"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )
    return


async def registration_6_accept(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setMultiUserData(message.from_id, "mailing_project = '✅ Подписан', mailing_server = '❌ Не подписан'")
    await message.answer(
        message=f"✅ Вы успешно подписались на рассылку о новостях проекта.\n"
                f"⚠ Чтобы отписаться от данной рассылки, вам необходимо перейти в настройки вашего персонажа."
    )
    await registration_7(message)
    return


async def registration_6_denial(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setMultiUserData(message.from_id, "mailing_project = '❌ Не подписан', mailing_server = '❌ Не подписан', state = 'registration.registration_7'")
    await message.answer(
        message=f"❌ Вы отказались от рассылки.\n"
                f"⚠ Вы всегда можете подписаться от отписаться от рассылки в настройках персонажа."
    )
    await registration_7(message)
    return


async def registration_7(message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setMultiUserData(message.from_id, f"lvl = '{server_settings[4]}', exp = '{server_settings[6]}', dollars = '{server_settings[5]}', donate = '{server_settings[7]}'")
    await registration_8(message)
    return


async def registration_8(message: Message):
    await database.setUserData(message.from_id, 'state', "'registration.registration_8'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"✈ Каждый человек, который прилетает в штат {server_settings[9]} получает начальное пособие:\n\n"
                f"— 💵 Доллары » {await database.pretty(server_settings[5])}\n\n"
                f"ℹ Данного пособия будет достаточно до того момента, пока вы не найдете себе работу.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Callback("💵 Забрать пособие", payload={"cmd": "mainMenu.ShowFixFromId"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


# ---------------------------------------------------------------------------------

async def newAccaunt(message: Message):
    await database.deleteUserData(message.from_id)
    await registration_1(message)
    return