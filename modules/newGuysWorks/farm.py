import asyncio
import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    if data[43] == 'Безработный' or data[43] != 'Фермер':
        await message.answer(
            message=f"🌽 Ферма\n\n"
                    f"👨‍🌾 Здраствуй, меня зовут Том и добро пожаловать на мою ферму. Вы что-то хотите?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "farm.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "farm.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Виды работ", {"cmd": "farm.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
        return
    else:
        await message.answer(
            message=f"🌽 Ферма\n\n"
                    f"👨‍🌾 Здраствуй, {data[3]}. Не хочешь сегодня поработать?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "farm.choose"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "farm.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "farm.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Виды работ", {"cmd": "farm.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
        return


async def Getting(message):
    await database.setUserData(message.from_id, 'work', "'Фермер'")
    await message.answer(
        message=f"✅ Вы успешно устроились на работу фермера"
        )
    await Show(message)
    return


async def Leave(message):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message)
    return


async def Info1(message):
    await database.setUserData(message.from_id, 'state', "'farm.Info1'")
    await message.answer(
        message=f"🌽 » 📖 Информация по зарплатам\n\n"
                f"На данной работе есть несколько должностей. На каждой должности вы получаете разную зарплату.\n\n"
                f"Чернорабочий (сбор кукурузы) » 10 долларов (💵)\n"
                f"Тракторист » 15 долларов (💵)\n"
                f"Комбайнер » 25 долларов (💵)\n"
                f"Пилот кукурузника » 30 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def Info2(message):
    await database.setUserData(message.from_id, 'state', "'farm.Info2'")
    await message.answer(
        message=f"🌽 » 📖 Виды работ\n\n"
                f"На ферме есть несколько служебных должностей, на которых вы можете работать. Узнать на каких должностях вы можете "
                f"работать, вы можете узнать в скиллах -> навык фермера\n\n"
                f"Чернорабочий (сбор кукурузы) — это самая первая должность на ферме. Именно на данной должности вы будете ходить по полю и собирать "
                f"кукурузу.\n"
                f"Тракторист — вторая должность после чернорабочего. На данной должности вы будете работать на тракторе и разбрасывать зерна кукурузы\n"
                f"Комбайнер — третья должность после тракториста. На данной должности вы собираете готовую кукурузу\n"
                f"Пилот кукурзника — четвертая должность после комбайнера. На данной должности вы должны будете иметь лицензию пилотирования. Тут вы будете летать на кукурзнике и сбрасывать химические элементы.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def choose(message):
    await database.setUserData(message.from_id, 'state', "'farm.choose'")
    await message.answer(
        message=f"🌽 » ⚒ Работать\n\n"
                f"Выберите, на какой должности вы будете работать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("⚒ Чернорабочий", {"cmd": "farm.CheckRab1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Тракторист", {"cmd": "farm.CheckRab2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Комбайнер", {"cmd": "farm.CheckRab3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Пилот кукурузника", {"cmd": "farm.CheckRab4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def CheckRab1(message):
    data = await database.getUserData(message.from_id)
    if int(data[70]) >= 0:
        await message.answer(
            message=f"✅ Вы успешно устроились на работу чернорабочего"
        )
        await rab1_1(message)
        return
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message)
        return


async def rab1_1(message):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"📦 Для того, чтобы начать работу, вам необходимо взять спец. инструменты из ангара фермы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Взять инструменты", {"cmd": "farm.rab1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_2(message):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_2'")
    await message.answer(
        message=f"📦 Вы взяли спец. инструменты из ангара"
    )
    await message.answer(
        message=f"🌽 Найдите поле, где можно собирать кукурузу",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👁 Найти поле", {"cmd": "farm.rab1_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_3(message):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"👁 Вы ищите поле для сбора урожая"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"👁 Вы нашли поле, где можно собирать урожай"
    )
    await rab1_4(message)
    return


async def rab1_4(message):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_4'")
    await message.answer(
        message=f"🚶 Подойдите к полю, чтобы начать собирать урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к полю", {"cmd": "farm.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_5(message):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶 Вы идете к полю"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"🚶 Вы подошли к полю и готовы собирать кукурузу"
    )
    await rab1_6(message)
    return


async def rab1_6(message):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_6'")
    await message.answer(
        message=f"👨‍🌾 Собирайте урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🌽 Собирать кукурузу", {"cmd": "farm.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_7(message):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🌽 Вы наклонились и начинаете собирать кукурузу"
    )
    await asyncio.sleep(7)
    kukurusa = random.randint(1, 5) # количество кукурузы, которое можем забрать за раз
    data = await database.getUserData(message.from_id)
    new_data = int(data[75]) + kukurusa
    new_skill = int(data[70]) + 1
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skill_farmer = '{new_skill}'")
    await message.answer(
        message=f"🌽 Вы собрали {kukurusa} кукурузы"
    )
    await rab1_8(message)
    return


async def rab1_8(message):
    await message.answer(
        message=f"🌽 Желаете продолжить или хотите сдать всю кукурузу и получить деньги за труд?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Закончить работу", {"cmd": "farm.rab1_end"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Продолжить работу", {"cmd": "farm.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_end(message):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    zarplata = int(data[75]) * 10
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")

    await message.answer(
        message=f"👨‍🌾 Том » Спасибо, что поработал на моей ферме. Ты собрал {int(data[75])} кукурузы и в итоге твоя зарплата составляет {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return