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
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Доброго времени суток, добро пожаловать в центр лицензирования. Чем я могу вам помочь?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📒 Получение прав", {"cmd": "LicensingCenter.GetLicences"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 Узнать стоимость", {"cmd": "LicensingCenter.PricesLicences"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def PricesLicences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.PricesLicences'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Мы являемся единственным местом лицензирования всех жителей штата. Здесь вы можете получить большинство лицензий. "
                f"Вот наш прайс-лист:\n\n"
                f"🚗 Лицензия на автомобили » 1 500 долларов (💵)\n"
                f"🏍 Лицензия на мотоциклы » 250 долларов (💵)\n"
                f"🚚 Лицензия на грузовой транспорт » 5 000 долларов (💵)\n"
                f"🔫 Лицензия на оружие » преобретается в полиции\n"
                f"🐠 Лицензия на ловлю рыбы » 500 долларов (💵)\n"
                f"🛩 Лицензия на воздушный транспорт » 50 000 (💵)\n"
                f"🛥 Лицензия на водный транспорт » 15 000 (💵)\n"
                f"🐅 Лицензия на охоту » преобретается в полиции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return
