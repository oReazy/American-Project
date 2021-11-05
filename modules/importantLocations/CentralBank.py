import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Центр лицензирования

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    if data[69] == '❌ Отсутствует':
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏦 Центральный банк\n\n"
                    f"👱‍♀ Доброго времени суток, меня зовуту Мария и являюсь сотрудницей Центрального Банка штата {server_settings[9]}. Чем я могу вам помочь?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💳 Получение банковской карты", {"cmd": "CentralBank.CreateBankCard1"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏦 Центральный банк\n\n"
                    f"👱‍♀ Доброго времени суток, меня зовуту Мария и являюсь сотрудницей Центрального Банка штата {server_settings[9]}. Чем я могу вам помочь?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💳 Провести операцию с картой", {"cmd": "CentralBank.BankomatWelcome"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return


# -------------------------------------------------------------------------------------------------------------


async def BankomatWelcome(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"💳 Вы вставляете в банкомат карту"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"👈 Вы прикладываете палец для индификации"
    )
    await asyncio.sleep(5)
    await Bankomat(message, bot, api)
    return


async def Bankomat(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.Bankomat'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Банковские операции над картой\n\n"
                f"👤 Здраствуйте, {data[3]}.\n\n"
                f"💳 Выберите опцию, которой хотите воспользоваться",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💳 Выйти", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("ℹ Баланс денег", {"cmd": "CentralBank.Balance"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔼 Пополнить", {"cmd": "CentralBank.addBalance1"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🔽 Списать", {"cmd": "CentralBank.vivodBalance1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💸 Перевод денег", {"cmd": "CentralBank.none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💱 Обменник валют", {"cmd": "CentralBank.none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def Balance(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    num1 = await database.pretty(data[16])
    num2 = await database.pretty(data[17])
    num3 = await database.pretty(data[18])
    num4 = await database.pretty(data[19])
    await message.answer(
        message=f"💵 Доллары в банке » {num1}\n"
                f"💶 Евро в банке » {num2}\n"
                f"💴 Иены в банке » {num3}\n"
                f"💷 Фунты в банке » {num4}",
    )
    await Bankomat(message, bot, api)
    return



async def vivodBalance1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalance1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 Списать\n\n"
                f"Выберите валюту для списания",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.vivodBalanceDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.vivodBalanceEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.vivodBalanceYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.vivodBalancePounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def vivodBalancePounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalancePoundsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💷 Фунты\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def vivodBalancePoundsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[15] <= data[19]:
                new_balance = int(data[15]) + count
                new_balance2 = int(data[19]) - count
                await database.setMultiUserData(message.from_id, f"pounds = '{new_balance}', bank_pounds = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли фунты со своего счета"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalancePounds(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalancePounds(message, bot, api)
        return





async def vivodBalanceYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalanceYenCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💴 Иены\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def vivodBalanceYenCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[14] <= data[18]:
                new_balance = int(data[14]) + count
                new_balance2 = int(data[18]) - count
                await database.setMultiUserData(message.from_id, f"yen = '{new_balance}', bank_yen = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли иены со своего счета"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceYen(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceYen(message, bot, api)
        return





async def vivodBalanceEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceEuroCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💶 Евро\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def vivodBalanceEuroCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[13] <= data[17]:
                new_balance = int(data[13]) + count
                new_balance2 = int(data[17]) - count
                await database.setMultiUserData(message.from_id, f"euro = '{new_balance}', bank_euro = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли евро со своего счета"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceEuro(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceEuro(message, bot, api)
        return



async def vivodBalanceDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalanceDollarsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💵 Доллары\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def vivodBalanceDollarsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[12] <= data[16]:
                new_balance = int(data[12]) + count
                new_balance2 = int(data[16]) - count
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', bank_dollars = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли доллары со своего счета"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceDollars(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceDollars(message, bot, api)
        return
















async def addBalance1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalance1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 Пополнить\n\n"
                f"Выберите валюту для пополнения",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.addBalanceDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.addBalanceEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.addBalanceYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.addBalancePounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def addBalancePounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalancePoundsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💷 Фунты\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def addBalancePoundsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[15] >= data[19]:
                new_balance = int(data[15]) - count
                new_balance2 = int(data[19]) + count
                await database.setMultiUserData(message.from_id, f"pounds = '{new_balance}', bank_pounds = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили фунтовый счет"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalancePounds(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalancePounds(message, bot, api)
        return





async def addBalanceYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceYenCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💴 Иены\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def addBalanceYenCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[14] >= data[18]:
                new_balance = int(data[14]) - count
                new_balance2 = int(data[18]) + count
                await database.setMultiUserData(message.from_id, f"yen = '{new_balance}', bank_yen = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили иеновский счет"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceYen(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceYen(message, bot, api)
        return





async def addBalanceEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceEuroCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💶 Евро\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def addBalanceEuroCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[13] >= data[17]:
                new_balance = int(data[13]) - count
                new_balance2 = int(data[17]) + count
                await database.setMultiUserData(message.from_id, f"euro = '{new_balance}', bank_euro = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили евро счет"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceEuro(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceEuro(message, bot, api)
        return



async def addBalanceDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceDollarsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💵 Доллары\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def addBalanceDollarsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[12] >= data[16]:
                new_balance = int(data[12]) - count
                new_balance2 = int(data[16]) + count
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', bank_dollars = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили долларовый счет"
                    )
                await Bankomat(message, bot, api)
                return
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
                return
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceDollars(message, bot, api)
            return
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceDollars(message, bot, api)
        return




# --------------------------------------------------------------------------------------------------------------


async def CreateBankCard1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Для того, чтобы оформить банковскую карту, вам необходимо 250 долларов (💵). Они у вас есть?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Нету", {"cmd": "CentralBank.CreateBankCardError"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Заплатить за оформление карты", {"cmd": "CentralBank.CreateBankCard2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCardError(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCardError'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Как только у вас будет 250 долларов (💵), то я вам смогу сделать банковскую карту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def CreateBankCard2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard2'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    if data[12] >= 250:
        await message.answer(
            message="👱‍♀ Отлично."
        )
        new_balance = int(data[12]) - 250
        await database.setUserData(message.from_id, "dollars", f"'{new_balance}'")
        await CreateBankCard3(message, bot, api)
        return
    else:
        await message.answer(
            message=f"❌ У вас нет 250 долларов на руках",
        )
        await CreateBankCard1(message, bot, api)
        return


async def CreateBankCard3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard3'")
    await message.answer(
        message="👱‍♀ Проследуйте за мной, необходима ваша фотография",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻‍♂ Идти за девушкой", {"cmd": "CentralBank.CreateBankCard4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶🏻‍♂ Вы идете за девушкой в специальную комнату"
    )
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard4'")
    await message.answer(
        message=f"🚶🏻‍♂ Вы пришли в специальную комнату и видите в ней фото-камеру и световые прожекторы"
    )
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Присаживайтесь за стул, сейчас я вас сфотографирую.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🪑 Сесть за стул", {"cmd": "CentralBank.CreateBankCard5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🪑 Вы сели за стул"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📸 *Произошел щелчек в камере*"
    )
    await asyncio.sleep(4)
    await message.answer(
        message=f"👱‍♀ Вы отлично получились на данной фотографии"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"👱‍♀ Сейчас подкреплю вашу фотографирую к карте и сейчас я ее вам выдам..."
    )
    await asyncio.sleep(15)
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard5'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Отлично, на этом все. Теперь это ваша карта. Спасибо, что выбрали именно наш банк.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Callback("💳 Взять карту", payload={"cmd": "CentralBank.CreateBankCard6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard6(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'CentralBank.Show'")
    await database.setUserData(from_id, 'bank_card', "'✅ Имеется'")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"💳 Вы взяли карту.\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Пользоваться услугами банка: пополнять, снимать деньги со счета\n"
                f"— Переводить деньги с карты на карту\n"
                f"— Получать уникальные скидки и кэшбек.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )