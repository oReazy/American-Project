import asyncio

import logging

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper
from modules import registration, database, mainMenu, characterAction, admin, block, donate, helpGame, game_rule
from modules import historyNicks, historyPunish, report, map, skills, telephone, settings, licences, passport, inventory, family
import json, time, os, sys, re, ast, datetime, random
from modules.newGuysWorks import farm, factory, warehouse
from modules.events import collectors
from modules.importantLocations import LicensingCenter, CentralBank, Pier, SportsHall, EmploymentCenter, CityHall, casino
import traceback

# ------------------------------------------------------------------------------------------

# with open('data/settings.json', 'r', encoding='UTF-8') as json_file:  # получаем файл с настройками
#     DATA = json.load(json_file)  # заносим настройки в файл DATA
#     json_file.close()

# ------------------------------------------------------------------------------------------

bot = Bot(token='aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API(token='52f4cd4631d55713cd43a4634578a60ddb1efd099309876b0f987e58914ad51397dd19e15d2eb0c674f72')
lw = LoopWrapper()



# ------------------------------------------------------------------------------------------

@bot.on.chat_message()
async def besidy(message: Message):
    command = message.text.split(' ')
    try:
        if command[0] == '/id':
            data = await database.getUserData(message.from_id)
            if data[11] >= 5:
                await message.answer(
                    message=f'💬 Индификатор беседы: {message.peer_id}'
                )
            else:
                await message.answer(
                    message=f'❌ Отказано в доступе'
                )

        if command[0] == '/lvl':
            data = await database.getUserData(message.from_id)
            if data[11] >= 5:
                await message.answer(
                    message=f'💬 Ваш уровень доступа: {data[11]}'
                )
            else:
                await message.answer(
                    message=f'❌ Отказано в доступе'
                )
    except Exception as ex:
        await message.answer(
            message=f'❌ Отказано в доступе'
        )
        print(ex)


@bot.on.private_message()
async def main(message: Message):
    count_messages = await bot.api.messages.get_history(
        peer_id=message.from_id)  # получаем кол-во сообщений в переписке
    if count_messages.count == 1 or await database.findBaseData("vk_id",  f"{message.from_id}") == 0:  # если человек первый раз написал, то переходим на регистрацию
        await registration.registration_1(message, bot, api)
    else:
        await database.setMultiUserData(message.from_id, f"last_message = '{int(time.time())}'")
        # await database.setUserData(message.from_id, "last_message", f"'{int(time.time())}'")
        data = await database.getUserData(message.from_id)
        server_data = await database.getBdData('settings', "id", "'1'")
        if int(data[7]) >= int(int(data[6]) * int(server_data[16])):
            await database.def_new_lvl(message, bot, api, data, server_data)
        if message.payload:
            payload = message.payload
            payload = payload.replace("{", "")
            payload = payload.replace("}", "")
            payload = payload.replace('"', "")
            payload = payload.replace(':', "")
            state = f"{payload[3:]}(message, bot, api)"
            # await message.answer(message=f'{state}')
            try:
                # print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Перемещение пользователя: {state}')
                await eval(state)
            except Exception as ex:
                print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}')
                state = f"{data[2]}(message, bot, api)"
                await eval(state)
        else:
            try:
                state = f"{data[2]}(message, bot, api)"
                # print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Перемещение пользователя: {state}')
                await eval(state)
            except Exception as ex:
                await message.answer(
                    message=f"😬 Как-то не удобно получилось. У нас возникла ошибка. Сейчас вас отправим в "
                            f"главное меню.")
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                await mainMenu.Show(message, bot, api)


@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def handle_message_event(event: GroupTypes.MessageEvent):
    await database.setUserData(event.object.user_id, "last_message", f"'{int(time.time())}'")
    payload = event.object.payload
    payloadcmd = payload['cmd']
    if payloadcmd == 'mainMenu.ShowFixFromId':
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "✅ Вы успешно зарегистрировались"}),
        )
        from_id = event.object.user_id
        await bot.api.messages.send(
            user_id=event.object.user_id,
            random_id=random.randint(1, 999999999),
            sticker_id=8441
        )
        await mainMenu.ShowFixFromId(from_id, bot, api)

    if payloadcmd == 'CentralBank.CreateBankCard6':
        from_id = event.object.user_id
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "⭐ Открыты новые возможности"}),
        )
        await CentralBank.CreateBankCard6(from_id, bot)

    if payloadcmd == 'LicensingCenter.ShowBikes':
        from_id = event.object.user_id
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "⭐ Открыты новые возможности"}),
        )
        await LicensingCenter.BikeOpen(from_id, bot)

    if payloadcmd == 'LicensingCenter.Show':
        from_id = event.object.user_id
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "⭐ Открыты новые возможности"}),
        )
        await LicensingCenter.AutoOpen(from_id, bot)


    if payloadcmd == 'CityHall.getPassport':
        from_id = event.object.user_id
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "⭐ Открыты новые возможности"}),
        )
        await CityHall.GetPassport(from_id, bot)


    if payloadcmd == 'mainMenu.ShowFix':
        from_id = event.object.user_id
        await mainMenu.ShowFixFromId(from_id, bot, api)

    if payloadcmd == 'mainMenu.toLink':
        payloadlink = payload['link']
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "open_link", "link": payloadlink}),
        )

    if payloadcmd == 'collectors.beseda':
        event_data = await database.getBdData('event', 'id', "'0'")
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "open_link", "link": f'{event_data[4]}'}),
        )


    if payloadcmd == 'casino.beseda':
        event_data = await database.getBdData('event', 'id', "'1'")
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "open_link", "link": f'{event_data[4]}'}),
        )










async def CreateBeseda(bot: Bot, api: API):
    # ----------------------------- КАЗИНО ----------------------------------------
    event_data = await database.getBdData('event', 'id', "'1'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    new_chat_id = 2000000000 + int(event_data[5])
    try:
        users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27])
        leave_user = 0
        final = int(users.count) - 1
        if final < 198:
            while leave_user < final:
                print(leave_user)
                await bot.api.messages.remove_chat_user(chat_id=event_data[5], user_id=users.profiles[leave_user].id)
                leave_user = leave_user + 1
        else:
            while leave_user < final:
                print(leave_user)
                await bot.api.messages.remove_chat_user(chat_id=event_data[5], user_id=users.profiles[leave_user].id)
                leave_user = leave_user + 1
            users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27])
            leave_user = 0
            final = int(users.count) - 1
            while leave_user < final:
                print(leave_user)
                await bot.api.messages.remove_chat_user(chat_id=event_data[5], user_id=users.profiles[leave_user].id)
                leave_user = leave_user + 1
            users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27])
            leave_user = 0
            final = int(users.count) - 1
            while leave_user < final:
                print(leave_user)
                await bot.api.messages.remove_chat_user(chat_id=event_data[5], user_id=users.profiles[leave_user].id)
                leave_user = leave_user + 1
    except Exception as ex:
        print(
            f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: не удалось удалить беседу "КАЗИНО"\n\n{ex}')

    chat_id = await bot.api.messages.create_chat(
        title=f'American Project | {server_settings[9]} | Казино',
        group_id=server_settings[27]
    )
    print(f'\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Создана беседа "КАЗИНО" с ID: {chat_id}\033[38m')
    new_chat_id = 2000000000 + int(chat_id)
    link = await bot.api.messages.get_invite_link(
        peer_id=2000000000 + int(chat_id),
        reset=1,
        group_id=server_settings[27]
    )
    file = await vkbottle.tools.PhotoChatFaviconUploader(bot.api).upload(chat_id, "images/casino.jpg")
    await bot.api.messages.set_chat_photo(file)
    await database.setBdData('event', 'id', "'1'", 'beseda', f"'{link.link}'")
    await database.setBdData('event', 'id', "'1'", 'chat_id', f"'{chat_id}'")

    # -----------------------------------------------------------------------------


async def Blocked():
    users = await database.getMultiProgramBdData('users', f"state = 'block.Show'")
    for selected in users:
        await bot.api.messages.send(
            user_id=selected[1],
            random_id=random.randint(100000, 999999999),
            peer_id=selected[1],
            message=f'🔄 Был перезагружен сервер\n\n'
                    f'💬 Мы перенесем вас в главное меню, так-как до этого ваши действия были заблокированы.'
        )
        await mainMenu.ShowFixFromId(selected[1], bot, api)



async def CollectorsSpawn2(bot: Bot, api: API):
    await asyncio.sleep(60)
    real_time = datetime.datetime.now()
    if int(real_time.hour) == 20:
        if int(real_time.minute >= 15 and real_time.minute < 59):
            server_settings = await database.getBdData('settings', 'id', "'1'")
            chat_id = await bot.api.messages.create_chat(
                title=f'American Project | {server_settings[9]} | Собиратели',
                group_id=server_settings[27]
            )
            print(f'\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Создана беседа "СОБИРАТЕЛИ" с ID: {chat_id}\033[38m')
            new_chat_id = 2000000000 + int(chat_id)
            link = await bot.api.messages.get_invite_link(
                peer_id=2000000000 + int(chat_id),
                reset = 1,
                group_id=server_settings[27]
            )
            file = await vkbottle.tools.PhotoChatFaviconUploader(bot.api).upload(chat_id, "images/collectors.jpg")
            await bot.api.messages.set_chat_photo(file)
            await database.setBdData('event', 'id', "'0'", 'beseda', f"'{link.link}'")
            await database.setBdData('event', 'id', "'0'", 'chat_id', f"'{chat_id}'")
            await asyncio.sleep(20)
            await database.setBdData('event', 'id', "'0'", 'count', "'60'")
            min = 0
            while min < 50:
                await asyncio.sleep(int(random.randint(40,60)))
                await database.setBdData('event', 'id', "'0'", 'count', "'60'")
                min = min + 1
            await database.setBdData('event', 'id', "'0'", 'count', "'0'")
            await database.setBdData('event', 'id', "'0'", 'playersOnline', "'0'")
            users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27], count=200)
            leave_user = 0
            final = int(users.count) - 1
            if final < 198:
                while leave_user < final:
                    await bot.api.messages.remove_chat_user(chat_id=chat_id, user_id=users.profiles[leave_user].id)
                    leave_user = leave_user + 1
            else:
                while leave_user < final:
                    await bot.api.messages.remove_chat_user(chat_id=chat_id, user_id=users.profiles[leave_user].id)
                    leave_user = leave_user + 1
                users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27], count=200)
                leave_user = 0
                final = int(users.count) - 1
                while leave_user < final:
                    await bot.api.messages.remove_chat_user(chat_id=chat_id, user_id=users.profiles[leave_user].id)
                    leave_user = leave_user + 1
                users = await bot.api.messages.get_conversation_members(peer_id=new_chat_id, group_id=server_settings[27], count=200)
                leave_user = 0
                final = int(users.count) - 1
                while leave_user < final:
                    await bot.api.messages.remove_chat_user(chat_id=chat_id, user_id=users.profiles[leave_user].id)
                    leave_user = leave_user + 1
        else:
            await CollectorsSpawn2(bot, api)
    else:
        await CollectorsSpawn2(bot, api)



async def CollectorsSpawn(bot: Bot, api: API):
    real_time = datetime.datetime.now()
    waited = 60 - int(real_time.second)
    await asyncio.sleep(waited)
    await CollectorsSpawn2(bot, api)



async def PayDay():
    server_data = await database.getBdData('settings', "id", "'1'")
    real_time = datetime.datetime.now()
    payDayRestart = 60 - int(real_time.minute)
    payDayRestart = payDayRestart * 60
    await asyncio.sleep(payDayRestart)
    math_count_online = int(time.time()) - 1200
    real_time = datetime.datetime.now()
    real_time_hour = real_time.hour
    real_time_minute = real_time.minute
    if real_time.hour < 10: real_time_hour = f'0{real_time.hour}'
    if real_time.minute < 10: real_time_minute = f'0{real_time.minute}'
    users = await database.getMultiProgramBdData('users', f"last_message >= {math_count_online}")
    for selected in users:
        exp = int(selected[7])
        lvl = int(selected[6])
        new_exp = exp + (1 * server_data[14])
        await database.setMultiUserData(selected[1], f"exp = '{new_exp}'")
        await bot.api.messages.send(
            user_id=selected[1],
            random_id=random.randint(100000, 999999999),
            peer_id=selected[1],
            message=f'🧾 Банковский чек — {real_time_hour}:{real_time_minute}\n\n'
                    f'💵 Текущая сумма долларов в банке » {await database.pretty(selected[16])}\n'
                    f'💶 Текущая сумма евро в банке » {await database.pretty(selected[17])}\n'
                    f'💴 Текущая сумма иен в банке » {await database.pretty(selected[18])}\n'
                    f'💷 Текущая сумма фунтов в банке » {await database.pretty(selected[19])}\n\n'
                    f'🌐 На данный момент у вас {selected[6]}-й уровень и {new_exp}/{lvl * server_data[16]} очков опыта'
        )

        if new_exp >= (lvl * server_data[16]):
            await database.def_new_lvl_payday(bot, api, selected, server_data, new_exp)
    await asyncio.sleep(50000)
    await PayDay()


print("\n" * 100)
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Чат-бот успешно запущен\033[38m")  # Вывод в лог "Работаем" зеленого цвета
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] PayDay успешно загружен\033[38m")  # Вывод в лог "Работаем" зеленого цвета

# pay_day_loop = asyncio.get_event_loop()
# pay_day_loop.run_until_complete(PayDay())
bot.loop_wrapper.add_task(Blocked())
bot.loop_wrapper.add_task(CreateBeseda(bot, api))
bot.loop_wrapper.add_task(CollectorsSpawn(bot, api))
bot.loop_wrapper.add_task(PayDay())
bot.run_forever() # ЗАПУСКАЕМ БОТА