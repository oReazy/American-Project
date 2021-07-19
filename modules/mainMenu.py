import random

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message: Message):
    database.setUserData(message.from_id, 'state', "'mainMenu.Show'")
    data = database.getUserData(message.from_id)
    server_settings = database.getBdData('settings', 'id', "'1'")
    num1 = await database.pretty(data[12])
    num2 = await database.pretty(data[13])
    num3 = await database.pretty(data[14])
    num4 = await database.pretty(data[15])
    if data[11] == 0:
        await message.answer(
            message=f"🎯 Главное меню{server_settings[25]}\n\n"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Помощь по игре", {"cmd": "help_game.Show"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"🎯 Главное меню{server_settings[25]}\n\n"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Помощь по игре", {"cmd": "help_game.Show"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
        return


async def ShowFixFromId(from_id, bot: Bot):
    database.setUserData(from_id, 'state', "'mainMenu.Show'")
    data = database.getUserData(from_id)
    server_settings = database.getBdData('settings', 'id', "'1'")
    num1 = await database.pretty(data[12])
    num2 = await database.pretty(data[13])
    num3 = await database.pretty(data[14])
    num4 = await database.pretty(data[15])
    if data[11] == 0:
        await bot.api.messages.send(
            user_id=from_id,
            random_id=random.randint(1, 999999999),
            message=f"🎯 Главное меню{server_settings[25]}\n\n"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Помощь по игре", {"cmd": "help_game.Show"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
        return
    else:
        await bot.api.messages.send(
            user_id=from_id,
            random_id=random.randint(1, 999999999),
            message=f"🎯 Главное меню{server_settings[25]}\n\n"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📖 Помощь по игре", {"cmd": "help_game.Show"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
            )
        )
        return