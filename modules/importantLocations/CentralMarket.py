# ----------------------------------------------------------------------------------------------------------------------

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ----------------------------------------------------------------------------------------------------------------------

import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database, map

# ----------------------------------------------------------------------------------------------------------------------

# Центральный рынок.

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):

    data_user = await database.getUserData(message.from_id)
    # Показываем интерфейс центрального рынка.
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Show'")

    # Получаем данные с центрального рынка.
    data_markerts = await database.yourSQL('SELECT * FROM `centralmarket` WHERE 1')

    # Создаем клавиатуру для лавок.
    KEYBOARD = Keyboard(one_time=True, inline=False)
    KEYBOARD.add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD.add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.row()

    # Далее проиходит проверка лавок (если лавка занята, то будет белая кнопка, иначе красная).
    if data_markerts[0][1] == 'free':
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[1][1] == 'free':
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[2][1] == 'free':
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[3][1] == 'free':
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if data_markerts[4][1] == 'free':
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[5][1] == 'free':
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[6][1] == 'free':
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[7][1] == 'free':
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if data_markerts[8][1] == 'free':
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[9][1] == 'free':
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[10][1] == 'free':
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[11][1] == 'free':
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()
    KEYBOARD.add(Text("➕ Арендовать лавку", {"cmd": "CentralMarket.Arenda"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.get_json()

    # Отпраляем человеку сообщение с составленной клавиатурой.
    await message.answer('🎯 » 🗺 » 🏛 » 🏰 Центральный рынок', keyboard=KEYBOARD)

# ----------------------------------------------------------------------------------------------------------------------

# Лавка игрока (универсальный скрипт для всех лавок).
async def Lavka(message: Message, bot: Bot, api: API):

    # Устанавливаем пользователю стейт, если он напишет постореннее сообщение.
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Show'")

    # Получаем номер лавки.
    number_market = int(message.text[3:])

    # Получаем данные от лавки
    data_market = await database.getBdData('centralmarket', 'id', f"'{number_market}'")
    data_market_items = ast.literal_eval(data_market[2])
    data_market_items = list(data_market_items)

    # Если лавка пустая, то выдаем ошибку и делаем переход на главное окно центрального рынка.
    if data_market[1] == 'free':
        await message.answer('❌ В данной лавке никто не продает')
        await Show(message, bot, api)
        return

    # Если продавец редактирует товар, то выдаем ошибку и делаем переход на главное окно центрального рынка.
    if data_market[1] == 'in production':
        await message.answer('❌ Продавец лавки редактирует товар')
        await Show(message, bot, api)
        return

    # Создаем массив с данными о магазине, статус магазина и VK_ID продавца.
    # info_market = [номер магазина, статус лавки, VK_ID продавца]
    info_market = [data_market[0], data_market[1], data_market[3], data_market[5]]
    await database.setMultiUserData(message.from_id, f'temporary_var = "{info_market}"')

    # --------------------------------------------------------

    # Создаем список товаров.
    spisok = ''

    # Если игрок скупает предметы, то ставим статус магазина "Игрок скупает предметы".
    if info_market[1] == 'скупка': STATUS_DROVEC = 'Игрок скупает предметы'

    # Если игрок продает предметы, то ставим статус магазина "Игрок продает предметы".
    if info_market[1] == 'продажа': STATUS_DROVEC = 'Игрок продает предметы'

    # Создаем клавиатуру.
    KEYBOARD = Keyboard(one_time=True, inline=False)
    KEYBOARD.add(Text("◀ Назад", {"cmd": "CentralMarket.Show"}), color=KeyboardButtonColor.PRIMARY)
    for item in data_market_items:
        if item[0] == 0:
            ITEM_NAME = '🧿 Фишки казино'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🧿 Купить фишки казино'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🧿 Продать фишки казино'
        if item[0] == 1:
            ITEM_NAME = 'дерево (🌲)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🌲 Купить дерево'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🌲 Продать дерево'
        if item[0] == 2:
            ITEM_NAME = 'металл (📦)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '📦 Купить металл'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '📦 Продать металл'
        if item[0] == 3:
            ITEM_NAME = 'подарок (🎁)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🎁 Купить подарок'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🎁 Продать подарок'
        if item[0] == 4:
            ITEM_NAME = 'бронзовая рулетка (🥉)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🥉 Купить бронзовую рулетку'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🥉 Продать бронзовую рулетку'
        if item[0] == 5:
            ITEM_NAME = 'серебряная рулетка (🥈)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🥈 Купить серебряную рулетку'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🥈 Продать серебряную рулетку'
        if item[0] == 6:
            ITEM_NAME = 'золотая рулетка (🥇)'
            if STATUS_DROVEC == 'Игрок продает предметы': ITEM_NAME_BUTTON = '🥇 Купить золотую рулетку'
            if STATUS_DROVEC == 'Игрок скупает предметы': ITEM_NAME_BUTTON = '🥇 Продать золотую рулетку'
        spisok = f'{spisok}1 {ITEM_NAME} — {await database.pretty(item[1])} долларов (💵) — {await database.pretty(item[2])} доступно шт.\n'
        KEYBOARD.add(Text(f"{ITEM_NAME_BUTTON}", {"cmd": "CentralMarket.Buy"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.get_json()

    # --------------------------------------------------------
    if len(data_market_items) == 0:
        spisok = '❌ В данный момент нет товаров'
    else:
        spisok = f'Название товара — цена — количество\n{spisok}'
    # Отправляем сообщение.
    await message.answer(
        message=f'🎯 » 🗺 » 🏛 » 🏰 » Лавка №{number_market}\n\n'
                f'{STATUS_DROVEC}\n\n'
                f'{spisok}',
        keyboard=KEYBOARD
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Buy(message: Message, bot: Bot, api: API):

    # Устанавливаем стейт для игрока.
    await database.setUserData(message.from_id, 'state', "'CentralMarket.BuyCheck'")

    # data_user — сырые значения данные об игроке, который является покупателем.
    data_user = await database.getUserData(message.from_id)

    # Вытягиваем данные из temporary_var, которые вносились ранее.
    data_user_temporary = ast.literal_eval(data_user[44])
    data_user_temporary = list(data_user_temporary)

    # Проверяем, какой предмет выбрал человек.
    if message.text.endswith('фишки казино'): buy_item_id = 0
    if message.text.endswith('дерево'): buy_item_id = 1
    if message.text.endswith('металл'): buy_item_id = 2
    if message.text.endswith('подарок'): buy_item_id = 3
    if message.text.endswith('бронзовую рулетку'): buy_item_id = 4
    if message.text.endswith('серебряную рулетку'): buy_item_id = 5
    if message.text.endswith('золотую рулетку'): buy_item_id =6

    # Добавляем в конец массива ID предмета, который хочет купить игрок.
    data_user_temporary.append(buy_item_id)

    # Обновляем переменную temporary_var.
    await database.setMultiUserData(message.from_id, f'temporary_var = "{data_user_temporary}"')

    # Выводим сообщение для пользователя.
    await message.answer(
        message=f"✏ Напишите количество товара",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🏰 Уйти из лавки", {"cmd": "CentralMarket.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def BuyCheck(message: Message, bot: Bot, api: API):

    # Устанавливаем игроку статус "Заблокирован", т.е. он не сможет взаимодействовать с ботом.
    await database.setUserData(message.from_id, 'state', "'block.Show'")

    # data_user — сырые значения данные об игроке, который является покупателем.
    data_user = await database.getUserData(message.from_id)

    # Инвентарь игрока
    data_user = await database.getUserData(message.from_id)
    data_user_inventory = ast.literal_eval(data_user[48])
    data_user_inventory = list(data_user_inventory)

    # Вытягиваем данные из temporary_var, которые вносились ранее.
    data_user_temporary = ast.literal_eval(data_user[44])
    data_user_temporary = list(data_user_temporary)

    # Получаем данные лавки
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user_temporary[0]}'")

    # Получаем данные о продавце
    data_prodavec = await database.getUserData(data_market[3])

    # Инвентарь продавца
    data_prodavec = await database.getUserData(data_market[3])
    data_prodavec_inventory = ast.literal_eval(data_prodavec[48])
    data_prodavec_inventory = list(data_prodavec_inventory)

    # Получаем данные о предметах
    data_market_items = ast.literal_eval(data_market[2])
    data_market_items = list(data_market_items)

    # Получаем данные об истории продаж
    data_market_history = ast.literal_eval(data_market[4])
    data_market_history = list(data_market_history)

    # Проверяем хэш магазина
    if data_user_temporary[3] != data_market[5]:
        await message.answer('❌ Список товаров в лавке устарел, повторите попытку')
        await Show(message, bot, api)
        return

    # Проверяем, является ли числом текст
    if message.text.isdigit():

        # count — количество товара для покупки/продажи
        count = int(message.text)
        if count < 0:
            await message.answer('❌ Введите количество товара больше 0')
            await Show(message, bot, api)
            return
        else:
            if data_market[1] == 'продажа':
                id_in_market = -1
                for row in data_market_items:
                    id_in_market = id_in_market + 1
                    if row[0] == data_user_temporary[4]:
                        item_info = row
                if data_prodavec_inventory[data_user_temporary[4]] >= count:
                    if data_user[12] >= int(item_info[1] * count):
                        data_user_inventory[data_user_temporary[4]] = data_user_inventory[data_user_temporary[4]] + count
                        data_prodavec_inventory[data_user_temporary[4]] = data_prodavec_inventory[data_user_temporary[4]] - count
                        new_balance_user = data_user[12] - int(count * item_info[1])
                        new_balance_prodavec = data_prodavec[12] + int(count * item_info[1])

                        new_store = item_info[2] - count
                        data_market_items[id_in_market][2] = new_store

                        data_market_history.append(f'Вы продали предмет (ID: {item_info[0]}) в кол-ве {count} и заработали {item_info[1] * count}')

                        await database.setMultiUserData(message.from_id, f'inventory = "{data_user_inventory}", dollars = "{new_balance_user}"')
                        await database.setMultiUserData(data_market[3], f'inventory = "{data_prodavec_inventory}", dollars = "{new_balance_prodavec}"')
                        await database.setMultiDbData('centralmarket', 'id', data_user_temporary[0], f'items = "{data_market_items}", history = "{data_market_history}"')
                        await message.answer(f'✅ Вы успешно купили {count} предмет(ов)')
                        await Show(message, bot, api)
                        return
                    else:
                        await message.answer('❌ У вас нехватает долларов для покупки')
                        await Show(message, bot, api)
                        return
                else:
                    await message.answer('❌ Продавец продает меньше товаров или у продавца закончились товары')
                    await Show(message, bot, api)
                    return
            elif data_market[1] == 'скупка':

                id_in_market = -1
                for row in data_market_items:
                    id_in_market = id_in_market + 1
                    if row[0] == data_user_temporary[4]:
                        item_info = row
                if data_user_inventory[data_user_temporary[4]] >= count:
                    if data_prodavec[12] >= int(item_info[1] * count):
                        data_user_inventory[data_user_temporary[4]] = data_user_inventory[data_user_temporary[4]] - count
                        data_prodavec_inventory[data_user_temporary[4]] = data_prodavec_inventory[data_user_temporary[4]] + count
                        new_balance_user = data_user[12] + int(count * item_info[1])
                        new_balance_prodavec = data_prodavec[12] - int(count * item_info[1])

                        new_store = item_info[2] - count
                        data_market_items[id_in_market][2] = new_store

                        data_market_history.append(f'Вы купили предмет (ID: {item_info[0]}) в кол-ве {count} и потратили {item_info[1] * count}')

                        await database.setMultiUserData(message.from_id, f'inventory = "{data_user_inventory}", dollars = "{new_balance_user}"')
                        await database.setMultiUserData(data_market[3], f'inventory = "{data_prodavec_inventory}", dollars = "{new_balance_prodavec}"')
                        await database.setMultiDbData('centralmarket', 'id', data_user_temporary[0], f'items = "{data_market_items}", history = "{data_market_history}"')
                        await message.answer(f'✅ Вы успешно продали {count} предмет(ов) и получили {item_info[1] * count} долларов')
                        await Show(message, bot, api)
                        return
                    else:
                        await message.answer('❌ У продавца нехватает денег на покупку всех ваших предметов')
                        await Show(message, bot, api)
                        return
                else:
                    await message.answer('❌ Продавец покупает меньше товаров или у продавца закончились товары')
                    await Show(message, bot, api)
                    return


            else:
                await message.answer('❌ Продавец редактирует товар, попробуйте попытку')
                await Show(message, bot, api)
                return
    else:
        await message.answer('❌ Введите число')
        await Show(message, bot, api)
        return

# ----------------------------------------------------------------------------------------------------------------------

async def Arenda(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Arenda'")

    # Показываем интерфейс центрального рынка.
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Arenda'")

    # Получаем данные с центрального рынка.
    data_markerts = await database.yourSQL('SELECT * FROM `centralmarket` WHERE 1')

    # Создаем клавиатуру для лавок.
    KEYBOARD = Keyboard(one_time=True, inline=False)
    KEYBOARD.add(Text("❌ Отменить", {"cmd": "CentralMarket.Show"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.row()

    # Далее проиходит проверка лавок (если лавка занята, то будет белая кнопка, иначе красная).
    if data_markerts[0][1] == 'free':
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[1][1] == 'free':
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[2][1] == 'free':
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[3][1] == 'free':
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if data_markerts[4][1] == 'free':
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[5][1] == 'free':
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[6][1] == 'free':
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[7][1] == 'free':
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if data_markerts[8][1] == 'free':
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[9][1] == 'free':
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[10][1] == 'free':
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)

    if data_markerts[11][1] == 'free':
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.POSITIVE)
    else:
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.ArendaCheck"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.get_json()

    # Отпраляем человеку сообщение с составленной клавиатурой.
    await message.answer('🎯 » 🗺 » 🏛 » 🏰 » ➕ Арендовать лавку\n\n'
                         '💵 Цена аренды лавки » 2 000 долларов (💵)\n'
                         '⤵ Выберите доступную лавку (все свободные лавки показываются зеленым цветом)\n\n',
                        keyboard=KEYBOARD)
# ----------------------------------------------------------------------------------------------------------------------

async def ArendaCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    number_market = int(message.text[3:])
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{number_market}'")
    if data_market[3] != 0:
        await message.answer('❌ Лавка занята, попробуйте выбрать другую')
        await Arenda(message, bot, api)
        return
    else:
        if data_user[12] >= 2000:
            await database.setBdData('centralmarket', 'id', f"'{number_market}'", 'vk_id', f"'{message.from_id}'")
            await database.setBdData('centralmarket', 'id', f"'{number_market}'", 'hash', f"'{int(random.randint(0, 99999999999))}'")
            await database.setBdData('centralmarket', 'id', f"'{number_market}'", 'status', f"'in production'")
            await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'history', f"'[]'")
            await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'items', f"'[]'")
            await database.setUserData(message.from_id, 'temporary_var', f"'{number_market}'")
            new_balance = data_user[12] - 2000
            await database.setUserData(message.from_id, 'dollars', f"'{new_balance}'")
            await message.answer('✅ Вы успешно арендовали лавку')
            await ArendaTypeSelect(message, bot, api)
            return
        else:
            await message.answer('❌ У вас недостоаточно долларов')
            await Arenda(message, bot, api)
            return

# ----------------------------------------------------------------------------------------------------------------------

async def ArendaTypeSelect(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaTypeSelect'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 Выбор лавки\n\n"
                f"⤵ Выберите, вы будете продавать товары или скупать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💸 Продажа товаров", {"cmd": "CentralMarket.ArendaTypeSelectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🛍 Покупка товаров", {"cmd": "CentralMarket.ArendaTypeSelectCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def ArendaTypeSelectCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)

    if message.text == '💸 Продажа товаров':
        await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'status', f"'продажа'")
    if message.text == '🛍 Покупка товаров':
        await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'status', f"'скупка'")
    await ArendaMenu(message, bot, api)


# ----------------------------------------------------------------------------------------------------------------------

async def ArendaMenu(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenu'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")
    data_market_items = ast.literal_eval(data_market[2])
    data_market_items = list(data_market_items)
    if data_market[1] == 'скупка': STATUS_DROVEC = 'Игрок скупает предметы'
    if data_market[1] == 'продажа': STATUS_DROVEC = 'Игрок продает предметы'
    spisok = ''
    for item in data_market_items:
        if item[0] == 0:
            ITEM_NAME = '🧿 Фишки казино'
        if item[0] == 1:
            ITEM_NAME = 'дерево (🌲)'
        if item[0] == 2:
            ITEM_NAME = 'металл (📦)'
        if item[0] == 3:
            ITEM_NAME = 'подарок (🎁)'
        if item[0] == 4:
            ITEM_NAME = 'бронзовая рулетка (🥉)'
        if item[0] == 5:
            ITEM_NAME = 'серебряная рулетка (🥈)'
        if item[0] == 6:
            ITEM_NAME = 'золотая рулетка (🥇)'
        spisok = f'{spisok}1 {ITEM_NAME} — {await database.pretty(item[1])} долларов (💵) — {await database.pretty(item[2])} доступно шт.\n'
    if len(data_market_items) == 0:
        spisok = 'Нету товаров'
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 Управление лавкой ({data_market[1]})\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закончить аренду", {"cmd": "CentralMarket.ArendaEnd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("➕ Добавить новый товар", {"cmd": "CentralMarket.ArendaMenuAdd"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Редактировать товары", {"cmd": "CentralMarket.ArendaMenuEdit"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🛑 Удалить товары", {"cmd": "CentralMarket.ArendaMenuDel"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def ArendaMenuAdd(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenuAdd'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 » ➕ Добавить новый товар",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralMarket.ArendaMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🧿 Фишки казино", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🌲 Дерево", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📦 Металл", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🎁 Подарок", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥉 Бронзовая рулетка", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🥈 Серебряная рулетка", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥇 Золотая рулетка", {"cmd": "CentralMarket.ArendaMenuAdd_Add"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ArendaMenuAdd_Add(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenuAdd_Add1'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    data_market_items = ast.literal_eval(data_market[2])
    data_market_items = list(data_market_items)

    if message.text == '🧿 Фишки казино':
        id_item = 0
    if message.text == '🌲 Дерево':
        id_item = 1
    if message.text == '📦 Металл':
        id_item = 2
    if message.text == '🎁 Подарок':
        id_item = 3
    if message.text == '🥉 Бронзовая рулетка':
        id_item = 4
    if message.text == '🥈 Серебряная рулетка':
        id_item = 5
    if message.text == '🥇 Золотая рулетка':
        id_item = 6

    count = 0
    for row in data_market_items:
        if row[0] == id_item:
            count = count + 1
    if count != 0:
        await message.answer('⚠ Данный предмет уже есть в лавке')
        await ArendaMenuAdd(message, bot, api)
        return
    massive = [id_item]
    await database.setMultiUserData(message.from_id, f'temporary_var2 = "{massive}"')
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 » ➕ Добавить новый товар (цена)\n\n"
                f"📝 Введите цену",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralMarket.ArendaMenuAdd"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ArendaMenuAdd_Add1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenuAdd_Add2'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    data_user_temporary = ast.literal_eval(data_user[54])
    data_user_temporary = list(data_user_temporary)

    if message.text.isdigit():
        if int(message.text) <= 0:
            await message.answer('⚠ Ошибка. Вы ввели число меньше 0')
            await ArendaMenu(message, bot, api)
            return
        data_user_temporary.append(int(message.text))
        await database.setMultiUserData(message.from_id, f'temporary_var2 = "{data_user_temporary}"')
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 » ➕ Добавить новый товар (количество товаров)\n\n"
                    f"📝 Введите количество",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "CentralMarket.ArendaMenuAdd"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer('⚠ Ошибка. Вы ввели текст')
        await ArendaMenu(message, bot, api)
        return

async def ArendaMenuAdd_Add2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenuAdd_Add3'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    data_user_temporary = ast.literal_eval(data_user[54])
    data_user_temporary = list(data_user_temporary)

    if message.text.isdigit():
        if int(message.text) <= 0:
            await message.answer('⚠ Ошибка. Вы ввели число меньше 0')
            await ArendaMenu(message, bot, api)
            return
        data_user_temporary.append(int(message.text))
        await database.setMultiUserData(message.from_id, f'temporary_var2 = "{data_user_temporary}"')

        if data_user_temporary[0] == 0:
            ITEM_NAME = '🧿 Фишки казино'
        if data_user_temporary[0] == 1:
            ITEM_NAME = 'дерево (🌲)'
        if data_user_temporary[0] == 2:
            ITEM_NAME = 'металл (📦)'
        if data_user_temporary[0] == 3:
            ITEM_NAME = 'подарок (🎁)'
        if data_user_temporary[0] == 4:
            ITEM_NAME = 'бронзовая рулетка (🥉)'
        if data_user_temporary[0] == 5:
            ITEM_NAME = 'серебряная рулетка (🥈)'
        if data_user_temporary[0] == 6:
            ITEM_NAME = 'золотая рулетка (🥇)'

        text = 'none'
        if data_market[1] == 'продажа':
            text = f'Вы будете продавать {ITEM_NAME} за {await database.pretty(data_user_temporary[1])} долларов (💵) в количестве {await database.pretty(data_user_temporary[2])} штук.'
        if data_market[1] == 'скупка':
            text = f'Вы будете покупать {ITEM_NAME} за {await database.pretty(data_user_temporary[1])} долларов (💵) в количестве {await database.pretty(data_user_temporary[2])} штук.'
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏰 » 🏰 » ➕ Добавить новый товар (подтверждение)\n\n"
                    f"{text}\n\n"
                    f"⤵ Нажмите на кнопку ниже, если вы подтверждаете добавление данного предмета в лавку",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "CentralMarket.ArendaMenuAdd"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("Подтверждаю", {"cmd": "CentralMarket.ArendaMenuAdd_Add3"}), color=KeyboardButtonColor.POSITIVE)
                    .add(Text("❌ Отмена", {"cmd": "CentralMarket.ArendaMenu"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer('⚠ Ошибка. Вы ввели текст')
        await ArendaMenu(message, bot, api)
        return


async def ArendaMenuAdd_Add3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    data_market_items = ast.literal_eval(data_market[2])
    data_market_items = list(data_market_items)

    data_user_temporary = ast.literal_eval(data_user[54])
    data_user_temporary = list(data_user_temporary)

    data_market_items.append([data_user_temporary[0], data_user_temporary[1], data_user_temporary[2]])
    await database.setMultiDbData('centralmarket', 'id', data_user[44], f'items = "{data_market_items}"')
    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'hash', f"'{int(random.randint(0, 99999999999))}'")

    await message.answer('✅ Вы успешно добавили товар')
    await ArendaMenu(message, bot, api)
    return
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------

async def ArendaEnd(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.ArendaMenu'")
    data_user = await database.getUserData(message.from_id)
    data_market = await database.getBdData('centralmarket', 'id', f"'{data_user[44]}'")

    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'vk_id', f"'0'")
    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'hash', f"''")
    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'status', f"'free'")
    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'history', f"'[]'")
    await database.setBdData('centralmarket', 'id', f"'{data_user[44]}'", 'items', f"'[]'")

    await message.answer('⚠ Вы закончили арендовывать лавку')
    await Show(message, bot, api)
    return