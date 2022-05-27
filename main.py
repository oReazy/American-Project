# ----------------------------------------------------------------------------------------------------------------------

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, ast, states
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper
import json, time, datetime, random, traceback
from vkbottle import GroupEventType

from modules import registration, database, mainMenu, characterAction, donate, family, game_rule, helpGame, historyNicks, historyPunish
from modules import inventory, licences, passport, report, settings, map, skills, telephone, admin, block, excursion, liderfraction

from modules.importantLocations import CentralBank, CityHall, EmploymentCenter, LicensingCenter, Pier, SportsHall, casino, CentralMarket
from modules.newGuysWorks import farm, factory, warehouse, delivery
from modules.events import collectors
from modules.fractions import radiostation

# ----------------------------------------------------------------------------------------------------------------------

bot = Bot('aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API('25a06c2cbdd3d2788f0af4bc75c6c4b5ede3e807d16143eafe0e03ff286ac2089760a2d7da9ac8b1a9415')
lw = LoopWrapper()

# ----------------------------------------------------------------------------------------------------------------------

# Стейты и их переходы.
functions = states.STATES

# ----------------------------------------------------------------------------------------------------------------------

# Обработка сообщений из бесед.
@bot.on.chat_message()
async def besidy(message: Message):
    await message.answer(
        message=f'❌ В данный момент нельзя запустить чат-бот в беседе!'
    )


# ----------------------------------------------------------------------------------------------------------------------

# Обработка сообщений из личных сообщений сообщества.
@bot.on.private_message()
async def main(message: Message):

    # Получаем количество сообщений в переписке.
    count_messages = await bot.api.messages.get_history(peer_id=message.from_id)

    # Проверяем, есть ли игрок в базе данных, если нет, то переходим этап регистрации.
    if count_messages.count == 1 or await database.findBaseData("vk_id", f"{message.from_id}") == 0:
        await registration.registration_1(message, bot, api)
    else:
        # Если игрок зарегистрирован в чат-боте, то обновляем переменную последнего написанного сообщения.
        await database.setMultiUserData(message.from_id, f"last_message = '{int(time.time())}'")

        # Получаем данные игрока, чтобы работать с ними в дальнейшем.
        data = await database.getUserData(message.from_id)

        # -----------------------------------------------------------------

        # Проверяем VIP, истекла ли она или нет.
        vip_data = ast.literal_eval(data[21])
        vip_data = list(vip_data)
        if vip_data[0] != 'no vip':
            if vip_data[1] != 10:
                if vip_data[1] < int(time.time()):
                    vip_data[1] = 0
                    vip_data[0] = 'no vip'
                    await database.setMultiUserData(message.from_id, f'VIP = "{vip_data}"')
                    await message.answer(
                        message=f"🔔 Время действия вашего VIP закончилось. Теперь у вас нет VIP")

        # -----------------------------------------------------------------

        # Переход к активному стейту.
        if message.payload:
            payload = message.payload
            payload = payload.replace("{", "")
            payload = payload.replace("}", "")
            payload = payload.replace('"', "")
            payload = payload.replace(':', "")
            state = f"{payload[3:]}"
            try:
                await functions[state](message, bot, api)
            except Exception as ex:
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                state = f"{data[2]}"
                await functions[state](message, bot, api)
        else:
            try:
                state = f"{data[2]}"
                # print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Перемещение пользователя: {state}')
                await functions[state](message, bot, api)
            except Exception as ex:
                await message.answer(message=f"😬 Как-то не удобно получилось. У нас возникла ошибка. Сейчас вас отправим в главное меню.")
                print( f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                await mainMenu.Show(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Обработка RAW эвентов от Callback-кнопок.
@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=MessageEvent)
async def handle_message_event(event: MessageEvent):

    # Обновляем переменную last_message, добавляя время последнего сообщения от пользователя.
    await database.setUserData(event.object.user_id, "last_message", f"'{int(time.time())}'")

    # Вынимаем объект payload.
    payload = event.object.payload
    payloadcmd = payload['cmd']

    # Проверяем условия.
    if payloadcmd == 'mainMenu.ShowFixFromId':
        await event.show_snackbar("✅ Вы успешно зарегистрировались")
        from_id = event.object.user_id
        await bot.api.messages.send(
            user_id=event.object.user_id,
            random_id=random.randint(1, 999999999),
            sticker_id=8441
        )
        await registration.registration_9_1(event, bot, api)

    if payloadcmd == 'CentralBank.CreateBankCard6':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await CentralBank.CreateBankCard6(from_id, bot)

    if payloadcmd == 'LicensingCenter.ShowBikes':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await LicensingCenter.BikeOpen(from_id, bot)

    if payloadcmd == 'LicensingCenter.Show':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await LicensingCenter.AutoOpen(from_id, bot)


    if payloadcmd == 'CityHall.getPassport':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
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
        zarplata = selected[16]
        if selected[22] != 'Без организации':
            data_fraction = await database.getBdData('fractions', 'name', f"'{selected[22]}'")
            data_faction = ast.literal_eval(data_fraction[6])
            data_faction = list(data_faction)
            if selected[23] == 1: vibor_zp = 9
            if selected[23] == 2: vibor_zp = 8
            if selected[23] == 3: vibor_zp = 7
            if selected[23] == 4: vibor_zp = 6
            if selected[23] == 5: vibor_zp = 5
            if selected[23] == 6: vibor_zp = 4
            if selected[23] == 7: vibor_zp = 3
            if selected[23] == 8: vibor_zp = 2
            if selected[23] == 9: vibor_zp = 1
            if selected[23] == 10: vibor_zp = 0
            zarplata = selected[16] + int(data_faction[vibor_zp])
            await database.setUserData(selected[1], 'bank_dollars', f"'{zarplata}'")
        exp = int(selected[7])
        lvl = int(selected[6])
        new_exp = exp + (1 * server_data[25])
        await database.setMultiUserData(selected[1], f"exp = '{new_exp}'")
        await bot.api.messages.send(
            user_id=selected[1],
            random_id=random.randint(100000, 999999999),
            peer_id=selected[1],
            message=f'🧾 Банковский чек — {real_time_hour}:{real_time_minute}\n\n'
                    f'💵 Текущая сумма долларов в банке » {await database.pretty(zarplata)}\n'
                    f'💶 Текущая сумма евро в банке » {await database.pretty(selected[17])}\n'
                    f'💴 Текущая сумма иен в банке » {await database.pretty(selected[18])}\n'
                    f'💷 Текущая сумма фунтов в банке » {await database.pretty(selected[19])}\n\n'
                    f'🌐 На данный момент у вас {selected[6]}-й уровень и {new_exp}/{lvl * server_data[20]} очков опыта'
        )

        if new_exp >= (lvl * server_data[20]):
            await database.def_new_lvl_payday(bot, api, selected, server_data, new_exp)
    await asyncio.sleep(3600)
    await PayDay()

# ----------------------------------------------------------------------------------------------------------------------


async def CollectorsSpawn2(bot: Bot, api: API):
    await asyncio.sleep(60)
    real_time = datetime.datetime.now()
    if int(real_time.hour) == 20:
        if int(15 <= real_time.minute < 59):
            server_settings = await database.getBdData('settings', 'id', "'1'")
            await asyncio.sleep(20)
            await database.setBdData('event', 'id', "'0'", 'playersOnline', "'0'")
            await database.setBdData('event', 'id', "'0'", 'count', "'60'")
            min = 0
            while min < 50:
                await asyncio.sleep(int(random.randint(40, 60)))
                await database.setBdData('event', 'id', "'0'", 'count', "'60'")
                min = min + 1
            await database.setBdData('event', 'id', "'0'", 'count', "'0'")
            await database.setBdData('event', 'id', "'0'", 'playersOnline', "'0'")
        else:
            await CollectorsSpawn2(bot, api)
    else:
        await CollectorsSpawn2(bot, api)



async def CollectorsSpawn(bot: Bot, api: API):
    real_time = datetime.datetime.now()
    waited = 60 - int(real_time.second)
    await asyncio.sleep(waited)
    await CollectorsSpawn2(bot, api)



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
bot.loop_wrapper.add_task(CollectorsSpawn(bot, api))

# ----------------------------------------------------------------------------------------------------------------------

bot.run_forever()


