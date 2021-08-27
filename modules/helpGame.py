import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re
from modules import database


# ------------------------------------------------------------------------------------------

async def Show(message):
    await database.setUserData(message.from_id, 'state', "'helpGame.Show'")
    setting_server = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 📖 Помощь по игре\n\n"
                f"ℹ {setting_server[8]} — игровой чат-бот, где вы можете зарабатывать игровые деньги, вступать в организации и семьи, "
                f"участвовать в мероприятиях и многое другое. Так-как в нашем чат-боте очень много систем, у многих игроков возникают "
                f"вопросы, ответы на которые можно получить тут.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔰 Часто задаваемые вопросы", {"cmd": "helpGame.List1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Как заработать первые деньги?", {"cmd": "helpGame.List2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Виды лицензий", {"cmd": "helpGame.List3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Банковская карта", {"cmd": "helpGame.List4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )
    return


async def List4(message):
    await database.setUserData(message.from_id, 'state', "'helpGame.List4'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Банковская карта\n\n"
                f"Получить банковскую карту можно в центральном отделении банка. Найти его можно на карте -> важные места -> центральный банк. "
                f"После получения банковской карты, вы можете положить на ее счет деньги, открывать вклады, сбережения, цели и много другое.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def List3(message):
    await database.setUserData(message.from_id, 'state', "'helpGame.List3'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Виды лицензий\n\n"
                f"В данный момент на проекте существует 8 видов лицензий.\n\n"
                f"🚗 Лицензия на автомобили » Вы сможете водить легковыми автомобилями, тем самым вы сможете управлять своим личным автомобилем\n"
                f"🏍 Лицензия на мотоциклы » Вы сможете брать в аренду мотоциклы, либо сможете управлять своим мотоциклом\n"
                f"🚚 Лицензия на грузовой транспорт » Вы сможете работать на грузовом транспорте (например на дальнобое)\n"
                f"🔫 Лицензия на оружие » Вы сможете покупать оружие в аммунации\n"
                f"🐠 Лицензия на ловлю рыбы » Вы сможете ловить рыбу в море легально\n"
                f"🛩 Лицензия на воздушный транспорт » Вы сможете управлять летательными средствами (вертолеты, самолеты). Также у вас появится возможность работать пилотом\n"
                f"🛥 Лицензия на водный транспорт » Вы сможете управлять водными средствами (лодки, яхты, катера). Также у вас появится возможность рыбачить.\n"
                f"🐅 Лицензия на охоту » Вы сможете легально вести охоту на животных в лесу\n\n"
                f"💬 Некоторые лицензии можно получить в центре лицензирования, но некоторые можно только в полиции.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def List2(message):
    await database.setUserData(message.from_id, 'state', "'helpGame.List2'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Как заработать первые деньги?\n\n"
                f"Для того, чтобы заработать первые деньги, вам необходимо зайти в карту -> Работы для новичков -> Выберите более подходящую работу для вас. "
                f"Как только вы заработаете деньги, купите лицензии и накопите уровень, то вы сможете остроится на основные работы, либо во фракцию!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return


async def List1(message):
    await database.setUserData(message.from_id, 'state', "'helpGame.List1'")
    await message.answer(
        message=f"🎯 » 📖 » 🔰 Часто задаваемые вопросы\n\n"
                f"Как можно получить паспорт? — Паспорт можно получить в мэрии\n"
                f"Где можно получить лицензию на авто? — Лицензию на легковые автомобили можно получить в центре лицензирования\n"
                f"Где можно получить какую-либо лицензию? — Любые лицензии можно получить в центре лицензирования\n"
                f"Как заработать первые деньги? — Откройте карту -> работы для новичков\n"
                f"Как можно вступить во фракцию? — Следите за новостями сервера. Как только начнется набор, вам необходимо прийти во фракцию, далее на собеседование\n"
                f"Как можно стать лидером? — Через обзвон.\n"
                f"Можно ли купить админку или как стать админом? — Админку купить нельзя! Стать администратором вы можете через пост лидера, либо через обзвон.\n"
                f"Как можно отписаться/подписаться на рассылки? — Откройте настройки персонажа -> рассылки\n"
                f"Где можно купить дом? — В риэлторском агентстве\n"
                f"Где можно купить машину? — Откройте карту -> Автосалоны",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )
    return