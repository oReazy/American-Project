import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message):
    await database.setUserData(message.from_id, 'state', "'game_rule.Show'")
    setting_server = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 📖 Правила\n\n"
                f"{setting_server[19]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return