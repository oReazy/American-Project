import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Подработка на ферме

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
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


async def Getting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Фермер'")
    await message.answer(
        message=f"✅ Вы успешно устроились на работу фермера"
        )
    await Show(message, bot, api)
    return


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)
    return


async def Info1(message: Message, bot: Bot, api: API):
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


async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Info2'")
    await message.answer(
        message=f"🌽 » 📖 Виды работ\n\n"
                f"На ферме есть несколько служебных должностей, на которых вы можете работать. Узнать на каких должностях вы можете "
                f"работать, вы можете узнать в скиллах -> навык фермера\n\n"
                f"Чернорабочий (сбор кукурузы) — это самая первая должность на ферме. Именно на данной должности вы будете ходить по полю и собирать "
                f"кукурузу.\n"
                f"Тракторист — вторая должность после чернорабочего. На данной должности вы будете работать на тракторе и вспахивать поле ковшом\n"
                f"Комбайнер — третья должность после тракториста. На данной должности вы собираете готовую кукурузу\n"
                f"Пилот кукурзника — четвертая должность после комбайнера. На данной должности вы должны будете иметь лицензию пилотирования. Тут вы будете летать на кукурзнике и сбрасывать химические элементы.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def choose(message: Message, bot: Bot, api: API):
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


# --------------------------------------------------------------------------------------------

# Работа чернорабочего (первая)

# --------------------------------------------------------------------------------------------

async def CheckRab1(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if int(data[70]) >= 0:
        await message.answer(
            message=f"✅ Вы успешно устроились на работу чернорабочего"
        )
        await rab1_1(message, bot, api)
        return
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)
        return


async def rab1_1(message: Message, bot: Bot, api: API):
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


async def rab1_2(message: Message, bot: Bot, api: API):
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


async def rab1_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"👁 Вы ищите поле для сбора урожая"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"👁 Вы нашли поле, где можно собирать урожай"
    )
    await rab1_4(message, bot, api)
    return


async def rab1_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_4'")
    await message.answer(
        message=f"🚶 Подойдите к полю, чтобы начать собирать урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к полю", {"cmd": "farm.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶 Вы ходите к полю"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"🚶 Вы подошли к полю и готовы собирать кукурузу"
    )
    await rab1_6(message, bot, api)
    return


async def rab1_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_6'")
    await message.answer(
        message=f"👨‍🌾 Собирайте урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🌽 Собирать кукурузу", {"cmd": "farm.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab1_7(message: Message, bot: Bot, api: API):
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
    await rab1_8(message, bot, api)
    return


async def rab1_8(message: Message, bot: Bot, api: API):
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


async def rab1_end(message: Message, bot: Bot, api: API):
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




# --------------------------------------------------------------------------------------------

# Работа тракториста (вторая)

# --------------------------------------------------------------------------------------------


async def CheckRab2(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if int(data[70]) >= 500:
        await message.answer(
            message=f"✅ Вы успешно устроились на работу тракториста"
        )
        await rab2_1(message, bot, api)
        return
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)
        return



async def rab2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"📦 Для того, чтобы начать работу трактористом, вам необходимо взять ключи от трактора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Взять ключи", {"cmd": "farm.rab2_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return



async def rab2_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_2'")
    await message.answer(
        message=f"🔑 Вы взяли ключи от трактора в гараже"
    )
    await message.answer(
        message=f"🚜 Подойдите и сядьте в тот трактор, от которого вы взяли ключи",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Подойти и сесть в трактор", {"cmd": "farm.rab2_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return



async def rab2_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы идете к трактору..."
    )
    await asyncio.sleep(3)
    await message.answer(
        message=f"🚜 Вы садитесь в трактор..."
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_3'")
    await message.answer(
        message=f"🔑 Заведите трактор",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Завести трактор", {"cmd": "farm.rab2_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return



async def rab2_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы вставили ключ в зажигание"
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🔑 Вы вставили ключ и поворачиваете его..."
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🔑 Трактор завелся"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_4'")
    await message.answer(
        message=f"🚜 Выезжайте из гаража и едьте к полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выехать из гаража", {"cmd": "farm.rab2_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab2_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выезжаете из гаража"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы выехали из гаража и едете к полю..."
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🚜 Вы приехали к полю"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_5'")
    await message.answer(
        message=f"🚜 Прицепите ковш к трактору",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Прицепить ковш к трактору", {"cmd": "farm.rab2_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab2_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы цепляете ковш к трактору"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы прицепили ковш к трактору"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_6'")
    await message.answer(
        message=f"🚜 Если вы готовы, то начинайте движение по полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Начать движение", {"cmd": "farm.rab2_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab2_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы начали движение"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы вспахиваете землю своим ковшом"
    )
    await asyncio.sleep(10)
    await message.answer(
        message=f"🚜 Вы вспахали половину поля, продолжаем оставшуюся часть вспахивать"
    )
    await asyncio.sleep(10)
    await rab2_8(message, bot, api)
    return


async def rab2_8(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    new_data = int(data[75]) + 1
    new_skill = int(data[70]) + 2
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skill_farmer = '{new_skill}'")
    await message.answer(
        message=f"🌽 Вы вспохали поле"
    )
    await rab2_9(message, bot, api)
    return


async def rab2_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_9'")
    await message.answer(
        message=f"🌽 Желаете продолжить или хотите закончить работу и получить деньги за труд?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Закончить работу", {"cmd": "farm.rab2_end"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Продолжить работу", {"cmd": "farm.rab2_10"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab2_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_10'")
    await message.answer(
        message=f"🚜 Вы едете к новому полю"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы приехали к новому полю"
    )
    await message.answer(
        message=f"🚜 Если вы готовы, то начинайте движение по полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Начать движение", {"cmd": "farm.rab2_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def rab2_end(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    zarplata = int(data[75]) * 15
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")

    await message.answer(
        message=f"👨‍🌾 Том » Спасибо, что поработал на моей ферме. Ты вспохал {int(data[75])} полей и в итоге твоя зарплата составляет {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return