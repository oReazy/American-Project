import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re, ast
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message: Message):
    database.setUserData(message.from_id, 'state', "'donate.Show'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 Донат\n\n"
                f'На данной странице вы можете узнать номер своего аккаунта, а также узнать текущее состояние '
                f'вашего доната. Чтобы воспользоваться донатом, нажмите на кнопку «Заказать». Если вам необходимо '
                f'пополнить счет, то нажмите на кнопку «Пополнить счет»\n\n'
                f'🆔 Номер вашего аккаунта » {data[0]}\n'
                f'💎 Текущее состояние счета » {data[21]}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🛍 Заказать", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("➕ Пополнить счет", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def ShopMenu1(message: Message):
    database.setUserData(message.from_id, 'state', "'donate.ShopMenu1'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {data[21]}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("👑 VIP", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("💵 Получить доллары", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📱 Эксклюзивный телефон", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("👕 Эксклюзивная одежда", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📝 Сменить ник", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🌐 Купить очки опыта", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📄 Получить все лицензии", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )
    return



async def ShopMenu2(message: Message):
    database.setUserData(message.from_id, 'state', "'donate.ShopMenu2'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {data[21]}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Навык фермера", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🚚 Навык дальнобойщика", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🚕 Навык таксиста", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📦 Коробки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🅰️ Снять варн", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )
    return