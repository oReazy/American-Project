import asyncio

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys
from modules import database


# --------------------------------------------------------------------------------

async def Show(message):
    print('Пользователь заблокирован. Действия невозможны')
    return
