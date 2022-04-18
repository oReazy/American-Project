# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper
import json, time, os, sys, re, ast, datetime, random, traceback
from vkbottle import Callback, GroupEventType, GroupTypes, Keyboard

# ----------------------------------------------------------------------------------------------------------------------

from modules import registration, database, mainMenu, characterAction, donate, family, game_rule, helpGame, historyNicks, historyPunish
from modules import inventory, licences, passport, report, settings, map, skills, telephone, admin

from modules.importantLocations import CentralBank, CityHall, EmploymentCenter, LicensingCenter, Pier, SportsHall, casino
from modules.newGuysWorks import farm, factory, warehouse

# ----------------------------------------------------------------------------------------------------------------------

bot = Bot('bot token')
api = API('api')
lw = LoopWrapper()

# ----------------------------------------------------------------------------------------------------------------------

# СООБЩЕНИЯ ИЗ БЕСЕДЕ
@bot.on.chat_message()
async def besidy(message: Message):
    await message.answer(
        message=f'❌ В данный момент нельзя запустить чат-бот в беседе!'
    )


# ----------------------------------------------------------------------------------------------------------------------

# СООБЩЕНИЯ ОТ ЛИЧНЫХ ПЕРЕПИСОК ЧАТ-БОТА
@bot.on.private_message()
async def main(message: Message):
    count_messages = await bot.api.messages.get_history(peer_id=message.from_id)  # получаем кол-во сообщений в переписке
    if count_messages.count == 1 or await database.findBaseData("vk_id", f"{message.from_id}") == 0:  # если человек первый раз написал, то переходим на регистрацию
        await registration.registration_1(message, bot, api)
    else:
        await database.setMultiUserData(message.from_id, f"last_message = '{int(time.time())}'") # УСТАНАВЛИВАЕМ ВРЕМЯ ПОСЛЕДНЕГО СООБЩЕНИЯ
        data = await database.getUserData(message.from_id) # ПОЛУЧАЕМ ДАННЫЕ ИГРОКА
        server_data = await database.getBdData('settings', "id", "'1'") # ПОЛУЧАЕМ ДАННЫЕ СЕРВЕРА
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
                print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
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

# ----------------------------------------------------------------------------------------------------------------------


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
        new_exp = exp + (1 * server_data[25])
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

        if new_exp >= (lvl * server_data[20]):
            await database.def_new_lvl_payday(bot, api, selected, server_data, new_exp)
    await asyncio.sleep(3600)
    await PayDay()

# ----------------------------------------------------------------------------------------------------------------------


print("\n" * 100)
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Чат-бот успешно запущен\033[38m")
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] PayDay успешно загружен\033[38m")
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Blocked успешно запущен\033[38m")
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Работы успешно запущены\033[38m")
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Админка успешно запущена\033[38m")


# ----------------------------------------------------------------------------------------------------------------------

bot.loop_wrapper.add_task(Blocked())
bot.loop_wrapper.add_task(PayDay())

# ----------------------------------------------------------------------------------------------------------------------

bot.run_forever()


