import asyncio
import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, Callback
import json, time, os, sys, re, ast, datetime

from modules import database
from modules import mainMenu


# ------------------------------------------------------------------------------------------

async def Check(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] > 0:
        await Show(message)
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await mainMenu.Show(message)


async def Show(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Show'")
    data = await database.getUserData(message.from_id)
    report_count = await database.getMultiBdData('report', 'vk_id_admin', "'0'")
    report_count = len(report_count)
    KEYBOARD_ADMIN = Keyboard(one_time=True, inline=False)
    KEYBOARD_ADMIN.add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD_ADMIN.add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_ADMIN.add(Text("▶", {"cmd": "admin.Show2"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD_ADMIN.row()
    if data[11] >= 8:
        KEYBOARD_ADMIN.add(Text("⚙ Панель основателя [8]", {"cmd": "admin.Panel8"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 7:
        KEYBOARD_ADMIN.add(Text("⚙ Панель руководства проекта [7]", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 6:
        KEYBOARD_ADMIN.add(Text("👹 Панель ГА [6]", {"cmd": "admin.Panel6"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 5:
        KEYBOARD_ADMIN.add(Text("🤠 Панель ЗГА [5]", {"cmd": "admin.Panel5"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 4:
        KEYBOARD_ADMIN.add(Text("😎 Старший администратор [4]", {"cmd": "admin.Panel4"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 3:
        KEYBOARD_ADMIN.add(Text("🙂 Администратор [3]", {"cmd": "admin.Panel3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 2:
        KEYBOARD_ADMIN.add(Text("🤨 Младший администратор [2]", {"cmd": "admin.Panel2"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD_ADMIN.row()
    if data[11] >= 1:
        KEYBOARD_ADMIN.add(Text("😀 Хелпер [1]", {"cmd": "admin.Panel1"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_ADMIN.get_json()
    await message.answer(
        message=f"🎯 » 🛠 Админ-панель\n\n"
                f"Здраствуйте @id{message.from_id}({data[3]}), вы являетесь администратором {data[11]} уровня.\n\n"
                f"📢 Количество репорта: {report_count}",
        keyboard=KEYBOARD_ADMIN
    )


async def Show2(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Show2'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 🛠 Админ-панель\n\n"
                f"Здраствуйте @id{message.from_id}({data[3]}), вы являетесь администратором {data[11]} уровня.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📟 Консоль [1]", {"cmd": "admin.toConsole"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Устав администрации [1]", {"cmd": "admin.Rules"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 FAQ для администрации [1]", {"cmd": "admin.FAQ"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 8-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------
async def Panel8(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 8:
        await database.setUserData(message.from_id, 'state', "'admin.Panel8'")
        await message.answer(
            message=f"🎯 » 🛠 » ⚙ Панель основателя [8]\n\n",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👤 Управление администрацией", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💎 Донат", {"cmd": "admin.Panel8_Donate"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("➕ Создать новый аккаунт", {"cmd": "admin.Panel8_NewAccaunt"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Тебе еще рано сюда"
        )
        await Show(message)
        return


async def Panel8_ControlAdmins(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 Управление администрацией",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel8"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("ℹ Информация об администраторе", {"cmd": "admin.Panel8_ControlAdmins_info"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👤 Поставить администратора", {"cmd": "admin.Panel8_ControlAdmins_add"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👤 Повысить/понизить администратора", {"cmd": "admin.Panel8_ControlAdmins_upp"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👤 Снять администратора", {"cmd": "admin.Panel8_ControlAdmins_leave"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel8_ControlAdmins_info(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel8_ControlAdmins_info1', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » ℹ Информация об администраторе\n\n📝 Укажите ссылку на администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_info1(message: Message, bot: Bot):
    try:
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id
        await database.setUserData(id_user, 'temporary_var', "'[]'")
        data = await database.getUserData(id_user)
        if data[66] == '[]':
            await message.answer(
                message=f"🎯 » 🛠 » ⚙ » 👤 » ℹ Информация об администраторе\n\n"
                        f"👤 @id{id_user}({data[3]}), настоящее имя @id{id_user}({user_get[0].first_name} {user_get[0].last_name})\n\n"
                        f"🅰️ Уровень администрирования » {data[11]}\n\n"
                        f"Данный игрок не был администратором на данном сервере",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("🔄 Посмотреть еще", {"cmd": "admin.Panel8_ControlAdmins_info"}),
                             color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
        else:
            info = ast.literal_eval(data[66])
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
            list_punish = info[5]
            punish_end = ''
            count = 0
            for row in list_punish:
                 punish_end = punish_end + f'{row}\n'
            # while count < (len(list_punish)) or count >= 20:
            #     print(f"{count}")
            #     punish_end = punish_end + f'{list_punish[count]}\n'
            #     count = count + 1
            print(punish_end)
            await message.answer(
                message=f"🎯 » 🛠 » ⚙ » 👤 » ℹ Информация об администраторе\n\n"
                        f"👤 @id{id_user}({data[3]}), настоящее имя @id{id_user}({user_get[0].first_name} {user_get[0].last_name})\n\n"
                        f"🅰️ Уровень администрирования » {data[11]}\n\n"
                        f"😀 Имя » {info[0]}\n"
                        f"🔢 Возраст » {info[1]}\n"
                        f"📟 Дискорд » {info[8]}\n"
                        f"🌇 Город проживания » {info[6]}\n"
                        f"💬 Описание администратора » {info[7]}\n\n"
                        f"📅 Поставлен на пост администратора:\n{info[4][0]}\n\n"
                        f"📅 История администрирования:\n{punish_end}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("🔄 Посмотреть еще", {"cmd": "admin.Panel8_ControlAdmins_info"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
    except Exception as ex:
        await message.answer(
            message=f'⚠ Возникла ошибка при проверки данных о администраторе\n\n'
                    f'— Убедитесь, что данный пользователь зарегистрирован в чат-боте.'
        )
        print(ex)
        await Panel8_ControlAdmins_info(message)
    return



async def Panel8_ControlAdmins_leave(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel8_ControlAdmins_leave_1', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Снять администратора\n\n📝 Укажите ссылку на администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_leave_1(message: Message, bot: Bot):
    try:
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id
        await database.setUserData(id_user, 'temporary_var', "'[]'")
        data = await database.getUserData(id_user)
        if data[11] != 0:
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_leave_2'")
            temporary = []
            temporary.append(id_user)
            await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
            await Panel8_ControlAdmins_leave_2(message, bot)
        else:
            await message.answer(
                message=f'⚠ Игрока, которого вы хотите снять с должности не является администратором!\n\n'
                        f'— Убедитесь, что вы ввели правильную ссылку'
            )
            await Panel8_ControlAdmins_leave(message)
    except Exception as ex:
        await message.answer(
            message=f'⚠ Возникла ошибка при снятии данного администратора.\n\n'
                    f'— Убедитесь, что администратору, которому вы хотите выдать админ-права зарегистрирован в чат-боте.\n\n{ex}'
        )
        await Panel8_ControlAdmins_leave(message)
    return


async def Panel8_ControlAdmins_leave_2(message: Message, bot: Bot):
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    admin = await database.getUserData(temporary[0])
    if admin[11] != 0:
        new_lvl = 0
        await database.setMultiUserData(temporary[0], f'admin = "{new_lvl}", state = "mainMenu.Show"')
        await bot.api.messages.send(user_id=temporary[0], random_id=random.randint(1, 9999999999), sticker_id=51567)
        await bot.api.messages.send(
            user_id=temporary[0],
            random_id=random.randint(1, 9999999999),
            message=f"🛑 Вы были сняты с поста администратора данного сервера\n\n"
                    f"ℹ Теперь в главном меню у вас не будет кнопки «Админ-панель», так-как вы больше не являетесь "
                    f"администратором нашего проекта/сервера.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        info = ast.literal_eval(admin[66])
        data_now = datetime.date.today()
        app = []
        app.extend(info[5])
        app.append(f'{data_now.day}.{data_now.month}.{data_now.year} — снят с поста администратора')
        JSON_admin = [
            info[0],
            info[1],
            info[2],
            info[3],
            info[4],
            app,
            info[6],
            info[7],
            info[8]
        ]
        await database.setMultiUserData(temporary[0], f'admin_info = "{JSON_admin}"')
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        await message.answer(
            message=f"✅ Вы успешно сняли с администратора пользователя",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("🔄 Снять еще администратора", {"cmd": "admin.Panel8_ControlAdmins_leave"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return







async def Panel8_ControlAdmins_upp(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel8_ControlAdmins_upp_1', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Повысить/понизить администратора\n\n📝 Укажите ссылку на администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_upp_1(message: Message, bot: API):
    try:
        link = message.text[15:]
        user_get = await bot.users.get(user_ids=link)
        id_user = user_get[0].id
        await database.setUserData(id_user, 'temporary_var', "'[]'")
        data = await database.getUserData(id_user)
        if data[11] != 0:
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_upp_2'")
            temporary = []
            temporary.append(id_user)
            await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
            await Panel8_ControlAdmins_upp_2(message)
        else:
            await message.answer(
                message=f'⚠ Игрока, которого вы хотите повысить в должности не является администратором!\n\n'
                        f'— Убедитесь, что вы ввели правильную ссылку'
            )
            await Panel8_ControlAdmins_upp(message)
    except:
        await message.answer(
            message=f'⚠ Возникла ошибка при повышении/понижении данного администратора.\n\n'
                    f'— Убедитесь, что администратору, которому вы хотите выдать админ-права зарегистрирован в чат-боте.'
        )
        await Panel8_ControlAdmins_upp(message)
    return


async def Panel8_ControlAdmins_upp_2(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_upp_set'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Повысить/понизить администратора\n\n📝 Укажите, что вы хотите сделать с данным администратором\n\n"
                f"ℹ Вы можете повысить/понизить админа на один уровень или установить администратору новый уровень.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Повысить", {"cmd": "admin.Panel8_ControlAdmins_upp_up"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Понизить", {"cmd": "admin.Panel8_ControlAdmins_upp_down"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("1", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("3", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("4", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("6", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("7", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("8", {"cmd": "admin.Panel8_ControlAdmins_upp_set"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_upp_set(message: Message, bot: Bot):
    if message.text.isdigit():
        new_lvl = int(message.text)
        if 1 <= new_lvl <= 8:
            data = await database.getUserData(message.from_id)
            temporary = ast.literal_eval(data[75])
            admin = await database.getUserData(temporary[0])
            await database.setMultiUserData(temporary[0], f'admin = "{new_lvl}", state = "mainMenu.Show"')
            await bot.api.messages.send(user_id=temporary[0], random_id=random.randint(1, 9999999999), sticker_id=17180)
            await bot.api.messages.send(
                user_id=temporary[0],
                random_id=random.randint(1, 9999999999),
                message=f"Вам изменили уровень администрирования на {new_lvl}.\n\n"
                        f"",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                        .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
            info = ast.literal_eval(admin[66])
            data_now = datetime.date.today()
            app = []
            app.extend(info[5])
            app.append(f'{data_now.day}.{data_now.month}.{data_now.year} — изменен на {new_lvl} уровень')
            JSON_admin = [
                info[0],
                info[1],
                info[2],
                info[3],
                info[4],
                app,
                info[6],
                info[7],
                info[8]
            ]
            await database.setMultiUserData(temporary[0], f'admin_info = "{JSON_admin}"')
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
            await message.answer(
                message=f"✅ Вы успешно повысили администратора до {new_lvl} уровня администрирования",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(
                        Text("📝 Изменить уровень этого администратора", {"cmd": "admin.Panel8_ControlAdmins_upp_2"}),
                        color=KeyboardButtonColor.SECONDARY)
                        .add(Text("🔄 Повысить/понизить другого", {"cmd": "admin.Panel8_ControlAdmins_upp"}),
                             color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
            return
        else:
            await message.answer(
                message=f"❌ Введите корректный уровень администратора от 1 до 8"
            )
            await Panel8_ControlAdmins_upp_2(message)


async def Panel8_ControlAdmins_upp_up(message: Message, bot: Bot):
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    admin = await database.getUserData(temporary[0])
    if admin[11] != 8:
        new_lvl = admin[11] + 1
        await database.setMultiUserData(temporary[0], f'admin = "{new_lvl}", state = "mainMenu.Show"')
        await bot.api.messages.send(user_id=temporary[0], random_id=random.randint(1, 9999999999), sticker_id=18509)
        await bot.api.messages.send(
            user_id=temporary[0],
            random_id=random.randint(1, 9999999999),
            message=f"🤙 Поздравляем, вас повысили до {new_lvl} уровня администрирования.\n\n"
                    f"ℹ Теперь вы имеете новый функционал для нового уровня. Увидеть вы его можете на первой "
                    f"страничке админ-панели.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        info = ast.literal_eval(admin[66])
        data_now = datetime.date.today()
        app = []
        app.extend(info[5])
        app.append(f'{data_now.day}.{data_now.month}.{data_now.year} — повышен на {new_lvl} уровень')
        JSON_admin = [
            info[0],
            info[1],
            info[2],
            info[3],
            info[4],
            app,
            info[6],
            info[7],
            info[8]
        ]
        await database.setMultiUserData(temporary[0], f'admin_info = "{JSON_admin}"')
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        await message.answer(
            message=f"✅ Вы успешно повысили администратора до {new_lvl} уровня администрирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}),color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить уровень этого администратора", {"cmd": "admin.Panel8_ControlAdmins_upp_2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Повысить/понизить другого", {"cmd": "admin.Panel8_ControlAdmins_upp"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка при повышении данного администратора.\n\n"
                    f"— Вы не можете повысить администратора, т.к. у него 8 уровень"
        )
        await Panel8_ControlAdmins_upp_2(message)
        return


async def Panel8_ControlAdmins_upp_down(message: Message, bot: Bot):
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    admin = await database.getUserData(temporary[0])
    if admin[11] != 1:
        new_lvl = admin[11] - 1
        await database.setMultiUserData(temporary[0], f'admin = "{new_lvl}", state = "mainMenu.Show"')
        await bot.api.messages.send(user_id=temporary[0], random_id=random.randint(1, 9999999999), sticker_id=5965)
        await bot.api.messages.send(
            user_id=temporary[0],
            random_id=random.randint(1, 9999999999),
            message=f"Вы были понижены до {new_lvl} уровня администрирования.\n\n"
                    f"ℹ Теперь у вас доступно меньше функционала и вкладок в админ-панели",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        info = ast.literal_eval(admin[66])
        data_now = datetime.date.today()
        app = []
        app.extend(info[5])
        app.append(f'{data_now.day}.{data_now.month}.{data_now.year} — понижен на {new_lvl} уровень')
        JSON_admin = [
            info[0],
            info[1],
            info[2],
            info[3],
            info[4],
            app,
            info[6],
            info[7],
            info[8]
        ]
        await database.setMultiUserData(temporary[0], f'admin_info = "{JSON_admin}"')
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        await message.answer(
            message=f"✅ Вы успешно понизили администратора до {new_lvl} уровня администрирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}),color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить уровень этого администратора", {"cmd": "admin.Panel8_ControlAdmins_upp_2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Повысить/понизить другого", {"cmd": "admin.Panel8_ControlAdmins_upp"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка при повышении данного администратора.\n\n"
                    f"— Вы не можете понижать администратора, т.к. у него 1 уровень"
        )
        await Panel8_ControlAdmins_upp_2(message)
        return









async def Panel8_ControlAdmins_add(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel8_ControlAdmins_add_1', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n📝 Укажите ссылку на нового администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_1(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_2'")
    data = await database.getUserData(message.from_id)
    temporary = []
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await Panel8_ControlAdmins_add_2(message)
    return


async def Panel8_ControlAdmins_add_2(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_3'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите имя администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_3(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_4'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите возраст администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_4(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_5'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    today = datetime.date.today()
    now = datetime.datetime.now()
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите дату принятия на пост администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"{today.day}.{today.month}.{today.year} — Поставлен на пост", {"cmd": "admin.Panel8_ControlAdmins_add_5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_5(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_6'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    today = datetime.date.today()
    now = datetime.datetime.now()
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите дату повышения на посту администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"{today.day}.{today.month}.{today.year} — Поставлен на 1 уровень", {"cmd": "admin.Panel8_ControlAdmins_add_6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_6(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_7'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите город проживания администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_7(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_8'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Укажите дискорд администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_8(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_9'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"📝 Опишите администратора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_9(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_10'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    temporary.append(message.text)
    await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"🔢 Укажите уровень администрирования для человека",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("1", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("3", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("4", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("6", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("7", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("8", {"cmd": "admin.Panel8_ControlAdmins_add_10"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_10(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 1 <= count <= 8:
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_11'")
            data = await database.getUserData(message.from_id)
            temporary = ast.literal_eval(data[75])
            temporary.append(message.text)
            await database.setUserData(message.from_id, 'temporary_var', f'"{temporary}"')
            await Panel8_ControlAdmins_add_11(message)
            return
        else:
            await message.answer(
                message=f"❌ Выберите уровень администрирования с 1 до 8")
            await Panel8_ControlAdmins_add_9(message)
            return
    else:
        await message.answer(
            message=f"❌ Вы ввели буквы в сообщении")
        await Panel8_ControlAdmins_add_9(message)
        return


async def Panel8_ControlAdmins_add_11(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins_add_11'")
    data = await database.getUserData(message.from_id)
    temporary = ast.literal_eval(data[75])
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 👤 » 👤 Поставить администратора\n\n"
                f"👤 Вы действительно хотите поставить на пост администратора {temporary[8]} уровня игрока {temporary[0]}\n\n"
                f"😀 Имя » {temporary[1]}\n"
                f"🔢 Возраст » {temporary[2]}\n"
                f"📟 Дискорд » {temporary[6]}\n"
                f"📟 ВКонтакте » {temporary[0]}\n"
                f"📅 Дата назначения » {temporary[3]}\n"
                f"📅 Дата повышения » {temporary[4]}\n"
                f"🌇 Город » {temporary[5]}\n"
                f"💬 Описание » {temporary[7]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Поставить администратора", {"cmd": "admin.Panel8_ControlAdmins_add_set"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("❌ Отменить", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔄 Заново заполнить информацию", {"cmd": "admin.Panel8_ControlAdmins_add"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel8_ControlAdmins_add_set(message: Message, api: API, bot: Bot):
    try:
        await database.setUserData(message.from_id, 'state', "'admin.Panel8_ControlAdmins'")
        data = await database.getUserData(message.from_id)
        temporary = ast.literal_eval(data[75])
        link = temporary[0]
        link = link[15:]
        user_get = await api.users.get(user_ids=link)
        id_user = (user_get[0].id)

        dataadmin = await database.getUserData(id_user)
        if dataadmin[66] == '[]':
            JSON_admin = [
                temporary[1],
                temporary[2],
                f'https://vk.com/{link}',
                id_user,
                [temporary[3]],
                [temporary[4]],
                temporary[5],
                temporary[7],
                temporary[6],
                temporary[8]
            ]
            await database.setMultiUserData(id_user, f'admin = "{temporary[8]}", admin_info = "{JSON_admin}"')
        else:
            info = ast.literal_eval(dataadmin[66])
            posted = []
            posted.extend(info[4])
            posted.append(temporary[3])
            app = []
            app.extend(info[5])
            app.append(temporary[4])
            JSON_admin = [
                temporary[1],
                temporary[2],
                f'https://vk.com/{link}',
                id_user,
                posted,
                app,
                temporary[5],
                temporary[7],
                temporary[6],
                temporary[8]
            ]
            await database.setMultiUserData(id_user, f'admin = "{temporary[8]}", admin_info = "{JSON_admin}"')
        await message.answer(
            message=f"✅ Администратор {user_get[0].first_name} {user_get[0].last_name} успешно назначен на {temporary[8]} уровень администрирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Panel8_ControlAdmins"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔄 Поставить еще одного администратора", {"cmd": "admin.Panel8_ControlAdmins_add"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
                    )
            )
        await bot.api.messages.send(user_id=id_user, random_id=random.randint(1,999999999), sticker_id=8644)
        await bot.api.messages.send(user_id=id_user, random_id=random.randint(1,999999999), message=f'🤟 Поздравляем, вас назначили на {temporary[8]} уровень администрирования.\n\n📖 Прочитайте внимательно устав администрации, который написал вам главный администратор\n📖 Повторите основные правила вашего сервера\nℹ В случае, если у вас возникают трудности с работой в админ-панеле, обращайтесь в FAQ.\n\n😉 Удачи на посту администратора.',
                                    keyboard=(
                                    Keyboard(one_time=True, inline=False)
                                        .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                                        .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                                        .get_json()
                                        )
                                    )
        await database.setUserData(id_user, 'state', "'mainMenu.Show'")
        return
    except Exception as ex:
        await message.answer(
            message=f"⚠ Возникла ошибка при постановлении данного администратора.\n\n"
                    f"— Убедитесь, что игроку, которому вы хотите выдать админ-права зарегистрирован "
                    f"в чат-боте.")
        print(f'ОШИБКА: {ex}')
        await Panel8_ControlAdmins_add_11(message)
    return


async def Panel8_NewAccaunt(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_NewAccaunt'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » ➕ Создать новый аккаунт\n\n"
                f"⚠ Нажимая на зеленую кнопку «Создать аккаунт», вы даете согласие на то, что "
                f"все ваши данные будут безвозвратно обнулены. Ваш ID, ваш уровень администрирования, "
                f"деньги и имущество также будет обнулено (удалено). В случае, если вы не хотите этого, "
                f"то нажмите на кнопку «Отказаться»\n\n"
                f"⚠ В случае, если у вас есть права администратора, то вы должны получить разрешение на нажатие "
                f"этой кнопки у руководителей проекта, либо у основателя.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel8"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Создать новый аккаунт", {"cmd": "registration.newAccaunt"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("❌ Отказаться", {"cmd": "admin.Panel8"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel8_Donate(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel8_Donate'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 💎 Донат\n\n"
                f"📊 Текущий курс обмена рублей на донат » 1 RUB = {server_settings[1]} 💎",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel8"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💎 Изменить курс рубля", {"cmd": "admin.Panel8_Donate_CurseRub"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel8_Donate_CurseRub(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti_PayDayAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 🌐 » 🌐 Изменить множитель PayDay\n\n"
                f"📝 Напишите новый множитель PayDay (от 0 до 5 000)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel8_Donate"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"1", {"cmd": "admin.Panel8_Donate_CurseRubAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2", {"cmd": "admin.Panel8_Donate_CurseRubAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3", {"cmd": "admin.Panel8_Donate_CurseRubAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4", {"cmd": "admin.Panel8_Donate_CurseRubAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5", {"cmd": "admin.Panel8_Donate_CurseRubAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel8_Donate_CurseRubAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 5000:
            await database.setUserData(message.from_id, 'state', "'admin.Panel8_Donate_CurseRubAdd'")
            await database.setBdData('settings', 'id', "'1'", 'course_ruble_to_donate', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли курс рубля к донату",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel8_Donate"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 5 000",
            )
            await Panel8_Donate_CurseRub(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 5 000",
        )
        await Panel8_Donate_CurseRub(message)
        return


# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 7-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel7(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 7:
        await database.setUserData(message.from_id, 'state', "'admin.Panel7'")
        await message.answer(
            message=f"🎯 » 🛠 » ⚙ Панель руководства проекта [7]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📝 Изменить данные", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💎 Изменить курс доната к товарам", {"cmd": "admin.Panel7_EditDonate"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🌐 Изменить множители сервера", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📢 Настройки рассылок", {"cmd": "admin.Panel7_EditMailing"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📊 Статистика приходов игроков", {"cmd": "admin.Panel7_Statistics"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return



async def Panel7_Statistics(message: Message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_Statistics'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📊 Статистика приходов игроков\n\n"
                f"👥 Узнал от друзей » {await database.pretty(int(server_settings[20]))}\n"
                f"📄 Узнал из списка чат-ботов » {await database.pretty(int(server_settings[21]))}\n"
                f"🔎 Узнал из поисковой системы » {await database.pretty(int(server_settings[22]))}\n"
                f"📺 Узнал от ютубера » {await database.pretty(int(server_settings[23]))}\n"
                f"🔘 Другое » {await database.pretty(int(server_settings[24]))}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🚫 Сбросить значения", {"cmd": "admin.Panel7_StatisticsClear"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_StatisticsClear(message: Message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_Statistics'")
    await database.setMultiDbData('settings', 'id', "'1'", f"statistics_friend = '0', 	statistics_list_chatbot = '0', statistics_search = '0', statistics_youtube = '0', statistics_other = '0'")
    await message.answer(
        message=f"✅ Значения по статистике были успешно сброшены"
        )
    await Panel7_Statistics(message)
    return


async def Panel7_EditMailing(message: Message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMailing'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📢 Настройки рассылок\n\n"
                f"ℹ Вознаграждение за рассылки — это уникальный способ замотивировать игроков чаще заходить в чат-бот и пользоваться им. "
                f"Благодаря тому, что людям предлагают бонусы за подписку на рассылку, они будут чаще подписываться на них.\n\n"
                f"📢 Вознаграждение за рассылку новостей проекта » 💵 {await database.pretty(int(server_settings[12]))}\n"
                f"📢 Вознаграждение за рассылку новостей сервера » 💵 {await database.pretty(int(server_settings[13]))}\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📝 Изменить награду за новости проекта", {"cmd": "admin.Panel7_EditMailing_Project"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить награду за новости сервера", {"cmd": "admin.Panel7_EditMailing_Server"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMailing_Project(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMailing_ProjectCheck'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📢 » 📝 Изменить награду за новости проекта\n\n"
                f"📝 Напишите новое вознаграждение за рассылку новостей проекта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditMailing"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("500", {"cmd": "admin.Panel7_EditMailing_ProjectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("1000", {"cmd": "admin.Panel7_EditMailing_ProjectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "admin.Panel7_EditMailing_ProjectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "admin.Panel7_EditMailing_ProjectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "admin.Panel7_EditMailing_ProjectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMailing_ProjectCheck(message: Message):
    if message.text.isdigit():
        price = int(message.text)
        await database.setBdData('settings', 'id', "'1'", 'pay_mailing_project', f"'{price}'")
        await message.answer(
            message=f"✅ Вы успешно поменяли вознаграждение за рассылку новостей проекта"
        )
        await Panel7_EditMailing(message)
    else:
        await message.answer(
            message=f"❌ Введите число"
        )
        await Panel7_EditMailing_Project(message)
        return



async def Panel7_EditMailing_Server(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMailing_ServerCheck'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📢 » 📝 Изменить награду за новости сервера\n\n"
                f"📝 Напишите новое вознаграждение за рассылку новостей сервера",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditMailing"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("500", {"cmd": "admin.Panel7_EditMailing_ServerCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("1000", {"cmd": "admin.Panel7_EditMailing_ServerCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "admin.Panel7_EditMailing_ServerCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "admin.Panel7_EditMailing_ServerCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "admin.Panel7_EditMailing_ServerCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMailing_ServerCheck(message: Message):
    if message.text.isdigit():
        price = int(message.text)
        await database.setBdData('settings', 'id', "'1'", 'pay_mailing_server', f"'{price}'")
        await message.answer(
            message=f"✅ Вы успешно поменяли вознаграждение за рассылку новостей сервера"
        )
        await Panel7_EditMailing(message)
    else:
        await message.answer(
            message=f"❌ Введите число"
        )
        await Panel7_EditMailing_Server(message)
        return





async def Panel7_EditData(message: Message, bot: Bot):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    byld = await bot.api.groups.get_by_id(group_id=message.group_id, fields=['status'])
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 Изменить данные\n\n"
                f"📔 Название проекта » {server_settings[8]}\n"
                f"📔 Название сервера » {server_settings[9]}\n"
                f"📓 Название группы » {byld[0].name}\n"
                f"📓 Статус группы » {byld[0].status}\n"
                f"📔 Название акции » {server_settings[25]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить название проекта", {"cmd": "admin.Panel7_EditData_Project"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить название сервера", {"cmd": "admin.Panel7_EditData_Server"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить название группы", {"cmd": "admin.Panel7_EditData_Group"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить статус группы", {"cmd": "admin.Panel7_EditData_Status"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить название акции", {"cmd": "admin.Panel7_EditData_Stocks"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_Project(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData_ProjectAdd'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 » 📝 Изменить название проекта\n\n"
                f"📝 Напишите новое название проекта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("American Project", {"cmd": "admin.Panel7_EditData_ProjectAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_ProjectAdd(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    await database.setBdData('settings', 'id', "'1'", 'name_project', f"'{message.text}'")
    await message.answer(
        message=f"✅ Вы успешно поменяли название проекта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Panel7_EditData_Server(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData_ServerAdd'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 » 📝 Изменить название сервера\n\n"
                f"📝 Напишите или выберите новое название сервера",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Oregon", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("Texas", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("Nevada", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Colorado", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("California", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("Arizona", {"cmd": "admin.Panel7_EditData_ServerAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_ServerAdd(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    await database.setBdData('settings', 'id', "'1'", 'name_server', f"'{message.text}'")
    await message.answer(
        message=f"✅ Вы успешно поменяли название сервера",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
        )
    return


async def Panel7_EditData_Group(message: Message, bot: Bot):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData_GroupAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 » 📝 Изменить название группы\n\n"
                f"📝 Напишите или выберите название для группы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"{server_settings[8]} | {server_settings[9]}", {"cmd": "admin.Panel7_EditData_GroupAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"{server_settings[8]} | {server_settings[9]} | Обновление!", {"cmd": "admin.Panel7_EditData_GroupAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"{server_settings[8]} | {server_settings[9]} | Акции", {"cmd": "admin.Panel7_EditData_GroupAdd"}), color=KeyboardButtonColor.SECONDARY) .get_json()
            )
        )
    return


async def Panel7_EditData_GroupAdd(message: Message, bot: Bot):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    await bot.api.groups.edit(group_id=message.group_id, title=message.text)
    await message.answer(
        message=f"✅ Вы успешно поменяли название группы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_Status(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData_StatusAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 » 📝 Изменить статус группы\n\n"
                f"📝 Напишите или выберите статус для группы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"~~~ Пустой ~~~", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"😀 На нашем сервере акция для новичков", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"📬 Включай рассылки и следи за проектом", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"🎉 Участвуйте в праздничных мероприятиях", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"⏰ Скоро обновление", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"📝 Открыты заявки на лидерки", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"🤠 Открыты заявки на пост администратора", {"cmd": "admin.Panel7_EditData_StatusAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_StatusAdd(message: Message, bot: API):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    if message.text == '~~~ Пустой ~~~':
        await bot.status.set(group_id=message.group_id, text='')
    else:
        await bot.status.set(group_id=message.group_id, text=message.text)
    await message.answer(
        message=f"✅ Вы успешно поменяли название группы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_Stocks(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData_StocksAdd'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 📝 » 📝 Изменить название акции\n\n"
                f"📝 Напишите новое название акции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("~~~ Пустой ~~~", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Акция для новичков", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Мероприятия и ивенты", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("X3 зарплаты на работах", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("X3 донат", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Скоро новое обновление", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Вышло новое обновление", {"cmd": "admin.Panel7_EditData_StocksAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditData_StocksAdd(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditData'")
    if message.text == '~~~ Пустой ~~~':
        await database.setBdData('settings', 'id', "'1'", 'name_stocks', f"''")
    else:
        await database.setBdData('settings', 'id', "'1'", 'name_stocks', f"' • {message.text}'")
    await message.answer(
        message=f"✅ Вы успешно поменяли название проекта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditData"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditDonate(message: Message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 💎 Изменить курс доната к товарам\n\n"
                f"📊 Текущий курс обмена рублей на донат » 1 RUB = {await database.pretty(server_settings[1])} 💎\n\n"
                f"За 1 💎, игрок может получить {await database.pretty(server_settings[2])} долларов 💵\n"
                f"За {await database.pretty(server_settings[3])} 💎, игрок может получить 1 EXP 🌐\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Изменить обмен доната на доллары", {"cmd": "admin.Panel7_EditDonate_Dollars"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Изменить обмен доната на EXP", {"cmd": "admin.Panel7_EditDonate_EXP"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditDonate_Dollars(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate_DollarsAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 💎 » 💵 Изменить обмен доната на доллары\n\n"
                f"📝 Напишите новый курс обмена доната на доллары (число от 0 до 999 999 999)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditDonate"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"50", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"100", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"150", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"200", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"500", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"750", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"1000", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"1500", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2000", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2500", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"3000", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3500", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4000", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5000", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"7500", {"cmd": "admin.Panel7_EditDonate_DollarsAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditDonate_DollarsAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 999999999:
            await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate'")
            await database.setBdData('settings', 'id', "'1'", 'course_donate_to_dollar', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли курс доната к доллару",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditDonate"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 999 999 999",
            )
            await Panel7_EditDonate_Dollars(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 999 999 999",
        )
        await Panel7_EditDonate_Dollars(message)
        return


async def Panel7_EditDonate_EXP(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate_DollarsAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 💎 » 💵 Изменить обмен доната на доллары\n\n"
                f"📝 Напишите новый курс обмена доната на EXP (число от 0 до 5 000)\n"
                f"⚠ Вы редактируете цену за 1 товар",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditDonate"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"1", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"6", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"7", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"8", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"9", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"10", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"11", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"12", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"13", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"14", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"15", {"cmd": "admin.Panel7_EditDonate_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditDonate_EXPAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 5000:
            await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate'")
            await database.setBdData('settings', 'id', "'1'", 'course_donate_to_exp', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли курс доната к EXP",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditDonate"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 5 000",
            )
            await Panel7_EditDonate_EXP(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 5 000",
        )
        await Panel7_EditDonate_EXP(message)
        return


async def Panel7_EditMulti(message: Message):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditDonate'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 🌐 Изменить множители сервера\n\n"
                f"🌐 Множитель PayDay » {server_settings[14]}\n"
                f"🌐 Множитель зарплат » {server_settings[15]}\n"
                f"🌐 Множитель EXP » {server_settings[16]}\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel7"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Изменить множитель PayDay", {"cmd": "admin.Panel7_EditMulti_PayDay"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Изменить множитель зарплат", {"cmd": "admin.Panel7_EditMulti_Salary"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Изменить множитель EXP", {"cmd": "admin.Panel7_EditMulti_EXP"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMulti_PayDay(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti_PayDayAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 🌐 » 🌐 Изменить множитель PayDay\n\n"
                f"📝 Напишите новый множитель PayDay (от 0 до 500)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"1", {"cmd": "admin.Panel7_EditMulti_PayDayAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2", {"cmd": "admin.Panel7_EditMulti_PayDayAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3", {"cmd": "admin.Panel7_EditMulti_PayDayAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4", {"cmd": "admin.Panel7_EditMulti_PayDayAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5", {"cmd": "admin.Panel7_EditMulti_PayDayAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMulti_PayDayAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 500:
            await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti'")
            await database.setBdData('settings', 'id', "'1'", 'multi_payday', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли множитель PayDay",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 500",
            )
            await Panel7_EditMulti_PayDay(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 500",
        )
        await Panel7_EditMulti_PayDay(message)
        return



async def Panel7_EditMulti_Salary(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti_SalaryAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 🌐 » 🌐 Изменить множитель зарплат\n\n"
                f"📝 Напишите новый множитель зарплат (от 0 до 500)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"1", {"cmd": "admin.Panel7_EditMulti_SalaryAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2", {"cmd": "admin.Panel7_EditMulti_SalaryAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3", {"cmd": "admin.Panel7_EditMulti_SalaryAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4", {"cmd": "admin.Panel7_EditMulti_SalaryAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5", {"cmd": "admin.Panel7_EditMulti_SalaryAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMulti_SalaryAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 500:
            await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti'")
            await database.setBdData('settings', 'id', "'1'", 'multi_salary', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли множитель зарплат",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 500",
            )
            await Panel7_EditMulti_Salary(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 500",
        )
        await Panel7_EditMulti_Salary(message)
        return



async def Panel7_EditMulti_EXP(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti_SalaryAdd'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » ⚙ » 🌐 » 🌐 Изменить множитель EXP\n\n"
                f"📝 Напишите новый множитель EXP (от 0 до 500)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"1", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"2", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"3", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"4", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"5", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"6", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"7", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"8", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"9", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"10", {"cmd": "admin.Panel7_EditMulti_EXPAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel7_EditMulti_EXPAdd(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        if 0 <= count <= 500:
            await database.setUserData(message.from_id, 'state', "'admin.Panel7_EditMulti'")
            await database.setBdData('settings', 'id', "'1'", 'multi_exp', f"'{message.text}'")
            await message.answer(
                message=f"✅ Вы успешно поменяли множитель EXP",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "admin.Panel7_EditMulti"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                    )
                )
            return
        else:
            await message.answer(
                message=f"❌ Укажите число от 0 до 500",
            )
            await Panel7_EditMulti_EXP(message)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число от 0 до 500",
        )
        await Panel7_EditMulti_EXP(message)
        return


# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 6-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel6(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 6:
        await database.setUserData(message.from_id, 'state', "'admin.Panel6'")
        await message.answer(
            message=f"🎯 » 🛠 » 👹 Панель ГА [6]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Изменение правил", {"cmd": "admin.Panel6_EditRules"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return


async def Panel6_EditRules(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 Изменение правил\n\n"
                    f"ℹ Тут вы можете изменить правила вашего сервера, правила для администраторов и FAQ для администраторов",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel6"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📖 Изменить правила сервера", {"cmd": "admin.Panel6_EditRules_RulesServer"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Изменить правила администраторов", {"cmd": "admin.Panel6_EditRules_RulesAdmins"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Изменить FAQ администраторов", {"cmd": "admin.Panel6_EditRules_FAQAdmins"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_RulesServer(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesServer'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить правила сервера\n\n"
                    f"{server_settings[19]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel6_EditRules"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📝 Изменить правила", {"cmd": "admin.Panel6_EditRules_RulesServer_Edit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_RulesServer_Edit(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesServer_EditCheck'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить правила сервера\n\n"
                f"📝 Напишите новые правила сервера (до 3000 символов)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel6_EditRules_RulesServer"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_RulesServer_EditCheck(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesServer_EditCheck'")
    if len(message.text) <= 3000:
        await database.setBdData('settings', 'id', "'1'", 'rules_server', f"'{message.text}'")
        await message.answer(
            message=f"✅ Вы успешно обновили правила сервера"
            )
        await Panel6_EditRules_RulesServer(message)
        return
    else:
        await message.answer(
            message=f"❌ Ошибка. Слишком длинное сообщение"
        )
        await Panel6_EditRules_RulesServer_Edit(message)








async def Panel6_EditRules_RulesAdmins(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesAdmins'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить правила администраторов\n\n"
                    f"{server_settings[17]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel6_EditRules"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📝 Изменить правила", {"cmd": "admin.Panel6_EditRules_RulesAdmins_Edit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_RulesAdmins_Edit(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesAdmins_EditCheck'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить правила администраторов\n\n"
                f"📝 Напишите новые правила для администраторов (до 3000 символов)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel6_EditRules_RulesAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_RulesAdmins_EditCheck(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_RulesAdmins_EditCheck'")
    if len(message.text) <= 3000:
        await database.setBdData('settings', 'id', "'1'", 'regulation_admins', f"'{message.text}'")
        await message.answer(
            message=f"✅ Вы успешно обновили правила для администраторов"
            )
        await Panel6_EditRules_RulesAdmins(message)
        return
    else:
        await message.answer(
            message=f"❌ Ошибка. Слишком длинное сообщение"
        )
        await Panel6_EditRules_RulesAdmins_Edit(message)







async def Panel6_EditRules_FAQAdmins(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_FAQAdmins'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить FAQ администраторов\n\n"
                    f"{server_settings[18]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel6_EditRules"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📝 Изменить правила", {"cmd": "admin.Panel6_EditRules_FAQAdmins_Edit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_FAQAdmins_Edit(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_FAQAdmins_EditCheck'")
    await message.answer(
        message=f"🎯 » 🛠 » 👹 » 📖 » 📖 Изменить FAQ администраторов\n\n"
                f"📝 Напишите новые правила для администраторов (до 3000 символов)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel6_EditRules_FAQAdmins"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
            )
        )
    return


async def Panel6_EditRules_FAQAdmins_EditCheck(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'admin.Panel6_EditRules_FAQAdmins_EditCheck'")
    if len(message.text) <= 3000:
        await database.setBdData('settings', 'id', "'1'", '	faq_admins', f"'{message.text}'")
        await message.answer(
            message=f"✅ Вы успешно обновили правила для администраторов"
            )
        await Panel6_EditRules_FAQAdmins(message)
        return
    else:
        await message.answer(
            message=f"❌ Ошибка. Слишком длинное сообщение"
        )
        await Panel6_EditRules_FAQAdmins_Edit(message)




# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 5-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel5(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 5:
        await database.setUserData(message.from_id, 'state', "'admin.Panel5'")
        await message.answer(
            message=f"🎯 » 🛠 » 🤠 Панель ЗГА [5]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return


# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 4-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel4(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 4:
        await database.setUserData(message.from_id, 'state', "'admin.Panel4'")
        await message.answer(
            message=f"🎯 » 🛠 » 😎 Старший администратор [4]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return



# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 3-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel3(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 3:
        await database.setUserData(message.from_id, 'state', "'admin.Panel3'")
        await message.answer(
            message=f"🎯 » 🛠 » 🙂 Администратор [3]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return


# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 2-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel2(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 2:
        await database.setUserData(message.from_id, 'state', "'admin.Panel2'")
        await message.answer(
            message=f"🎯 » 🛠 » 🤨 Младший администратор [2]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👥 Онлайн игроков", {"cmd": "admin.Panel2_Online"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return


async def Panel2_Online(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel2_Online', temporary_var = '[]'")
    math_count_online = int(time.time())-300
    math_count_1h = int(time.time())-3600
    count_online = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_online}"))
    count_1h = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_1h}"))
    await message.answer(
        message=f"🎯 » 🛠 » 🤨 » 👥 Онлайн игроков\n\n"
                f"👥 Онлайн игроков » {count_online}\n"
                f"🤠 За последний час ботом воспользовалось » {count_1h} человек",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel2"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return



# --------------------------------------------------------------------------------------------------------

# АДМИН ПАНЕЛЬ 1-ОГО УРОВНЯ !!!

# --------------------------------------------------------------------------------------------------------


async def Panel1(message: Message):
    data = await database.getUserData(message.from_id)
    if data[11] >= 1:
        await database.setUserData(message.from_id, 'state', "'admin.Panel1'")
        await message.answer(
            message=f"🎯 » 🛠 » 😀 Хелпер [1]",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💬 Репорт", {"cmd": "admin.Panel1_Report"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("ℹ Статистика игрока", {"cmd": "admin.Panel1_CheckPlayer"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"❌ Нету доступа"
        )
        await Show(message)
        return


async def Panel1_Report(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel1_Report', temporary_var = '[]'")
    data = await database.getUserData(message.from_id)
    report_count = await database.getMultiBdData('report', 'vk_id_admin', "'0'")
    print(len(report_count))
    if len(report_count) == 0:
        await message.answer(
            message=f"🎯 » 🛠 » 😀 » 💬 Репорт\n\n❌ Сейчас нет вопросов в репорт",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "admin.Panel1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("🔄 Обновить", {"cmd": "admin.Panel1_Report"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        print(report_count[0][0])
        await database.setMultiUserData(message.from_id, f"state = 'admin.Panel1_ReportSendReport', temporary_var = '{report_count[0][0]}'")
        await database.setMultiDbData('report', 'id', f"'{report_count[0][0]}'", f"vk_id_admin = '{message.from_id}', nick_admin = '{data[3]}'")
        await message.answer(
            message=f"🎯 » 🛠 » 😀 » 💬 Репорт\n\n"
                    f"@id{report_count[0][1]}({report_count[0][2]}) » {report_count[0][5]}"
        )


async def Panel1_ReportSendReport(message: Message, bot: Bot):
    data = await database.getUserData(message.from_id)
    id_report = data[75]
    await database.setMultiDbData('report', 'id', f"'{id_report}'", f"answer = '{message.text}'")
    report_data = await database.getBdData('report', 'id', f"'{id_report}'")
    await message.answer(
        message='✅ Вы успешно ответили на репорт игрока'
    )
    await database.setUserData(report_data[1], 'state', "'mainMenu.Show'")
    await bot.api.messages.send(
        user_id=report_data[1],
        random_id=random.randint(1, 999999999),
        message=f'👤 Вам ответил администратор @id{message.from_id}({data[3]})\n\n'
                f'Ваш вопрос » {report_data[5]}\n\n'
                f'Ответ @id{message.from_id}(администратора) » {report_data[6]}',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text("👉🏻 Продолжить", payload={"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    await Panel1(message)
    return




async def Panel1_CheckPlayer(message: Message):
    await database.setMultiUserData(message.from_id, "state = 'admin.Panel1_CheckPlayer1', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🛠 » 😀 » ℹ Статистика игрока\n\n📝 Укажите ссылку на пользователя",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "admin.Panel1"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def Panel1_CheckPlayer1(message: Message, bot: Bot):
    try:
        await database.setUserData(message.from_id, 'state', "'admin.Panel1'")
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id
        await database.setUserData(id_user, 'temporary_var', "'[]'")
        server_settings = await database.getBdData('settings', 'id', "'1'")
        data = await database.getUserData(id_user)
        await message.answer(
            message=f"🎯 » 🛠 » 😀 » ℹ Статистика игрока\n\n"
                    f"⚠ Вы просматриваете статистику игрока @id{id_user}({data[3]})\n\n"
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
                    f"💵 Доллары в банке » {await database.pretty(data[16])}\n"
                    f"💶 Евро в банке » {await database.pretty(data[17])}\n"
                    f"💴 Иены в банке » {await database.pretty(data[18])}\n"
                    f"💷 Фунты в банке » {await database.pretty(data[19])}\n\n"
                    f"🛠 Работа » {data[43]}\n"
                    f"🏢 Организация » {data[24]}\n"
                    f"⭐ Уровень розыска » {data[20]}\n\n"
                    f"🅰️ Предупреждения » {data[34]}\n"
                    f"💳 Банковская карта » {data[69]}\n"
                    f"📱 Телефон » {data[5]}\n"
                    f"👑 VIP » {data[22]}\n"
                    f"💰 Фишки казино » {await database.pretty(data[65])}\n"
                    f"💎 Донат » {await database.pretty(data[21])}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Panel1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🔄 Посмотреть еще", {"cmd": "admin.Panel1_CheckPlayer"}),
                color=KeyboardButtonColor.SECONDARY)
                .get_json()
                )
            )
    except Exception as ex:
        await message.answer(
            message=f'⚠ Возникла ошибка при проверки статистики\n\n'
                    f'— Убедитесь, что данный пользователь зарегистрирован в чат-боте.'
        )
        await Panel1_CheckPlayer(message)
    return





# ------------------------------------------------------------------------------------------------------------

# ПРОЧИЕ МЕНЮШКИ ИЗ ГЛАВНОГО МЕНЮ

# ------------------------------------------------------------------------------------------------------------


async def Rules(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Rules'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » 📖 Устав администрации [1]\n\n"
                f"{server_settings[17]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Show2"}), color=KeyboardButtonColor.PRIMARY).get_json()
        )
    )


async def FAQ(message: Message):
    await database.setUserData(message.from_id, 'state', "'admin.Rules'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 🛠 » 📖 FAQ для администрации [1]\n\n"
                f"{server_settings[18]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "admin.Show2"}), color=KeyboardButtonColor.PRIMARY).get_json()
        )
    )


async def toConsole(message: Message):
    await message.answer(
        message=f"📟 Вы перешли в режим консоли.\n\n"
                f"Базовые команды:\n"
                f"/quit — покинуть режим консоли\n"
                f"/mn — перейти в главное меню"
    )
    await database.setUserData(message.from_id, 'state', "'admin.Console'")
    return


async def Console(message: Message, api: API, bot: Bot):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    command = message.text.split(' ')

    if command[0] == '/test' and data[11] >= 8:
        await message.answer(
            message=f"Эхо бот работает!"
        )
        return
    else:
        if command[0] == '/test':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return

    # -------------------------------------------------------------

    if command[0] == '/changenameproject' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        await message.answer(
            message=f'✅ Вы изменили название проекта на "{text}"'
        )
        await database.setBdData('settings', 'id', "'1'", 'name_project', f"'{text}'")
        return
    else:
        if command[0] == '/changenameproject':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/changenameserver' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        await message.answer(
            message=f'✅ Вы изменили название сервера на "{text}"'
        )
        await database.setBdData('settings', 'id', "'1'", 'name_server', f"'{text}'")
        return
    else:
        if command[0] == '/changenameserver':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/setmailingprojectprice' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        if text.isdigit():
            await message.answer(
                message=f'✅ Вы изменили вознаграждение за рассылку новостей проекта'
            )
            await database.setBdData('settings', 'id', "'1'", 'pay_mailing_project', f"'{text}'")
            return
        else:
            await message.answer(
                message=f'❌ Введите корректное число'
            )
    else:
        if command[0] == '/setmailingprojectprice':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/setmailingserverprice' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        if text.isdigit():
            await message.answer(
                message=f'✅ Вы изменили вознаграждение за рассылку новостей сервера'
            )
            await database.setBdData('settings', 'id', "'1'", 'pay_mailing_server', f"'{text}'")
            return
        else:
            await message.answer(
                message=f'❌ Введите корректное число'
            )
    else:
        if command[0] == '/setmailingserverprice':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/changenamegroup' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        await message.answer(
            message=f'✅ Вы изменили название сообщества на "{text}"'
        )
        await bot.api.groups.edit(group_id=message.group_id, title=text)
        return
    else:
        if command[0] == '/changenamegroup':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/changestatusgroup' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        await message.answer(
            message=f'✅ Вы изменили статус сообщества на "{text}"'
        )
        await api.status.set(group_id=message.group_id, text=text)
        return
    else:
        if command[0] == '/changestatusgroup':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/changenamestocks' and data[11] >= 7:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        await message.answer(
            message=f'✅ Вы изменили название акции на "{text}"'
        )
        await database.setBdData('settings', 'id', "'1'", 'name_stocks', f"'{text}'")
        return
    else:
        if command[0] == '/changenamestocks':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/testproject' and data[11] >= 7:
        data = await database.getUserData(message.from_id)
        from_link = command[1]
        group_link = command[2]
        link = from_link[15:]
        today = datetime.date.today()
        now = datetime.datetime.now()
        user_get = await api.users.get(user_ids=link)
        id_user = (user_get[0].id)
        await message.answer(
            message=f'✅ Вы успешно отправили приглашение на тестовый сервер'
        )
        await bot.api.messages.send(
            user_id=id_user,
            random_id=random.randint(1,999999999),
            message='↗ Вам отправлена ссылка на закрытую группу.\n\n'
                    f'⏰ Ссылка действительна до {today.day + 1}.{today.month}.{today.year} {now.hour}:{now.minute}:{now.second}',
            keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Callback("↗ Перейти по приглашению", payload={"cmd": "mainMenu.toLink", "link": group_link}), color=KeyboardButtonColor.SECONDARY)
                .add(Callback("❌ Отказаться", payload={"cmd": "mainMenu.ShowFix"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
        return
    else:
        if command[0] == '/testproject':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return
    # -------------------------------------------------------------

    if command[0] == '/onlineserver' and data[11] >= 2:
        math_count_online = int(time.time()) - 300
        math_count_1h = int(time.time()) - 3600
        count_online = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_online}"))
        count_1h = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_1h}"))
        await message.answer(
            message=f"👥 Онлайн игроков » {count_online}\n"
                    f"🤠 За последний час ботом воспользовалось » {count_1h} человек",
        )
        return
    else:
        if command[0] == '/onlineserver':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/online' and data[11] >= 2:
        math_count_online = int(time.time()) - 300
        count_online = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_online}"))
        await message.answer(
            message=f"👥 Онлайн игроков » {count_online}",
        )
        return
    else:
        if command[0] == '/online':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/houronline' and data[11] >= 2:
        math_count_1h = int(time.time()) - 3600
        count_1h = len(await database.getMultiProgramBdData('users', f"last_message >= {math_count_1h}"))
        await message.answer(
            message=f"🤠 За последний час ботом воспользовалось » {count_1h} человек",
        )
        return
    else:
        if command[0] == '/houronline':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return




    # -------------------------------------------------------------

    if command[0] == '/check' and data[11] >= 1:
        lentext = len(command[0]) + 1
        text = message.text[lentext:]
        try:
            link = text[15:]
            user_get = await bot.api.users.get(user_ids=link)
            id_user = user_get[0].id
            await database.setUserData(id_user, 'temporary_var', "'[]'")
            server_settings = await database.getBdData('settings', 'id', "'1'")
            data = await database.getUserData(id_user)
            await message.answer(
                message=f"📟 » ℹ Статистика игрока\n\n"
                        f"⚠ Вы просматриваете статистику игрока @id{id_user}({data[3]})\n\n"
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
                        f"💵 Доллары в банке » {await database.pretty(data[16])}\n"
                        f"💶 Евро в банке » {await database.pretty(data[17])}\n"
                        f"💴 Иены в банке » {await database.pretty(data[18])}\n"
                        f"💷 Фунты в банке » {await database.pretty(data[19])}\n\n"
                        f"🛠 Работа » {data[43]}\n"
                        f"🏢 Организация » {data[24]}\n"
                        f"⭐ Уровень розыска » {data[20]}\n\n"
                        f"🅰️ Предупреждения » {data[34]}\n"
                        f"💳 Банковская карта » {data[69]}\n"
                        f"📱 Телефон » {data[5]}\n"
                        f"👑 VIP » {data[22]}\n"
                        f"💰 Фишки казино » {await database.pretty(data[65])}\n"
                        f"💎 Донат » {await database.pretty(data[21])}"
            )
        except Exception as ex:
            await message.answer(
                message=f'⚠ Возникла ошибка при проверки статистики\n\n'
                        f'— Убедитесь, что данный пользователь зарегистрирован в чат-боте.'
            )
        return
    else:
        if command[0] == '/check':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/mn' and data[11] >= 1:
        await mainMenu.Show(message)
        return
    else:
        if command[0] == '/mn':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/newmn' and data[11] >= 1:
        await mainMenu.Mini(message)
        return
    else:
        if command[0] == '/newmn':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return


    if command[0] == '/quit' and data[11] >= 1:
        await Show(message)
        return
    else:
        if command[0] == '/quit':
            await message.answer(
                message=f"❌ Нету доступа"
            )
            return

    await message.answer(
        message=f"❌ Неизвестная команда."
    )
    return