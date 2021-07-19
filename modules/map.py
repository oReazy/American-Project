import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re, ast
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message: Message):
    database.setUserData(message.from_id, 'state', "'report.Show'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 🗺 Карта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏛 Важные места", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🧱 Работы для новичков", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🛠 По работе", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🚙 Автосалоны", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏢 Отели", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🏷 Разное", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔩 Автомастерские", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🍐 Фермы", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Секонд-хенды", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🎭 Мероприятия", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Квестовые персонажи", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🛢 Нефтевышки", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return