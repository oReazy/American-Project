import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re, ast
from modules import database
from modules import characterAction


# ------------------------------------------------------------------------------------------

async def Show(message: Message):
    data = await database.getUserData(message.from_id)
    if data[60] == 'Нету':
        await message.answer(
            message=f"❌ У вас нет паспорта. Сделать вы его можете в правительстве")
        await characterAction.Show(message)
        return
    else:
        await database.setUserData(message.from_id, 'state', "'passport.Show'")
        temporary = ast.literal_eval(data[54])
        blacklist_end = ''
        count = 0
        while count < len(temporary):
            blacklist_end = blacklist_end + f'{temporary[count]}\n'
            count = count + 1
        if count == 0:
            await message.answer(
                message=f"🎯 » 👤 » 📕 Мой паспорт\n\n"
                        f"😀 Имя » {data[3]}\n"
                        f"🌐 Лет в штате » {data[6]}\n"
                        f"📕 Серия » {data[61]}\n"
                        f"📕 Номер » {data[62]}\n"
                        f"🚻 Семейное положение » {data[63]}\n"
                        f"🏠 Прописка » \n\n"
                        f"🛠 Работа » {data[43]}\n"
                        f"📓 Военный билет » {data[64]}\n\n"
                        f"{blacklist_end}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .get_json()
                )
            )
            return
        else:
            await message.answer(
                message=f"🎯 » 👤 » 📕 Мой паспорт\n\n"
                        f"😀 Имя » {data[3]}\n"
                        f"🌐 Лет в штате » {data[6]}\n"
                        f"📕 Серия » {data[61]}\n"
                        f"📕 Номер » {data[62]}\n"
                        f"🚻 Семейное положение » {data[63]}\n"
                        f"🏠 Прописка » \n\n"
                        f"🛠 Работа » {data[43]}\n"
                        f"📓 Военный билет » {data[64]}\n\n"
                        f"⛔ Вы находитесь в черных списках фракций:\n"
                        f"{blacklist_end}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .get_json()
                )
            )
            return