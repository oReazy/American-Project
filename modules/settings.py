import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys, re
from modules import database
import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# ------------------------------------------------------------------------------------------

async def Show(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.Show'")
    await message.answer(
        message=f"🎯 » ⚙ Настройки персонажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("✉ Email", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📬 Рассылки", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def Email(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.Email'")
    if data[4] == 'No email address':
        await message.answer(
            message=f"🎯 » ⚙ » ✉ Email\n\n"
                    f"❌ Почта не установлена\n\n"
                    f"ℹ Мы рекомендуем добавить электронную почту, так-как это дополнительно "
                    f"обезопасит ваш аккаут: на данную электронную почту мы будем отправлять "
                    f"сообщения о подозрительных действий с вашим аккаунтом.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("✉ Добавить почту", {"cmd": "settings.addMail"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return
    else:
        await message.answer(
            message=f"🎯 » ⚙ » ✉ Email\n\n"
                    f"✉ Привязана почта » {data[4]}\n\n"
                    f"💬 На указанную электронную почту мы будем отправлять сообщения о "
                    f"подозрительных действий на вашем аккаунте. В случае, если вам надо поменять почту, "
                    f"нажмите на кнопку ниже.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("✉ Изменить почту", {"cmd": "settings.editMail"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
        return


async def addMail(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.addMail_check'")
    await message.answer(
        message=f"🎯 » ⚙ » ✉ » ✉ Добавить почту\n\n"
                f"📝 Введите электронную почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Email"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return

async def addMail_check(message: Message):
    result = database.regularCheck('^(?!.*@.*@.*$)(?!.*@.*\-\-.*\..*$)(?!.*@.*\-\..*$)(?!.*@.*\-$)(.*@.+(\..{1,11})?)$', str(message.text))
    if result[0] == 1:
        await database.setUserData(message.from_id, 'mail', f"'{result[1]}'")
        await addMail_OK(message)
    else:
        await message.answer(
            message=f"❌ Ошибка. Такой почты не существует, либо вы ее написали неправильно"
        )
        await addMail(message)
    return


async def addMail_check(message: Message):
    result = database.regularCheck('^(?!.*@.*@.*$)(?!.*@.*\-\-.*\..*$)(?!.*@.*\-\..*$)(?!.*@.*\-$)(.*@.+(\..{1,11})?)$', str(message.text))
    if result[0] == 1:
        await database.setUserData(message.from_id, 'mail', f"'{result[1]}'")
        await addMail_OK(message)
    else:
        await message.answer(
            message=f"❌ Ошибка. Такой почты не существует, либо вы ее написали неправильно"
        )
        await addMail(message)
    return


async def addMail_OK(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.addMail_OK'")
    await message.answer(
        message=f"✅ Вы успешно добавили почту.\n\n"
                f"⚠ Для максимальной безопасности, мы рекомендуем вам поставить двухфакторную аунтификацию от ВКонтакте. В случае, "
                f"если она у вас уже стоит, то беспокоится не надо",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def editMail(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.editMail_check'")
    await message.answer(
        message=f"🎯 » ⚙ » ✉ » ✉ Изменить почту\n\n"
                f"📝 Введите новую электронную почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Email"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )
    return

async def editMail_check(message: Message):
    result = await database.regularCheck('^(?!.*@.*@.*$)(?!.*@.*\-\-.*\..*$)(?!.*@.*\-\..*$)(?!.*@.*\-$)(.*@.+(\..{1,11})?)$', str(message.text))
    print(result)
    if result[0] == 1:
        await database.setUserData(message.from_id, 'mail', f"'{result[1]}'")
        await editMail_OK(message)
    else:
        await message.answer(
            message=f"❌ Ошибка. Такой почты не существует, либо вы ее написали неправильно"
        )
        await editMail(message)
    return


async def editMail_OK(message: Message):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.editMail_OK'")
    await message.answer(
        message=f"✅ Вы успешно изменили почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return



# ---------------------------------------------------------------------------------------------------------------
# РАССЛЫКИ
async def Mailing(message: Message):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'settings.Mailing'")

    KEYBOARD_MAILING = Keyboard(one_time=True, inline=False)
    KEYBOARD_MAILING.add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD_MAILING.row()
    temporary = str(data[67])
    if temporary != '❌ Не подписан':
        KEYBOARD_MAILING.add(Text("📮 Отписаться от рассылок проекта", {"cmd": "settings.MailingLeaveProject"}), color=KeyboardButtonColor.SECONDARY)
    else:
        KEYBOARD_MAILING.add(Text("📮 Подписаться на рассылки проекта", {"cmd": "settings.MailingAddProject"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_MAILING.row()
    temporary = str(data[68])
    if temporary != '❌ Не подписан':
        KEYBOARD_MAILING.add(Text("📮 Отписаться от рассылок сервера", {"cmd": "settings.MailingLeaveServer"}), color=KeyboardButtonColor.SECONDARY)
    else:
        KEYBOARD_MAILING.add(Text("📮 Подписаться на рассылки сервера", {"cmd": "settings.MailingAddServer"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_MAILING = KEYBOARD_MAILING.get_json()

    await message.answer(
        message=f"🎯 » ⚙ » 📬 Рассылки\n\n"
                f"📮 Рассылка с новостями проекта » {data[67]} » 💵 {await database.pretty(server_settings[12])}\n"
                f"📮 Рассылка с новостями сервера » {data[68]} » 💵 {await database.pretty(server_settings[13])}\n\n"
                f"💵 Мы платим за рассылки! Читайте новости нашего проекта и получайте гарантированное вознаграждение за это. Для того, "
                f"чтобы получить вознаграждение, вам необходимо нажать на специальную кнопку в рассылке и после чего вы получите деньги.\n"
                f"Кроме этого, в наших рассылках мы информируем наших игроков о грядущих обновляниях, а серверная рассылка позволяет "
                f"следить за новостями вашего сервера: мероприятия, РП-ситуации, наборы во фракции и многое другое.",
        keyboard=KEYBOARD_MAILING
    )
    return



async def MailingLeaveProject(message: Message):
    await database.setMultiUserData(message.from_id, "mailing_project = '❌ Не подписан', state = 'settings.MailingLeaveProject'")
    await message.answer(
        message=f"😭 Вы отписались от рассылки с новостями проекта\n\n"
                f"👉🏻 Теперь вы не будете получать вознаграждений от рассылок, так-как они к вам больше не поступают. "
                f"Если вы передумаете и решите снова подписаться на рассылки, то перейдите в раздел «Настройки персонажа» в "
                f"раздел «Рассылки».",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def MailingAddProject(message: Message):
    await database.setMultiUserData(message.from_id, "mailing_project = '✅ Подписан', state = 'settings.MailingAddProject'")
    await message.answer(
        message=f"🎉 Вы подписались на новости проекта\n\nМы благодарим вас за подписку на рассылку новостей от проекта. В ней "
                f"мы рассказываем о будущих обновлениях, так и об актуальных. Никакой воды и рекламы, только все по делу. Также "
                f"мы предалгаем каждому нашему игроку, который подписался на новости, небольшой бонус. Узнать сумму бонуса "
                f"можно в «Настройки персонажа» в разделе «Рассылки»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def MailingLeaveServer(message: Message):
    await database.setMultiUserData(message.from_id, "mailing_server = '❌ Не подписан', state = 'settings.MailingLeaveServer'")
    await message.answer(
        message=f"😭 Вы отписались от рассылки с новостями сервера\n\n"
                f"👉🏻 Теперь вы не будете получать вознаграждений от рассылок, так-как они к вам больше не поступают. "
                f"Если вы передумаете и решите снова подписаться на рассылки, то перейдите в раздел «Настройки персонажа» в "
                f"раздел «Рассылки».",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return


async def MailingAddServer(message: Message):
    await database.setMultiUserData(message.from_id, "mailing_server = '✅ Подписан', state = 'settings.MailingAddServer'")
    await message.answer(
        message=f"🎉 Вы подписались на новости сервера\n\nМы благодарим вас за подписку на рассылку новостей от сервера. В ней "
                f"мы рассказываем о мероприятиях, новостях, наборах во фракции и различные РП-ситуации. Также "
                f"мы предалгаем каждому нашему игроку, который подписался на новости, небольшой бонус. Узнать сумму бонуса "
                f"можно в «Настройки персонажа» в разделе «Рассылки»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )
    return