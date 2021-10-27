import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Раздел с донатом

# -------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 Донат\n\n"
                f'На данной странице вы можете узнать номер своего аккаунта, а также узнать текущее состояние '
                f'вашего доната. Чтобы воспользоваться донатом, нажмите на кнопку «Заказать». Если вам необходимо '
                f'пополнить счет, то нажмите на кнопку «Пополнить счет»\n\n'
                f'🆔 Номер вашего аккаунта » {data[0]}\n'
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🛍 Заказать", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("➕ Пополнить счет", {"cmd": "donate.Show_ADD"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Show_ADD(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » ➕ Пополнить счет\n\n"
                f'Пополнить счет игрового аккаунта можно с помощью разных способов. Выберите самый удобный и подходящий для вас.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def ShopMenu1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ShopMenu1'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("👑 VIP", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("💵 Получить доллары", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Эксклюзивный телефон", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Эксклюзивная одежда", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📝 Сменить ник", {"cmd": "donate.ChangeNick"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Купить очки опыта", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📄 Получить все лицензии", {"cmd": "donate.Licences"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def ShopMenu2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ShopMenu2'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Навык фермера", {"cmd": "donate.SkillFarmer"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚚 Навык дальнобойщика", {"cmd": "donate.SkillTruck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚕 Навык таксиста", {"cmd": "donate.SkillTaxi"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📦 Коробки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🅰️ Снять варн", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )
    return


async def ChangeNick(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ChangeNick'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📝 Сменить ник\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'🛍 Цена » 30 💎\n\n'
                f'📄 Купив данную услугу, вы сможете поменять себе ник. Главной особенностью данной услуги является то, что вы сможете поставить ник длинной от 3 до 30 символов!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Поменять ник", {"cmd": "donate.ChangeNickGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return

async def ChangeNickGet(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if int(data[21]) >= 30:
        await database.setUserData(message.from_id, 'state', "'donate.ChangeNickGetCheck'")
        await message.answer(
            message=f'✏ Напишите новый желаемый ник от 3 до 30 символов',
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("Отменить", {"cmd": "donate.ChangeNick"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для смены ника',
        )
        await ChangeNick(message, bot, api)
        return


async def ChangeNickGetCheck(message: Message, bot: Bot, api: API):
    if 3 <= len(message.text) <= 30:
        if await database.findBaseData('nick', f"'{message.text}'") == 0:
            data = await database.getUserData(message.from_id)
            info = ast.literal_eval(data[56])
            info = list(info)
            info.append(f'{data[3]}')
            new_donate = int(data[21]) - 30
            await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", nick = "{message.text}", history_nicks = "{info}"')
            await message.answer(
                message='✅ Вы успешно поменяли себе ник'
            )
            await ChangeNick(message, bot, api)
        else:
            await message.answer(
                message='❌ Ошибка. Данный ник уже занят. Попробуйте другой'
            )
            await ChangeNickGet(message, bot, api)
    else:
        await message.answer(
            message=f'❌ Ошибка. Вы ввели либо короткий ник, либо слишком длинный.'
        )
        await ChangeNickGet(message, bot, api)






async def SkillTaxi(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillTaxi'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🚕 Навык таксиста\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'🛍 Цена » 100 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык таксиста. Это означает, что вы сможете получать больше денег за работу.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillTaxiBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def SkillTaxiBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 100:
        new_donate = int(data[21]) - 100
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', skill_taxi = '10000'")
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык дальнобойщика',
        )
        await SkillTaxi(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillTaxi(message, bot, api)




async def SkillTruck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillTruck'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🚚 Навык дальнобойщика\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'🛍 Цена » 250 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык дальнобойщика. Это означает, что вы сможете получать больше денег за работу.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillTruckBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def SkillTruckBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 250:
        new_donate = int(data[21]) - 250
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', skill_trucker = '5000'")
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык дальнобойщика',
        )
        await SkillTruck(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillTruck(message, bot, api)



async def SkillFarmer(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillFarmer'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🌽 Навык фермера\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'🛍 Цена » 150 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык фермера. Это означает, что вы сможете работать на любой должности фермы',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillFarmerBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def SkillFarmerBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 150:
        new_donate = int(data[21]) - 150
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', skill_farmer = '10000'")
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык фермера',
        )
        await SkillFarmer(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillFarmer(message, bot, api)



async def Licences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Licences'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📄 Получить все лицензии\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'🛍 Цена » 250 💎\n\n'
                f'📄 Купив данную услугу, вы получаете все виды лицензий.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.LicencesBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def LicencesBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 250:
        new_donate = int(data[21]) - 250
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', license_auto = '✅ Имеется', license_motorbike = '✅ Имеется', license_cargocar = '✅ Имеется', license_gun = '✅ Имеется', license_fish = '✅ Имеется', license_air = '✅ Имеется', license_water = '✅ Имеется', license_hunting = '✅ Имеется'")
        await message.answer(
            message=f'✅ Вы успешно купили все лицензии',
        )
        await Licences(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Licences(message, bot, api)



async def EXP(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXP'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🌐 Купить очки опыта\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'📊 Курс обмена » 1 очко опыта (🌐) = {await database.pretty(server_settings[3])} 💎\n\n'
                f'📄 Воспользовавшись данной услугой, вы можете получить неограниченное количество очков опыта. Очки опыта необходимы для повышения вас на новый уровень.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Получить очки опыта", {"cmd": "donate.EXPGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def EXPGet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXPGetCheck'")
    await message.answer(
        message=f'✏ Напишите, сколько доната вы готовы потратить',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отменить", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def EXPGetCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXPGetCheck'")
    if message.text.isdigit():
        money = int(message.text)
        if 1 <= money <= 999999999:
            data = await database.getUserData(message.from_id)
            server_settings = await database.getBdData('settings', 'id', "'1'")
            await database.setMultiUserData(message.from_id, f"temporary_var = '{message.text}'")
            if int(data[21]) >= int(int(message.text) * int(server_settings[3])):
                await message.answer(
                    message=f'⚠ Подтвердите действие\n\n'
                            f'Вы действительно хотите получить {await database.pretty(message.text)} очков опыта (🌐) за {await database.pretty(int(message.text) * int(server_settings[3]))} алмазов 💎',
                    keyboard=(
                        Keyboard(one_time=True, inline=False)
                            .add(Text("Подтверждаю", {"cmd": "donate.EXPGetCheckOK"}), color=KeyboardButtonColor.POSITIVE)
                            .row()
                            .add(Text("❌ Отказываюсь", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.SECONDARY)
                            .get_json()
                    )
                )
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько алмазов"
                )
                await EXPGet(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Введите число от 1 до 999 999 999"
            )
            await EXPGet(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Введите корректное число"
        )
        await EXPGet(message)
        return


async def EXPGetCheckOK(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    new_donate = int(data[21]) - int(int(data[75]) * int(server_settings[3]))
    new_exp = int(data[7]) + int(int(data[75]))
    await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', exp = '{new_exp}'")
    await message.answer(
        message=f'✅ Транзакция успешно проведена.',
    )
    await EXP(message, bot, api)
    return














async def Dollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Dollars'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 💵 Получить доллары\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'💵 Долларов на руках » {await database.pretty(data[12])}\n\n'
                f'📊 Курс обмена » 1 💎 = {await database.pretty(server_settings[2])} долларов (💵)\n\n'
                f'📄 Воспользовавшись данной услугой, вы можете получить неограниченное количество долларов в обмен на донат. С помощью долларов вы можете покупать внутриигровые предметы, а также взаимодействовать с другими игроками',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Получить доллары", {"cmd": "donate.DollarsGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def DollarsGet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.DollarsGetCheck'")
    await message.answer(
        message=f'✏ Напишите, сколько доната вы готовы потратить',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отменить", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def DollarsGetCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.DollarsGetCheck'")
    if message.text.isdigit():
        money = int(message.text)
        if 1 <= money <= 999999999:
            data = await database.getUserData(message.from_id)
            server_settings = await database.getBdData('settings', 'id', "'1'")
            await database.setMultiUserData(message.from_id, f"temporary_var = '{message.text}'")
            if int(data[21]) >= int(message.text):
                await message.answer(
                    message=f'⚠ Подтвердите действие\n\n'
                            f'Вы действительно хотите потратить {await database.pretty(message.text)} алмазов (💎) в обмен на {await database.pretty(int(message.text) * int(server_settings[2]))} игровых доллара (💵)',
                    keyboard=(
                        Keyboard(one_time=True, inline=False)
                            .add(Text("Подтверждаю", {"cmd": "donate.DollarsGetCheckOK"}), color=KeyboardButtonColor.POSITIVE)
                            .row()
                            .add(Text("❌ Отказываюсь", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.SECONDARY)
                            .get_json()
                    )
                )
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько алмазов"
                )
                await DollarsGet(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Введите число от 1 до 999 999 999"
            )
            await DollarsGet(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Введите корректное число"
        )
        await DollarsGet(message, bot, api)
        return


async def DollarsGetCheckOK(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    new_donate = int(data[21]) - int(data[75])
    new_dollars = int(data[12]) + int(int(data[75]) * int(server_settings[2]))
    await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', dollars = '{new_dollars}'")
    await message.answer(
        message=f'✅ Транзакция успешно проведена.',
    )
    await Dollars(message, bot, api)
    return



async def Telephone(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 Эксклюзивный телефон\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'📱 Ваш текущий телефон » {data[5]}\n\n'
                f'📱 iPhone 12 » 500 алмазов 💎\n'
                f'📱 iPhone 11 » 400 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy S21 » 350 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy A72 » 250 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy S20 » 200 алмазов 💎\n'
                f'📱 Xiaomi Mi 11 Lite » 150 алмазов 💎\n'
                f'📱 Xiaomi Redmi Note 10 Pro » 100 алмазов 💎\n'
                f'📱 Xiaomi Redmi Note 8 Pro » 50 алмазов 💎\n\n'
                f'📄 Воспользовавшись данной услугой, вы обмениваете донат на эксклюзивный телефон. Вы его сможете продать/обменять другому игроку, однако в игровом мире его нельзя получить за доллары, евро, иены или фунты.\n'
                f'Покупая эксклюзивные телефоны, вы получаете дополнительные приложения в телефон, которые доступны только на этих моделях',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📱 iPhone 12", {"cmd": "donate.Telephone_iPhone12"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 iPhone 11", {"cmd": "donate.Telephone_iPhone11"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy S21", {"cmd": "donate.Telephone_SamsungS21"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy A72", {"cmd": "donate.Telephone_SamsungA72"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy S20", {"cmd": "donate.Telephone_SamsungS20"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Mi 11 Lite", {"cmd": "donate.Telephone_Xiaomi11Lite"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Redmi Note 10 Pro", {"cmd": "donate.Telephone_Xiaomi10Pro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Redmi Note 8 Pro", {"cmd": "donate.Telephone_Xiaomi8Pro"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Telephone_Xiaomi8Pro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi8Pro'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Redmi Note 8 Pro\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Redmi Note 8 Pro за 50 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi8Pro_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_Xiaomi8Pro_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 50:
        new_donate = int(data[21]) - 50
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Redmi Note 8 Pro'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi8Pro(message, bot, api)



async def Telephone_Xiaomi10Pro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi10Pro'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Redmi Note 10 Pro\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Redmi Note 10 Pro за 100 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi10Pro_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_Xiaomi10Pro_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 100:
        new_donate = int(data[21]) - 100
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Redmi Note 10 Pro'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi10Pro(message, bot, api)





async def Telephone_Xiaomi11Lite(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi11Lite'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Mi 11 Lite\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Mi 11 Lite за 150 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi11Lite_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_Xiaomi11Lite_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 150:
        new_donate = int(data[21]) - 150
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Mi 11 Lite'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi11Lite(message, bot, api)



async def Telephone_SamsungS20(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungS20'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy S20\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy S20 за 200 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungS20_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_SamsungS20_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 200:
        new_donate = int(data[21]) - 200
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy S20'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungS20(message, bot, api)




async def Telephone_SamsungA72(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungA72'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy A72\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy A72 за 250 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungA72_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_SamsungA72_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 250:
        new_donate = int(data[21]) - 250
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy A72'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungA72(message, bot, api)



async def Telephone_SamsungS21(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungS21'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy S21\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy S21 за 350 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungS21_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_SamsungS21_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 350:
        new_donate = int(data[21]) - 350
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy S21'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungS21(message, bot, api)




async def Telephone_iPhone11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_iPhone11'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 iPhone 11\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить iPhone 11 за 400 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_iPhone11_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_iPhone11_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 400:
        new_donate = int(data[21]) - 400
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'iPhone 11'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_iPhone11(message, bot, api)


async def Telephone_iPhone12(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_iPhone12'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 iPhone 12\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[21])}\n'
                f'⚠ Вы действительно хотите купить iPhone 12 за 500 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_iPhone12_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )
    return


async def Telephone_iPhone12_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[21] >= 500:
        new_donate = int(data[21]) - 500
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'iPhone 12'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
        return
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_iPhone12(message, bot, api)