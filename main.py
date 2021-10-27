import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes
from modules import registration, database, mainMenu, characterAction, admin, block, donate, helpGame, game_rule
from modules import historyNicks, historyPunish, report, map, skills, telephone, settings, licences, passport
import json, time, os, sys, re, ast, datetime, random
# from modules.newGuysWorks import farm

# ------------------------------------------------------------------------------------------

with open('data/settings.json', 'r', encoding='UTF-8') as json_file:  # получаем файл с настройками
    DATA = json.load(json_file)  # заносим настройки в файл DATA

# ------------------------------------------------------------------------------------------

bot = Bot(token=DATA['token_group'])
api = API(token=DATA['token_user'])

# ------------------------------------------------------------------------------------------

@bot.on.message()
async def main(message: Message):
    count_messages = await bot.api.messages.get_history(
        peer_id=message.from_id)  # получаем кол-во сообщений в переписке
    if count_messages.count == 1 or await database.findBaseData("vk_id", f"{message.from_id}") == 0:  # если человек первый раз написал, то переходим на регистрацию
        await registration.registration_1(message, bot, api)
        return

    await database.setUserData(message.from_id, "last_message", f"'{int(time.time())}'")
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
            print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}')
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

print("\n" * 100)
print("\033[38m[\033[32m!\033[38m][\033[33mDEBUG\033[38m] Чат-бот успешно запущен\033[38m")  # Вывод в лог "Работаем" зеленого цвета

bot.run_forever()