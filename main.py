import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes
from modules import registration, database, block, mainMenu, characterAction, skills, game_rule, admin
from modules import historyPunish, historyNicks, passport, licences, settings, report, map, donate, telephone
import json, time, os, random

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
    if count_messages.count == 1:  # если человек первый раз написал, то переходим на регистрацию
        await registration.registration_1(message)
        return

    if message.payload:
        payload = message.payload
        payload = payload.replace("{", "")
        payload = payload.replace("}", "")
        payload = payload.replace('"', "")
        payload = payload.replace(':', "")
        state = f"{payload[3:]}(message)"
        if state == 'admin.Panel8_ControlAdmins_add_set(message)': await admin.Panel8_ControlAdmins_add_set(message, api, bot); return
        if state == 'admin.Panel7_EditData(message)': await admin.Panel7_EditData(message, bot); return
        if state == 'admin.Panel7_EditData_StatusAdd(message)': await admin.Panel7_EditData_StatusAdd(message, api); return
        if state == 'admin.Panel7_EditData_GroupAdd(message)': await admin.Panel7_EditData_GroupAdd(message, bot); return
        if state == 'admin.Panel7_EditData_Group(message)': await admin.Panel7_EditData_Group(message, bot); return
        if state == 'admin.Panel8_ControlAdmins_upp_up(message)': await admin.Panel8_ControlAdmins_upp_up(message, bot); return
        try:
            print(f'payload: {state}')
            await eval(state)
        except Exception as ex:
            print(f'[!] Ошибка: {ex}')
            data = database.getUserData(message.from_id)
            state = f"{data[2]}(message)"
            await eval(state)
    else:
        try:
            data = database.getUserData(message.from_id)
            state = f"{data[2]}(message)"
            if state == 'admin.Panel7_EditData_StatusAdd(message)': await admin.Panel7_EditData_StatusAdd(message, api); return
            if state == 'admin.Panel7_EditData_GroupAdd(message)': await admin.Panel7_EditData_GroupAdd(message, bot); return
            if state == 'admin.Console(message)': await admin.Console(message, api, bot); return
            if state == 'admin.Panel8_ControlAdmins_upp_1(message)': await admin.Panel8_ControlAdmins_upp_1(message, api); return
            print(state)
            await eval(state)
        except Exception as ex:
            await message.answer(
                message=f"😬 Как-то не удобно получилось. У нас возникла ошибка. Сейчас вас отправим в "
                        f"главное меню.")
            print(f'[!] Ошибка: {ex}')
            await mainMenu.Show(message)


@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def handle_message_event(event: GroupTypes.MessageEvent):
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
        await mainMenu.ShowFixFromId(from_id, bot)

    if payloadcmd == 'mainMenu.ShowFix':
        from_id = event.object.user_id
        await mainMenu.ShowFixFromId(from_id, bot)

    if payloadcmd == 'mainMenu.toLink':
        payloadlink = payload['link']
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "open_link", "link": payloadlink}),
        )

print("\033[32m[!] Чат-бот запущен\033[39m")  # Вывод в лог "Работаем" зеленого цвета

bot.run_forever()
