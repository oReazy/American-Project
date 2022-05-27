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
    await database.setUserData(message.from_id, 'state', "'liderfraction.Show'")
    data_user = await database.getUserData(message.from_id)
    count = await database.findBaseDataSetting('fractions', 'leader', f"'{data_user[3]}'")
    if count > 0:
        data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
        data_fraction_name_rang = ast.literal_eval(data_fraction[5])
        data_fraction_name_rang = list(data_fraction_name_rang)
        await message.answer(
            message=f"🎯 » 👤 » 🤠 Меню лидера\n\n"
                    f"👔 Ваша должность » {data_fraction_name_rang[data_user[23]]} во фракции {data_fraction[1]}\n"
                    f"💳 Банк организации » {await database.pretty(data_fraction[7])} долларов (💵)",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👥 Управление сотрудниками", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📝 Управление должностями", {"cmd": "liderfraction.rangs"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🗂 Собеседования", {"cmd": "liderfraction.Sobes"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer('❌ Вы не являетесь лидером фракции')
        await characterAction.Show(message, bot, api)




async def staff(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    count = await database.findBaseData('member', f"'{data_fraction[1]}'")
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 Управление сотрудниками\n\n"
                f"👥 Количество участников организации » {count}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("👥 Повысить/понизить сотрудника", {"cmd": "liderfraction.staffUpdate"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Выдать/убрать выговор у сотрудника", {"cmd": "liderfraction.staffReprimand"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Уволить сотрудника", {"cmd": "liderfraction.staffFire"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Список сотрудников", {"cmd": "liderfraction.staffList"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def staffFire(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "state = 'liderfraction.staffFire1', temporary_var = ''")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Уволить сотрудника\n\n📝 Введите ссылку на страничку ВКонтакте вашего сотрудника",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )




async def staffFire1(message: Message, bot: Bot, api: API):
    try:
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id

        data_user = await database.getUserData(message.from_id)

        data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

        data = await database.getUserData(id_user)
        if data[22] == f'{data_fraction[1]}':
            await database.setUserData(message.from_id, 'state', "'liderfraction.staffFire2'")
            await database.setUserData(message.from_id, 'temporary_var', f'"{id_user}"')
            await staffFire2(message, bot, api)
        else:
            await message.answer(
                message=f'⚠ Возникла ошибка.\n\n'
                        f'— Данного игрока нет в вашей организации'
            )
            await staffFire(message, bot, api)
    except:
        await message.answer(
            message=f'⚠ Возникла ошибка.\n\n'
                    f'— Данного игрока нет в вашей организации'
        )
        await staffFire(message, bot, api)



async def staffFire2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffFire2'")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Уволить сотрудника\n\n"
                f"ℹ Вы можете уволить сотрудника с ЧС вашей фракции, либо без ЧС",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📄 Просто уволить", {"cmd": "liderfraction.staffFire3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔥 Уволить и занести в ЧС", {"cmd": "liderfraction.staffFire3"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def staffFire3(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    temporary = data[44]
    admin = await database.getUserData(temporary)
    await database.setMultiUserData(temporary, f'warn_fraction = "0"')
    await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=20105)
    await bot.api.messages.send(
        user_id=temporary,
        random_id=random.randint(1, 9999999999),
        message=f"🔥 Вас уволили из организации"
    )
    await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
    await database.setMultiUserData(admin[1], f"state = 'mainMenu.Show', warn_fraction = '0', rang = '0', member = 'Без организации'")
    if message.text == '🔥 Уволить и занести в ЧС':
        blacklist = ast.literal_eval(admin[31])
        blacklist = list(blacklist)

        blacklist.append(f'{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year} — {data[22]}')
        await database.setMultiUserData(admin[1], f'blacklist = "{blacklist}"')
    await message.answer(
        message=f"✅ Вы успешно уволили сотрудника.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🔄 Уволить еще сотрудника", {"cmd": "liderfraction.staffFire"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )





















async def staffReprimand(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "state = 'liderfraction.staffReprimand1', temporary_var = ''")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Выдать/убрать выговор у сотрудника\n\n📝 Введите ссылку на страничку ВКонтакте вашего сотрудника",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )




async def staffReprimand1(message: Message, bot: Bot, api: API):
    try:
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id

        data_user = await database.getUserData(message.from_id)

        data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

        data = await database.getUserData(id_user)
        if data[22] == f'{data_fraction[1]}':
            await database.setUserData(message.from_id, 'state', "'liderfraction.staffReprimand2'")
            await database.setUserData(message.from_id, 'temporary_var', f'"{id_user}"')
            await staffReprimand2(message, bot, api)
        else:
            await message.answer(
                message=f'⚠ Возникла ошибка.\n\n'
                        f'— Данного игрока нет в вашей организации'
            )
            await staffReprimand(message, bot, api)
    except:
        await message.answer(
            message=f'⚠ Возникла ошибка.\n\n'
                    f'— Данного игрока нет в вашей организации'
        )
        await staffReprimand(message, bot, api)



async def staffReprimand2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffReprimand2'")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Повысить/понизить сотрудника\n\n📝 Укажите, что вы хотите сделать с данным сотрудником\n\n"
                f"ℹ Вы можете повысить/понизить сотрудника на один ранг или установить сотруднику новый ранг.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🔽 Убрать", {"cmd": "liderfraction.staffReprimand2_down"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🔥 Выдать", {"cmd": "liderfraction.staffReprimand2_up"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def staffReprimand2_up(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    temporary = data[44]
    admin = await database.getUserData(temporary)
    if admin[53] != 3:
        new_lvl = admin[53] + 1
        await database.setMultiUserData(temporary, f'warn_fraction = "{new_lvl}"')
        await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=68157)
        await bot.api.messages.send(
            user_id=temporary,
            random_id=random.randint(1, 9999999999),
            message=f"🔥 Вы получили выговор. Всего у вас их {new_lvl}"
        )
        if new_lvl == 3:
            await database.setMultiUserData(admin[1], f"state = 'mainMenu.Show', warn_fraction = '0', rang = '0', member = 'Без организации'")
            await bot.api.messages.send(
                user_id=temporary,
                random_id=random.randint(1, 9999999999),
                message=f"⚠ Вы были уволены из организации.",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("🎯 В главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
        await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
        await message.answer(
            message=f"✅ Вы успешно выдали сотруднику выговор. У данного сотрудника теперь {new_lvl} выговоров",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить выговоры у сотрудника", {"cmd": "liderfraction.staffReprimand2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Добавить/убрать у другого", {"cmd": "liderfraction.staffReprimand"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка.\n\n"
                    f"— Вы не можете выдать еще один выговор, так-как у сотрудника их уже 3"
        )
        await staffReprimand2(message, bot, api)




async def staffReprimand2_down(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    temporary = data[44]
    admin = await database.getUserData(temporary)
    if admin[53] != 0:
        new_lvl = admin[53] - 1
        await database.setMultiUserData(temporary, f'warn_fraction = "{new_lvl}"')
        await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=21183)
        await bot.api.messages.send(
            user_id=temporary,
            random_id=random.randint(1, 9999999999),
            message=f"🔽 Вам убрали выговор. Теперь их у вас {new_lvl}."
        )
        await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
        await message.answer(
            message=f"✅ Вы успешно убрали с сотрдуника сотрудника выговор. Теперь у него их {new_lvl}.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить выговоры у сотрудника", {"cmd": "liderfraction.staffReprimand2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Добавить/убрать у другого", {"cmd": "liderfraction.staffReprimand"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка.\n\n"
                    f"— Вы не можете убрать у сотрудника выговор, т.к. у него их 0"
        )
        await staffReprimand2(message, bot, api)



































async def staffList(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffList'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    list = await database.getMultiBdData('users', 'member', f"'{data_fraction[1]}'")
    spisok = ''
    for item in list:
        spisok = f'{spisok}@id{item[1]}({item[3]}) (Ранг: {item[23]}, выговоров: {item[53]}/3)\n'
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 » 👥 Список сотрудников (всего {len(list)})\n\n"
                f"{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("👥 Посмотреть по рангам", {"cmd": "liderfraction.staffListRang"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Самые не активные", {"cmd": "liderfraction.staffListNoActive"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Самые активные", {"cmd": "liderfraction.staffListActive"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )




async def staffListActive(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffListNoActive'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    list = await database.getMultiBdData('users', 'member', f"'{data_fraction[1]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])

    rows = await database.yourSQL(f"SELECT * FROM `users` WHERE member = '{data_fraction[1]}' ORDER BY `users`.`last_message` DESC LIMIT 20;")

    spisok = ''
    for item in rows:
        online = datetime.datetime.utcfromtimestamp(item[46]).strftime('%d.%m.%Y')
        spisok = f'{spisok}⏰ Последняя активность у @id{item[1]}({item[3]}) была {online}\n'

    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 » 👥 » 👥 Самые активные\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staffList"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def staffListNoActive(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffListNoActive'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    list = await database.getMultiBdData('users', 'member', f"'{data_fraction[1]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])

    rows = await database.yourSQL(f"SELECT * FROM `users` WHERE member = '{data_fraction[1]}' ORDER BY `users`.`last_message` ASC LIMIT 20;")

    spisok = ''
    for item in rows:
        online = datetime.datetime.utcfromtimestamp(item[46]).strftime('%d.%m.%Y')
        spisok = f'{spisok}⏰ Последняя активность у @id{item[1]}({item[3]}) была {online}\n'

    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 » 👥 » 👥 Самые не активные\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staffList"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def staffListRang(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffListRang'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    list = await database.getMultiBdData('users', 'member', f"'{data_fraction[1]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])

    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 » 👥 » 👥 Посмотреть по рангам",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staffList"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"[10] {NAME_RANGS[0]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[9] {NAME_RANGS[1]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[8] {NAME_RANGS[2]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[7] {NAME_RANGS[3]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[6] {NAME_RANGS[4]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[5] {NAME_RANGS[5]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[4] {NAME_RANGS[6]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[3] {NAME_RANGS[7]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[2] {NAME_RANGS[8]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[1] {NAME_RANGS[9]}", {"cmd": "liderfraction.staffListRangProsmotr"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def staffListRangProsmotr(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffListRang'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")
    NAME_RANGS = ast.literal_eval(data_fraction[5])
    NAME_RANGS = list(NAME_RANGS)

    if message.text.startswith('[1]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '1'")
        name = f'[1] {NAME_RANGS[9]}'
    if message.text.startswith('[2]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '2'")
        name = f'[2] {NAME_RANGS[8]}'
    if message.text.startswith('[3]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '3'")
        name = f'[3] {NAME_RANGS[7]}'
    if message.text.startswith('[4]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '4'")
        name = f'[4] {NAME_RANGS[6]}'
    if message.text.startswith('[5]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '5'")
        name = f'[5] {NAME_RANGS[5]}'
    if message.text.startswith('[6]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '6'")
        name = f'[6] {NAME_RANGS[4]}'
    if message.text.startswith('[7]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '7'")
        name = f'[7] {NAME_RANGS[3]}'
    if message.text.startswith('[8]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '8'")
        name = f'[8] {NAME_RANGS[2]}'
    if message.text.startswith('[9]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '9'")
        name = f'[9] {NAME_RANGS[1]}'
    if message.text.startswith('[10]'):
        rows = await database.getMultiProgramBdData('users', f"member = '{data_fraction[1]}' AND rang = '10'")
        name = f'[10] {NAME_RANGS[0]}'


    data_user = await database.getUserData(message.from_id)


    spisok = ''
    for item in rows:
        spisok = f'{spisok}, @id{item[1]}({item[3]})'
    spisok = spisok[2:]
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 👥 » 👥 » 👥 » {name}\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.staffListRang"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )




async def staffUpdate(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "state = 'liderfraction.staffUpdateUpp1', temporary_var = ''")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Повысить/понизить сотрудника\n\n📝 Введите ссылку на страничку ВКонтакте вашего сотрудника",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )




async def staffUpdateUpp1(message: Message, bot: Bot, api: API):
    try:
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id

        data_user = await database.getUserData(message.from_id)

        data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

        data = await database.getUserData(id_user)
        if data[22] == f'{data_fraction[1]}':
            await database.setUserData(message.from_id, 'state', "'liderfraction.staffUpdateUpp2'")
            await database.setUserData(message.from_id, 'temporary_var', f'"{id_user}"')
            await staffUpdateUpp2(message, bot, api)
        else:
            await message.answer(
                message=f'⚠ Возникла ошибка при повышении/понижении сотрудника.\n\n'
                        f'— Данного игрока нет в вашей организации'
            )
            await staffUpdate(message, bot, api)
    except:
        await message.answer(
            message=f'⚠ Возникла ошибка при повышении/понижении сотрудника.\n\n'
                    f'— Данного игрока нет в вашей организации'
        )
        await staffUpdate(message, bot, api)



async def staffUpdateUpp2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.staffUpdateUpp2_set'")
    await message.answer(
        message=f"🎯 » 👤 » 👥 » 👥 Повысить/понизить сотрудника\n\n📝 Укажите, что вы хотите сделать с данным сотрудником\n\n"
                f"ℹ Вы можете повысить/понизить сотрудника на один ранг или установить сотруднику новый ранг.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Повысить", {"cmd": "liderfraction.staffUpdateUpp2_up"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Понизить", {"cmd": "liderfraction.staffUpdateUpp2_down"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("1", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("3", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("4", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("6", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("7", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("8", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("9", {"cmd": "liderfraction.staffUpdateUpp2_set"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )




async def staffUpdateUpp2_set(message: Message, bot: Bot, api: API):
    if message.text.isdigit():
        new_lvl = int(message.text)
        if 1 <= new_lvl <= 9:
            data = await database.getUserData(message.from_id)
            temporary = data[44]
            admin = await database.getUserData(temporary)
            await database.setMultiUserData(temporary, f'rang = "{new_lvl}"')
            await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=1933)
            await bot.api.messages.send(
                user_id=temporary,
                random_id=random.randint(1, 9999999999),
                message=f"Вам изменили ранг на {new_lvl} во фракции.\n\n"
            )
            await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
            await message.answer(
                message=f"✅ Вы успешно повысили сотрудника до {new_lvl} ранга.",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("📝 Изменить ранг этого сотрудника", {"cmd": "liderfraction.staffUpdateUpp2"}), color=KeyboardButtonColor.SECONDARY)
                        .add(Text("🔄 Повысить/понизить другого", {"cmd": "liderfraction.staffUpdate"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
        else:
            await message.answer(
                message=f"❌ Введите число от 1 до 9"
            )
            await staffUpdateUpp2(message, bot, api)




async def staffUpdateUpp2_up(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    temporary = data[44]
    admin = await database.getUserData(temporary)
    if admin[11] != 9:
        new_lvl = admin[23] + 1
        await database.setMultiUserData(temporary, f'rang = "{new_lvl}"')
        await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=1933)
        await bot.api.messages.send(
            user_id=temporary,
            random_id=random.randint(1, 9999999999),
            message=f"⏫ Поздравляем, вас повысили до {new_lvl} ранга во фракции"
        )
        await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
        await message.answer(
            message=f"✅ Вы успешно повысили сотрудника до {new_lvl} ранга.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить ранг этого сотрудника", {"cmd": "liderfraction.staffUpdateUpp2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Повысить/понизить другого", {"cmd": "liderfraction.staffUpdate"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка.\n\n"
                    f"— Вы не можете повысить сотрудника, т.к. у него 9 ранг"
        )
        await staffUpdateUpp2(message, bot, api)




async def staffUpdateUpp2_down(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    temporary = data[44]
    admin = await database.getUserData(temporary)
    if admin[11] != 1:
        new_lvl = admin[23] - 1
        await database.setMultiUserData(temporary, f'rang = "{new_lvl}"')
        await bot.api.messages.send(user_id=temporary, random_id=random.randint(1, 9999999999), sticker_id=50454)
        await bot.api.messages.send(
            user_id=temporary,
            random_id=random.randint(1, 9999999999),
            message=f"⏬ Увы, вас понизили до {new_lvl} ранга во фракции"
        )
        await database.setUserData(message.from_id, 'state', "'liderfraction.staff'")
        await message.answer(
            message=f"✅ Вы успешно понизили сотрудника до {new_lvl} ранга.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "liderfraction.staff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📝 Изменить ранг этого сотрудника", {"cmd": "liderfraction.staffUpdateUpp2"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔄 Повысить/понизить другого", {"cmd": "liderfraction.staffUpdate"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"'⚠ Возникла ошибка.\n\n"
                    f"— Вы не можете понизить сотрудника, т.к. у него 1 ранг"
        )
        await staffUpdateUpp2(message, bot, api)













async def rangs(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.rangs'")
    data_user = await database.getUserData(message.from_id)
    count = await database.findBaseDataSetting('fractions', 'leader', f"'{data_user[3]}'")

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])
    NAME_RANGS = list(NAME_RANGS)

    SALARY_RANGS = ast.literal_eval(data_fraction[6])
    SALARY_RANGS = list(SALARY_RANGS)
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 📝 Управление должностями\n\n"
                f"10 ранг — {NAME_RANGS[0]} — зарплата {await database.pretty(SALARY_RANGS[0])} долларов (💵)\n"
                f"9 ранг — {NAME_RANGS[1]} — зарплата {await database.pretty(SALARY_RANGS[1])} долларов (💵)\n"
                f"8 ранг — {NAME_RANGS[2]} — зарплата {await database.pretty(SALARY_RANGS[2])} долларов (💵)\n"
                f"7 ранг — {NAME_RANGS[3]} — зарплата {await database.pretty(SALARY_RANGS[3])} долларов (💵)\n"
                f"6 ранг — {NAME_RANGS[4]} — зарплата {await database.pretty(SALARY_RANGS[4])} долларов (💵)\n"
                f"5 ранг — {NAME_RANGS[5]} — зарплата {await database.pretty(SALARY_RANGS[5])} долларов (💵)\n"
                f"4 ранг — {NAME_RANGS[6]} — зарплата {await database.pretty(SALARY_RANGS[6])} долларов (💵)\n"
                f"3 ранг — {NAME_RANGS[7]} — зарплата {await database.pretty(SALARY_RANGS[7])} долларов (💵)\n"
                f"2 ранг — {NAME_RANGS[8]} — зарплата {await database.pretty(SALARY_RANGS[8])} долларов (💵)\n"
                f"1 ранг — {NAME_RANGS[9]} — зарплата {await database.pretty(SALARY_RANGS[9])} долларов (💵)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📝 Изменить название ранга", {"cmd": "liderfraction.rangsEditRang"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Изменить зарплату ранга", {"cmd": "liderfraction.rangsEditSalary"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )




async def rangsEditSalary(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.rangsEditSalary'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])
    NAME_RANGS = list(NAME_RANGS)
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 📝 » 📝 Изменить зарплату ранга\n\n"
                f"⤵ Выберите ранг, который хотите отредактировать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.rangs"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"[10] {NAME_RANGS[0]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[9] {NAME_RANGS[1]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}),  color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[8] {NAME_RANGS[2]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[7] {NAME_RANGS[3]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[6] {NAME_RANGS[4]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[5] {NAME_RANGS[5]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[4] {NAME_RANGS[6]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[3] {NAME_RANGS[7]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[2] {NAME_RANGS[8]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[1] {NAME_RANGS[9]}", {"cmd": "liderfraction.rangsEditSalaryEdit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def rangsEditSalaryEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.rangsEditSalaryEditCheck'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    if message.text.startswith('[1]'):
        await database.setUserData(message.from_id, 'temporary_var', "'9'")
    if message.text.startswith('[2]'):
        await database.setUserData(message.from_id, 'temporary_var', "'8'")
    if message.text.startswith('[3]'):
        await database.setUserData(message.from_id, 'temporary_var', "'7'")
    if message.text.startswith('[4]'):
        await database.setUserData(message.from_id, 'temporary_var', "'6'")
    if message.text.startswith('[5]'):
        await database.setUserData(message.from_id, 'temporary_var', "'5'")
    if message.text.startswith('[6]'):
        await database.setUserData(message.from_id, 'temporary_var', "'4'")
    if message.text.startswith('[7]'):
        await database.setUserData(message.from_id, 'temporary_var', "'3'")
    if message.text.startswith('[8]'):
        await database.setUserData(message.from_id, 'temporary_var', "'2'")
    if message.text.startswith('[9]'):
        await database.setUserData(message.from_id, 'temporary_var', "'1'")
    if message.text.startswith('[10]'):
        await database.setUserData(message.from_id, 'temporary_var', "'0'")

    data_user = await database.getUserData(message.from_id)
    SALARY_RANGS = ast.literal_eval(data_fraction[6])
    SALARY_RANGS = list(SALARY_RANGS)
    await message.answer(
        message=f"📝 Напишите новую зарплату для данного ранга\n\n"
                f"▶ В данный момент стоит зарплата » {SALARY_RANGS[int(data_user[44])]} долларов (💵)\n\n"
                f"ℹ Укажите новую зарплату от 1 до 200 000 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.rangsEditRang"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def rangsEditSalaryEditCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    SALARY_RANGS = ast.literal_eval(data_fraction[6])
    SALARY_RANGS = list(SALARY_RANGS)

    text = message.text.replace("\n", "")
    text = text.replace("\r", "")

    if text.isdigit():
        if 0 < int(text) <= 200000:
            SALARY_RANGS[int(data_user[44])] = message.text
            await database.setBdData('fractions', 'id', "'6'", 'SALARY_RANGS', f'\"{SALARY_RANGS}\"')
            await message.answer(f'✅ Вы успешно поменяли название ранга на {message.text}')
            await rangsEditRang(message, bot, api)
        else:
            await message.answer('❌ Ошибка. Укажите зарплату от 1 до 200 000 долларов (💵)')
            await rangsEditRang(message, bot, api)
    else:
        await message.answer('❌ Ошибка. Введите число')
        await rangsEditRang(message, bot, api)

















async def rangsEditRang(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.rangsEditRang'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])
    NAME_RANGS = list(NAME_RANGS)
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 📝 » 📝 Изменить название ранга\n\n"
                f"⤵ Выберите ранг, который хотите отредактировать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.rangs"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"[10] {NAME_RANGS[0]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[9] {NAME_RANGS[1]}", {"cmd": "liderfraction.rangsEditRangEdit"}),  color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[8] {NAME_RANGS[2]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[7] {NAME_RANGS[3]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[6] {NAME_RANGS[4]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[5] {NAME_RANGS[5]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[4] {NAME_RANGS[6]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[3] {NAME_RANGS[7]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text(f"[2] {NAME_RANGS[8]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text(f"[1] {NAME_RANGS[9]}", {"cmd": "liderfraction.rangsEditRangEdit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def rangsEditRangEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.rangsEditRangEditCheck'")
    data_user = await database.getUserData(message.from_id)

    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    if message.text.startswith('[1]'):
        await database.setUserData(message.from_id, 'temporary_var', "'9'")
    if message.text.startswith('[2]'):
        await database.setUserData(message.from_id, 'temporary_var', "'8'")
    if message.text.startswith('[3]'):
        await database.setUserData(message.from_id, 'temporary_var', "'7'")
    if message.text.startswith('[4]'):
        await database.setUserData(message.from_id, 'temporary_var', "'6'")
    if message.text.startswith('[5]'):
        await database.setUserData(message.from_id, 'temporary_var', "'5'")
    if message.text.startswith('[6]'):
        await database.setUserData(message.from_id, 'temporary_var', "'4'")
    if message.text.startswith('[7]'):
        await database.setUserData(message.from_id, 'temporary_var', "'3'")
    if message.text.startswith('[8]'):
        await database.setUserData(message.from_id, 'temporary_var', "'2'")
    if message.text.startswith('[9]'):
        await database.setUserData(message.from_id, 'temporary_var', "'1'")
    if message.text.startswith('[10]'):
        await database.setUserData(message.from_id, 'temporary_var', "'0'")
    await message.answer(
        message=f"📝 Напишите новое название для ранга",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.rangsEditRang"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def rangsEditRangEditCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    NAME_RANGS = ast.literal_eval(data_fraction[5])
    NAME_RANGS = list(NAME_RANGS)

    text = message.text.replace("\n", "")
    text = text.replace("\r", "")

    if len(text) <= 40:
        NAME_RANGS[int(data_user[44])] = message.text
        await database.setBdData('fractions', 'id', "'6'", 'NAME_RANGS', f'\"{NAME_RANGS}\"')
        await message.answer(f'✅ Вы успешно поменяли название ранга на {message.text}')
        await rangsEditRang(message, bot, api)
    else:
        await message.answer('❌ Ошибка. Название ранга не должно превышать 40 символов')
        await rangsEditRang(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

async def Sobes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.Sobes'")
    data_user = await database.getUserData(message.from_id)
    count = await database.findBaseDataSetting('fractions', 'leader', f"'{data_user[3]}'")
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    data_fraction_resumes = ast.literal_eval(data_fraction[9])
    data_fraction_resumes = list(data_fraction_resumes)

    if data_fraction[8] == 0:
        TextOpenSobes = '🟥 Собеседование во фракцию закрыто'
        TextButton = '🟩 Открыть заявки на собеседование'
    if data_fraction[8] == 1:
        TextOpenSobes = '🟩 Собеседование во фракцию открыто'
        TextButton = '🟥 Закрыть заявки на собеседование'
    await message.answer(
        message=f"🎯 » 👤 » 🤠 » 🗂 Собеседования\n\n"
                f"📄 Собеседование » {TextOpenSobes}\n"
                f"📄 Всего необработанных резюме » {len(data_fraction_resumes)} шт.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "liderfraction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"{TextButton}", {"cmd": "liderfraction.SobesSwitch"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📄 Просмотр резюме", {"cmd": "liderfraction.ShowResume"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ShowResume(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'liderfraction.ShowResume'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    data_fraction_resumes = ast.literal_eval(data_fraction[9])
    data_fraction_resumes = list(data_fraction_resumes)

    print(data_fraction_resumes)
    if len(data_fraction_resumes) != 0:
        await message.answer(
            message=f"🎯 » 👤 » 🤠 » 🗂 » 📄 Просмотр резюме\n\n"
                    f"📄 Резюме от @id{data_fraction_resumes[0][0]}({data_fraction_resumes[0][2]}), живет {data_fraction_resumes[0][3]} лет в штате\n\n"
                    f"{data_fraction_resumes[0][1]}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "liderfraction.Sobes"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text(f"Принять", {"cmd": "liderfraction.SobesOK"}), color=KeyboardButtonColor.POSITIVE)
                    .add(Text(f"Отказать", {"cmd": "liderfraction.SobesFalse"}), color=KeyboardButtonColor.NEGATIVE)
                    .get_json()
            )
        )
    else:
        await message.answer('❌ Отсутствуют резюме для проверки или они закончились')
        await Sobes(message, bot, api)


async def SobesOK(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    data_fraction_resumes = ast.literal_eval(data_fraction[9])
    data_fraction_resumes = list(data_fraction_resumes)

    user_resume = data_fraction_resumes[0][0]
    user_resume = await database.getUserData(user_resume)

    if user_resume[22] == 'Без организации':
        await message.answer('✅ Вы успешно приняли игрока во фракцию')
        await database.setUserData(data_fraction_resumes[0][0], 'member', f"'{data_fraction[1]}'")
        await database.setUserData(data_fraction_resumes[0][0], 'rang', f"'1'")
        await bot.api.messages.send(
            user_id=data_fraction_resumes[0][0],
            random_id=random.randint(1, 999999999),
            message=f"✅ Вас приняли во фракцию {data_fraction[1]}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🎯 Главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💻 Панель работника", {"cmd": "radiostation.JobPanel"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        data_fraction_resumes.pop(0)
        await database.setBdData('fractions', 'id', "'6'", 'resumes', f'\"{data_fraction_resumes}\"')
        await ShowResume(message, bot, api)
    else:
        await message.answer('❌ Игрок находится уже в другой организации, удаляем резюме...')
        data_fraction_resumes.pop(0)
        await database.setBdData('fractions', 'id', "'6'", 'resumes', f'\"{data_fraction_resumes}\"')
        await ShowResume(message, bot, api)


async def SobesFalse(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    data_fraction_resumes = ast.literal_eval(data_fraction[9])
    data_fraction_resumes = list(data_fraction_resumes)

    await message.answer('✅ Вы успешно отклонили резюме')
    data_fraction_resumes.pop(0)
    print(data_fraction_resumes)
    await database.setBdData('fractions', 'id', "'6'", 'resumes', f'\"{data_fraction_resumes}\"')
    await ShowResume(message, bot, api)


async def SobesSwitch(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'leader', f"'{data_user[3]}'")

    if data_fraction[8] == 0:
        await database.setBdData('fractions', 'id', "'6'", 'open_sobes', "'1'")
    if data_fraction[8] == 1:
        await database.setBdData('fractions', 'id', "'6'", 'open_sobes', "'0'")

    await message.answer('✅ Вы успешно сменили статус собеседования')
    await Sobes(message, bot, api)
