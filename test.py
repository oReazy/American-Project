import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Центральный рынок

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Show'")
    server_settings = await database.getBdData('settings', 'id', "'1'")

    server_settings = ast.literal_eval(server_settings[29])
    server_settings = list(server_settings)
    KEYBOARD = Keyboard(one_time=True, inline=False)
    KEYBOARD.add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD.add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.row()
    if server_settings[0][0] == 'free':
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №1", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[1][0] == 'free':
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №2", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[2][0] == 'free':
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №3", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[3][0] == 'free':
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №4", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if server_settings[4][0] == 'free':
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №5", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[5][0] == 'free':
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №6", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[6][0] == 'free':
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №7", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[7][0] == 'free':
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №8", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()

    if server_settings[8][0] == 'free':
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №9", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[9][0] == 'free':
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №10", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[10][0] == 'free':
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №11", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    if server_settings[11][0] == 'free':
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.NEGATIVE)
    else:
        KEYBOARD.add(Text("🏰 №12", {"cmd": "CentralMarket.Lavka"}), color=KeyboardButtonColor.SECONDARY)

    KEYBOARD.row()
    KEYBOARD.add(Text("➕ Арендовать лавку", {"cmd": "CentralMarket.Arenda"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.get_json()

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏰 Центральный рынок (β)\n\n"
                f"β — в данный момент центральный рынок находится в бета-режиме. Возможно баги, ошибки.",
        keyboard=KEYBOARD
    )



# [['work', 'скупка', [[0, 200, 1000]], 340311937],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free']]
# [['work', 'скупка', [[3, 10000, 1000]], 340311937, ''],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free']]



# [['work', 'скупка', [[3, 10000, 1000], [4, 30000, 10], [5, 150000, 10], [6, 700000, 10]], 340311937, ''],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free'],['free']]




async def Lavka(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.Show'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    server_settings = ast.literal_eval(server_settings[29])
    server_settings = list(server_settings)
    number_store = int(message.text[3:]) - 1
    info_store = [number_store, server_settings[number_store][1], server_settings[number_store][3]]
    await database.setMultiUserData(message.from_id, f'temporary_var = "{info_store}"')
    if server_settings[number_store][0] == 'free':
        await message.answer('❌ В данной лавке никто не продает')
        await Show(message, bot, api)
        return
    if server_settings[number_store][0] == 'in redaction':
        await message.answer('❌ Продавец лавки редактирует товар')
        await Show(message, bot, api)
        return
    else:
        spisok = ''
        if server_settings[number_store][1] == 'скупка': STATUS_DROVEC = 'Игрок скупает предметы'
        if server_settings[number_store][1] == 'продажа': STATUS_DROVEC = 'Игрок продает предметы'
        KEYBOARD = Keyboard(one_time=True, inline=False)
        KEYBOARD.add(Text("◀ Назад", {"cmd": "CentralMarket.Show"}), color=KeyboardButtonColor.PRIMARY)
        for item in server_settings[number_store][2]:
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
            KEYBOARD.row()
            KEYBOARD.add(Text(f"{ITEM_NAME_BUTTON}", {"cmd": "CentralMarket.Buy"}), color=KeyboardButtonColor.SECONDARY)


        KEYBOARD.get_json()
        await message.answer(
            message=f'🎯 » 🗺 » 🏛 » 🏰 » Лавка №{number_store + 1}\n\n'
                    f'{STATUS_DROVEC}\n\n'
                    f'Название товара — цена — количество\n'
                    f'{spisok}',
            keyboard=KEYBOARD
        )


async def Buy(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralMarket.BuyCheck'")
    data_user = await database.getUserData(message.from_id)
    data_user = ast.literal_eval(data_user[44])
    data_user = list(data_user)
    if message.text.endswith('фишки казино'): item_id = 0
    if message.text.endswith('дерево'): item_id = 1
    if message.text.endswith('металл'): item_id = 2
    if message.text.endswith('подарок'): item_id = 3
    if message.text.endswith('бронзовую рулетку'): item_id = 4
    if message.text.endswith('серебряную рулетку'): item_id = 5
    if message.text.endswith('золотую рулетку'): item_id =6
    data_user.append(item_id)
    await database.setMultiUserData(message.from_id, f'temporary_var = "{data_user}"')
    await message.answer(
        message=f"✏ Напишите количество товара",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🏰 Уйти из лавки", {"cmd": "CentralMarket.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def BuyCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_user = await database.getUserData(message.from_id)
    data_user = ast.literal_eval(data_user[44])
    data_user = list(data_user)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    server_settings = ast.literal_eval(server_settings[29])
    server_settings = list(server_settings)
    if message.text.isdigit():
        count = int(message.text)
        if count < 0:
            await message.answer('❌ Введите количество товара больше 0')
            await Show(message, bot, api)
            return
    else:
        await message.answer('❌ Введите число')
        await Show(message, bot, api)
        return
    count_item_final = -1
    if data_user[1] == server_settings[data_user[0]][1]:
        if data_user[2] == server_settings[data_user[0]][3]:
            for item in server_settings[data_user[0]][2]:
                count_item_final = count_item_final + 1
                print(item)
                if item[0] == data_user[3]:
                    if item[2] >= count:
                        if server_settings[data_user[0]][1] == 'скупка':
                            pocupatel_user = await database.getUserData(message.from_id)
                            inventory = pocupatel_user
                            inventory = ast.literal_eval(inventory[48])
                            inventory = list(inventory)
                            if inventory[data_user[3]] >= count:
                                print(data_user)
                                prodavec_profile = await database.getUserData(server_settings[data_user[0]][3])
                                inventory_prodavec = prodavec_profile
                                inventory_prodavec = ast.literal_eval(inventory_prodavec[48])
                                inventory_prodavec = list(inventory_prodavec)
                                inventory_prodavec[data_user[3]] = inventory_prodavec[data_user[3]] + count
                                inventory[data_user[3]] = inventory[data_user[3]] - count
                                print(item[1])
                                prodavec_profile_new = int(prodavec_profile[12]) - (count * int(item[1]))
                                pocupatel_user_new = int(pocupatel_user[12]) + (count * int(item[1]))
                                await database.setUserData(pocupatel_user[1], 'dollars', f"'{prodavec_profile_new}'")
                                await database.setUserData(pocupatel_user[1], 'inventory', f"'{inventory}'")
                                await database.setUserData(prodavec_profile[1], 'dollars', f"'{pocupatel_user_new}'")
                                await database.setUserData(prodavec_profile[1], 'inventory', f"'{inventory_prodavec}'")
                                print(server_settings[data_user[0]][4])
                                settings_history_update = list(server_settings[data_user[0]][4])
                                server_settings[data_user[0]][4] = (f'{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year} — вы купили предметы на {count * item[1]} (ID: {item[0]})/n{server_settings[data_user[0]][4]}')
                                item_new = item[2] - count
                                server_settings[data_user[0]][2][count_item_final][2] = item_new
                                print(server_settings)
                                await database.setMultiDbData('settings', 'id', "'1'", f'CentralMarket = \"{server_settings}\"')
                                await message.answer(f'✅ Вы успешно продали {count} предметов и получили {count * item[1]}')
                                await Show(message, bot, api)
                                return
                            else:
                                await message.answer('❌ У вас недостаточно предметов для продажи')
                                await Show(message, bot, api)
                                return
                        if server_settings[data_user[0]][1] == 'продажа':
                            pocupatel_user = await database.getUserData(message.from_id)
                            inventory = pocupatel_user
                            inventory = ast.literal_eval(inventory[48])
                            inventory = list(inventory)
                            if pocupatel_user[12] >= (count * item[1]):
                                prodavec_profile = await database.getUserData(server_settings[data_user[0]][3])
                                inventory_prodavec = prodavec_profile
                                inventory_prodavec = ast.literal_eval(inventory_prodavec[48])
                                inventory_prodavec = list(inventory_prodavec)
                                inventory_prodavec[data_user[3]] = inventory_prodavec[data_user[3]] - count
                                inventory[data_user[3]] = inventory[data_user[3]] + count
                                prodavec_profile_new = int(prodavec_profile[12]) + (count * int(item[1]))
                                pocupatel_user_new = int(pocupatel_user[12]) - (count * int(item[1]))
                                await database.setUserData(pocupatel_user[1], 'dollars', f"'{prodavec_profile_new}'")
                                await database.setUserData(pocupatel_user[1], 'inventory', f"'{inventory}'")
                                await database.setUserData(prodavec_profile[1], 'dollars', f"'{pocupatel_user_new}'")
                                await database.setUserData(prodavec_profile[1], 'inventory', f"'{inventory_prodavec}'")
                                print(server_settings[data_user[0]][4])
                                settings_history_update = list(server_settings[data_user[0]][4])
                                server_settings[data_user[0]][4] = (f'{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year} — вы продали предметы на {count * item[1]} (ID: {item[0]})/n{server_settings[data_user[0]][4]}')
                                item_new = item[2] - count
                                server_settings[data_user[0]][2][count_item_final][2] = item_new
                                print(server_settings)
                                await database.setMultiDbData('settings', 'id', "'1'", f'CentralMarket = \"{server_settings}\"')
                                await message.answer(f'✅ Вы успешно купили {count} предметов и потратили {count * item[1]}')
                                await Show(message, bot, api)
                                return
                            else:
                                await message.answer('❌ У вас недостаточно денег для покупки')
                                await Show(message, bot, api)
                                return
                    await message.answer('❌ Продавец лавки не покупает/продает такое количество предметов')
                    await Show(message, bot, api)
                    return
            await message.answer('❌ Данного товара в лавке больше нет')
            await Show(message, bot, api)
            return
        else:
            await message.answer('❌ В лавке поменялся продавец')
            await Show(message, bot, api)
    else:
        await message.answer('❌ Продавец больше не покупает/продает товары')
        await Show(message, bot, api)