import random, asyncio
import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, Bot, API
import json, time, os, sys, re, ast, datetime
from modules import database

# ------------------------------------------------------------------------------------------

# Инвентарь

# ID ПРЕДМЕТОВ
# ----------------------------------
# ID    | НАЗВАНИЕ
# ----------------------------------
# 1       ПОДАРОК
# 2       ЛАРЕЦ С ПРЕМИЕЙ
# 3       ЛАРЕЦ С АВТОМОБИЛЯМИ
# 4       ЛАРЕЦ С ОДЕЖДОЙ
# 5       БРОНЗОВАЯ РУЛЕТКА
# 6       СЕРЕБРЯНАЯ РУЛЕТКА
# 7       ЗОЛОТАЯ РУЛЕТКА
# 8       СЕЗОННЫЕ ПРЕДМЕТЫ: ЗАБРОНИРОВАНО
# 9       СЕЗОННЫЕ ПРЕДМЕТЫ: ЗАБРОНИРОВАНО
# 10      СЕЗОННЫЕ ПРЕДМЕТЫ: ЗАБРОНИРОВАНО
# 11      СЕЗОННЫЕ ПРЕДМЕТЫ: ЗАБРОНИРОВАНО
# 12      СЕЗОННЫЕ ПРЕДМЕТЫ: ЗАБРОНИРОВАНО
# 13      ФИШКИ КАЗИНО
#

# -------------------------------------------------------------------------------------------


async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'inventory.Show'")
    inventory = await database.getUserData(message.from_id)
    inventory = inventory[80]
    inventory = inventory.replace("]", "")
    inventory = inventory.replace("[", "")
    inventory = inventory.replace('"', "")
    inventory = inventory.replace("'", "")
    inventory = inventory.split(', ')

    # massive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(len(massive))
    #
    # inventory = str(inventory)
    # inventory = inventory.replace("'", "")
    # print(inventory)

    await database.setUserData(message.from_id, 'state', "'inventory.Show'")
    await message.answer(
        message=f"🎯 » 👤 » 💼 Инвентарь\n\n"
                f"❄ Снежинок » {inventory[8]} шт.\n\n"
                f"🎁 Подарки » {inventory[0]} шт.\n"
                f"🧰 Ларец с премией » {inventory[1]} шт.\n"
                f"🧰 Ларец с автомобилями » {inventory[2]} шт.\n"
                f"🧰 Ларец с одеждой » {inventory[3]} шт.\n"
                f"🥉 Бронзовая рулетка » {inventory[4]} шт.\n"
                f"🥈 Серебряная рулетка » {inventory[5]} шт.\n"
                f"🥇 Золотая рулетка » {inventory[6]} шт.\n"
                f"🧿 Фишки казино » {inventory[12]} шт.\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )