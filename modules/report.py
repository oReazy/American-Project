import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re, ast
from modules import database


# ------------------------------------------------------------------------------------------

async def Check(message: Message):
    await Show(message)
    return


async def Show(message: Message):
    database.setUserData(message.from_id, 'state', "'report.Show'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 📣 Связь с администрацией\n\n"
                f"💬 Вы собираетесь отправить сообщение для администрации. Будьте внимательны, чтобы ваш репорт не нарушал правила, "
                f"которые написаны ниже.\n\n"
                f"⛔ Запрещено:\n"
                f"— Флудить, оскорблять, оффтопить\n"
                f"— Просить что-либо (дайте денег, дайте лидеру, дайте что-то)\n"
                f"— Ложные сообщения\n\n"
                f"⚠ За нарушение данных правил, администрация в праве:\n"
                f"— Предупредить (Warn)\n"
                f"— Выдать вам мут или выдать только мут репорта (Mute)\n"
                f"— Заблокировать аккаунт (Ban)\n"
                f"— Удалить аккаунт (Delite)\n\n"
                f"Если вам долго не отвечают, подождите пару минут.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📣 Отправить репорт", {"cmd": "report.Send"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



async def Send(message: Message):
    database.setUserData(message.from_id, 'state', "'report.SendCheck'")
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 📣 » 📣 Отправить репорт\n\n"
                f"📝 Напишите ваш репорт",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "report.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return


async def SendCheck(message: Message):
    data = database.getUserData(message.from_id)
    await message.answer(
        message=f"✅ Ваш репорт был отправлен администрации",
    )
    database.setUserData(message.from_id, 'state', "'mainMenu.Show'")