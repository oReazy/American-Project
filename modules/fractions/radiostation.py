import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database, characterAction

# ------------------------------------------------------------------------------------------

# Панель лидера фракции

# -------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'radiostation.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'id', "'6'")
    if data_user[22] != data_fraction[1]:
        if data_fraction[8] == 0:
            await message.answer(
                message=f"🎯 » 🗺 » 🏛 » 📻 Радиостанция\n\n"
                        f"Добро пожаловать на радиостанцию. Отправить свое объявление вы можете с помощью телефона\n\n"
                        f"🔒 На данный момент данная организация не набирает людей",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "map.importandPlaces2"}), color=KeyboardButtonColor.PRIMARY)
                        .get_json()
                )
            )
        else:
            await message.answer(
                message=f"🎯 » 🗺 » 🏛 » 📻 Радиостанция\n\n"
                        f"Добро пожаловать на радиостанцию. Отправить свое объявление вы можете с помощью телефона",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "map.importandPlaces2"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("📄 Оставить резюме", {"cmd": "radiostation.Sobes"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
    else:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 📻 Радиостанция\n\n"
                    f"Добро пожаловать на радиостанцию!",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces2"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💻 Панель работника", {"cmd": "radiostation.JobPanel"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )


async def Sobes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'radiostation.SobesCheck'")
    server_settings = await database.getBdData('fractions', 'id', "'6'")
    data_user = await database.getUserData(message.from_id)

    if data_user[22] == 'Без организации':
        data = ast.literal_eval(server_settings[9])
        data = list(data)
        for row in data:
            if row[0] == message.from_id:
                await message.answer(
                    message=f"❌ Ошибка. Вы уже оставляли свое резюме.",
                )
                await Show(message, bot, api)
                return
        await message.answer(
            message=f"✏ Напишите немного про себя, сколько вам полных лет, сколько лет проживаете в штате,"
                    f"а также почему выбрали именно нашу организацию (до 500 букв)",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "radiostation.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"❌ Ошибка. Вы уже состоите в другой организации!",
        )
        await Show(message, bot, api)
        return


async def SobesCheck(message: Message, bot: Bot, api: API):
    if len(message.text) <= 500:
        server_settings = await database.getBdData('fractions', 'id', "'6'")
        data_user = await database.getUserData(message.from_id)

        text = message.text.replace("\n", "")
        text = text.replace("\r", "")
        new_data = [message.from_id, text, data_user[3], data_user[6], data_user[8]]
        data = ast.literal_eval(server_settings[9])
        data = list(data)
        data.append(new_data)
        await database.setBdData('fractions', 'id', "'6'", 'resumes', f'\"{data}\"')
        await message.answer(
            message=f"✅ Вы успешно отправили свое резюме. Совсем скоро лидер его проверит и в случае, если вы подходите, вам пришлют уведомление",
        )
        await Show(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Ошибка. Текст вашего резюме превышает норму на {len(message.text)-500} символов",
        )
        await Show(message, bot, api)




# ----------------------------------------------------------------------------------------------------------------------


async def JobPanel(message: Message, bot: Bot, api: API):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data_user = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'radiostation.JobPanel'")
    data_adverts = ast.literal_eval(server_settings[28])
    data_adverts = list(data_adverts)

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📻 » 💻 Панель работника\n\n"
                f"",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "radiostation.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📇 Редактирование объявлений", {"cmd": "radiostation.JobPanel_Adverts"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Задания", {"cmd": "radiostation.JobPanel_Tasks"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Информация о фракции", {"cmd": "radiostation.JobPanel_Info"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def JobPanel_Adverts(message: Message, bot: Bot, api: API):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data_user = await database.getUserData(message.from_id)

    data_adverts = ast.literal_eval(server_settings[28])
    data_adverts = list(data_adverts)
    if data_user[23] >= 3:
        if len(data_adverts) > 0:
            count = -1
            for item in data_adverts:
                count = count + 1
                if item[2] == 'no edit':
                    item[2] = 'in edit'
                    data_adverts.pop(count)
                    await database.setMultiUserData(message.from_id, f'temporary_var = "{item}"')
                    await database.setMultiDbData('settings', 'id', "'1'", f'advert_edit = "{data_adverts}"')
                    await JobPanel_Adverts2(message, bot, api)
                    return
            await message.answer('❌ Ошибка. В данный момент нет объявлений для редактирования')
            await JobPanel(message, bot, api)
        else:
            await message.answer('❌ Ошибка. В данный момент объявлений нет')
            await JobPanel(message, bot, api)
    else:
        await message.answer('❌ Ошибка. Редактировать объявления можно с 3-его ранга')
        await JobPanel(message, bot, api)



async def JobPanel_Adverts2(message: Message, bot: Bot, api: API):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data_user = await database.getUserData(message.from_id)

    server_settings = ast.literal_eval(data_user[44])
    server_settings = list(server_settings)

    if server_settings[3] == '📄 Стандартное объявление': payment = 300
    if server_settings[3] == '👑 VIP объявление': payment = 3000
    await database.setUserData(message.from_id, 'state', "'radiostation.JobPanel_Adverts2Check'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📻 » 💻 » 📇 Редактирование объявлений (вам заплатят {await database.pretty(payment)} долларов (💵)\n\n"
                f"📇 Отредактируйте объявление » {server_settings[0]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🗑 Отклонить объявление", {"cmd": "radiostation.JobPanel_Adverts2Denied"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def JobPanel_Adverts2Check(message: Message, bot: Bot, api: API):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    server_fraction = await database.getBdData('fractions', 'id', "'6'")
    data_user = await database.getUserData(message.from_id)

    data_adverts = ast.literal_eval(server_settings[28])
    data_adverts = list(data_adverts)

    data_user_temporary = ast.literal_eval(data_user[44])
    data_user_temporary = list(data_user_temporary)
    if len(message.text) > 160:
        await message.answer('❌ Ошибка. Текст отредактированного объявления слишком длинный')
        await JobPanel_Adverts2(message, bot, api)
        return
    if data_user_temporary[3] == '📄 Стандартное объявление':
        payment = 300
        payment_fraction = 700
    if data_user_temporary[3] == '👑 VIP объявление':
        payment = 3000
        payment_fraction = 22000
    await database.setUserData(message.from_id, 'dollars', f"'{data_user[12] + payment}'")
    await database.setBdData('fractions', 'id', "'6'", 'bank', f"'{server_fraction[7] + payment_fraction}'")

    data_adverts_access = ast.literal_eval(server_settings[27])
    data_adverts_access = list(data_adverts_access)

    try:
        if len(data_adverts) > 9:
            data_adverts_access.pop(0)
    except:
        pass
    ad = [message.text, data_user_temporary[1], int(message.from_id), data_user_temporary[3]]
    data_adverts_access.append(ad)


    await database.setMultiDbData('settings', 'id', "'1'", f'advert_access = "{data_adverts_access}"')
    await message.answer('✅ Вы успешно отредактировали объявление')
    await JobPanel(message, bot, api)