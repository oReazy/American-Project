import pymysql, json, re


def connect_base():  # Подключение к БД
    with open("data/database.json", 'r', encoding='UTF-8') as json_file:
        db = json.load(json_file)
    try:
        connected = pymysql.connect(
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            db=db['DATABASE']
        )
        print('\033[34m[i] Подключение к базе данных прошло \033[32mуспешно\033[34m (БД)')
        return connected
    except:
        print('\033[34m[!] Ошибка. Не удалось подключиться к базе данных (БД)')


def registerNewAccaunt(user_id):  # Создание нового аккаунта в базе данных
    try:
        connection = connect_base()
        with connection.cursor() as cursor:
            # new_user = "INSERT INTO `users` (vk_id, state, nick, mail, telephone, lvl, exp, sex, age, nationality, " \
            #            "admin, dollars, euro, yen, pounds, bank_dollars, bank_euro, bank_yen, bank_pounds, " \
            #            "tracing, donate, VIP, lider, member, rang, license_auto, license_motorbike, " \
            #            "license_cargocar, license_gun, license_fish, license_air, license_water, " \
            #            "license_hunting, warns, clothes_head, clothes_body, clothes_legs, " \
            #            "clothes_boots, clothes_hands, clothes_neck, numTelephone, drugs, " \
            #            "work, fighting_kung_fu, fighting_kneehed, fighting_boks, fighting_elbow, " \
            #            "fighting_selected, mask, skill_pistol, skill_ak47, skill_drubovic, " \
            #            "skill_sniper, blacklist, history_punish, history_nicks, history_reports, " \
            #            "health, eat, passport, passport_serial, passport_number, marriage, " \
            #            "military_card, casino_chips, admin_info, mailing_project, mailing_server, " \
            #            "bank_card, skill_farmer, skill_drive, skill_trucker, skill_taxi, skill_air
            #            "temporary_var) VALUES " \
            #            f"({user_id}, " \  # vk_id
            # f"'', " \  # state
            # f"'', " \  # nick
            # f"'', " \  # mail
            # f"'', " \  # telephone
            # f"'', " \  # lvl
            # f"'', " \  # exp
            # f"'', " \  # sex
            # f"'', " \  # age
            # f"'', " \  # nationality
            # f"'', " \  # admin
            # f"'', " \  # dollars
            # f"'', " \  # euro
            # f"'', " \  # yen
            # f"'', " \  # pounds
            # f"'', " \  # bank_dollars
            # f"'', " \  # bank_euro
            # f"'', " \  # bank_yen
            # f"'', " \  # bank_pounds
            # f"'', " \  # tracing
            # f"'', " \  # donate
            # f"'', " \  # VIP
            # f"'', " \  # lider
            # f"'', " \  # member
            # f"'', " \  # rang
            # f"'', " \  # license_auto
            # f"'', " \  # license_motorbike
            # f"'', " \  # license_cargocar
            # f"'', " \  # license_gun
            # f"'', " \  # license_fish
            # f"'', " \  # license_air
            # f"'', " \  # license_water
            # f"'', " \  # license_hunting
            # f"'', " \  # warns
            # f"'', " \  # clothes_head
            # f"'', " \  # clothes_body
            # f"'', " \  # clothes_legs
            # f"'', " \  # clothes_boots
            # f"'', " \  # clothes_hands
            # f"'', " \  # clothes_neck
            # f"'', " \  # numTelephone
            # f"'', " \  # drugs
            # f"'', " \  # work
            # f"'', " \  # fighting_kung_fu
            # f"'', " \  # fighting_kneehed
            # f"'', " \  # fighting_boks
            # f"'', " \  # fighting_elbow
            # f"'', " \  # fighting_selected
            # f"'', " \  # mask
            # f"'', " \  # skill_pistol
            # f"'', " \  # skill_ak47
            # f"'', " \  # skill_drubovic
            # f"'', " \  # skill_sniper
            # f"'', " \  # blacklist
            # f"'', " \  # history_punish
            # f"'', " \  # history_nicks
            # f"'', " \  # history_reports
            # f"'', " \  # health
            # f"'', " \  # eat
            # f"'', " \  # passport
            # f"'', " \  # passport_serial
            # f"'', " \  # passport_number
            # f"'', " \  # marriage
            # f"'', " \  # military_card
            # f"'', " \  # casino_chips
            # f"'', " \  # admin_info
            # f"'', " \  # mailing_project
            # f"'', " \  # mailing_server
            # f"'', " \  # bank_card
            # f"'', " \  # skill_farmer
            # f"'', " \  # skill_drive
            # f"'', " \  # skill_trucker
            # f"'', " \  # skill_taxi
            # f"'', " \  # skill_air
            # f"'', " \  # temporary_var
            # f")"
            admin_info = {"admin_name": "", "admin_age": "", "admin_city_live": "", "admin_discord": "",
                          "admin_desc": "", "admin_date_add": "", "admin_date_upp": "", "admin_date_leave": "",
                          "admin_status": "", "admin_post": ""}
            new_user = "INSERT INTO `users` (vk_id, state, nick, mail, telephone, lvl, exp, sex, age, nationality, " \
                       "admin, dollars, euro, yen, pounds, bank_dollars, bank_euro, bank_yen, bank_pounds, " \
                       "tracing, donate, VIP, lider, member, rang, license_auto, license_motorbike, " \
                       "license_cargocar, license_gun, license_fish, license_air, license_water, " \
                       "license_hunting, warns, clothes_head, clothes_body, clothes_legs, " \
                       "clothes_boots, clothes_hands, clothes_neck, numTelephone, drugs, " \
                       "work, fighting_kung_fu, fighting_kneehed, fighting_boks, fighting_elbow, " \
                       "fighting_selected, mask, skill_pistol, skill_ak47, skill_drubovic, " \
                       "skill_sniper, blacklist, history_punish, history_nicks, history_reports, " \
                       "health, eat, passport, passport_serial, passport_number, marriage, " \
                       "military_card, casino_chips, admin_info, mailing_project, mailing_server, " \
                       "bank_card, skill_farmer, skill_drive, skill_trucker, skill_taxi, skill_air, " \
                       "temporary_var) VALUES " \
                       f"({user_id}, " \
                       f"'', " \
                       f"'', " \
                       f"'No email address', " \
                       f"'❌ Отсутствует', " \
                       f"'1', " \
                       f"'0', " \
                       f"'', " \
                       f"'0', " \
                       f"'', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'❌ Отсутствует', " \
                       f"'Нет', " \
                       f"'Нет', " \
                       f"'0', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'0', " \
                       f"'Ничего', " \
                       f"'Ничего', " \
                       f"'Ничего', " \
                       f"'Ничего', " \
                       f"'Ничего', " \
                       f"'Ничего', " \
                       f"'0', " \
                       f"'0', " \
                       f"'Безработный', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'Бокс', " \
                       f"'Нету', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'100', " \
                       f"'100', " \
                       f"'Нету', " \
                       f"'0', " \
                       f"'0', " \
                       f"'Не женат(а)', " \
                       f"'❌ Отсутствует', " \
                       f"'0', " \
                       "'[]', " \
                       f"'❌ Не подписаны', " \
                       f"'❌ Не подписаны', " \
                       f"'❌ Отсутствует', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'[]'" \
                       f")"
            cursor.execute(new_user)
            connection.commit()
            connection.close()
            print(f'\033[33mВстречайте нового пользователя')
    except Exception as ex:
        print(f'\033[34m[!] Ошибка. Не удалось создать пользователя (он уже есть в БД)\n{ex}')


def getUserData(user_id):  # получение данных пользователя
    connection = connect_base()
    with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `vk_id` = {user_id}"
        cursor.execute(select_row)
        rows = cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data


def setUserData(user_id, key, value):  # Изменение переменных у пользователя (по одной переменной)
    connection = connect_base()
    with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {key} = {value} WHERE vk_id = {user_id}"
        cursor.execute(update_row)
        connection.commit()
        cursor.close()


def setMultiUserData(user_id, value):  # Изменение переменных у пользователя (несколько переменных)
    connection = connect_base()
    with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {value} WHERE vk_id = {user_id}"
        cursor.execute(update_row)
        connection.commit()
        cursor.close()


def deleteUserData(user_id):  # Удаление данных пользователя
    connection = connect_base()
    with connection.cursor() as cursor:
        delete_row = f"DELETE from `users` WHERE `vk_id` = {user_id}"
        cursor.execute(delete_row)
        connection.commit()
        cursor.close()


def findBaseData(key, value):  # найти значения в базе данных. Выводит их количестве в БД
    count_row = 0
    connection = connect_base()
    with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `{key}` = {value}"
        cursor.execute(select_row)
        rows = cursor.fetchall()
        for row in rows:
            count_row = count_row + 1
        connection.close()
    return count_row

# --------------------------------------------------------------------------------------------------

def getBdData(table, key, value):  # получение данных
    connection = connect_base()
    with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {key} = {value}"
        cursor.execute(select_row)
        rows = cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data


def setBdData(table, where_key, where_value, key, value):  # Изменение переменных (по одной переменной)
    connection = connect_base()
    with connection.cursor() as cursor:
        update_row = f"UPDATE `{table}` SET {key} = {value} WHERE {where_key} = {where_value}"
        cursor.execute(update_row)
        connection.commit()
        cursor.close()

def setMultiDbData(table, where_key, where_value, value):  # Изменение переменных (несколько переменных)
    connection = connect_base()
    with connection.cursor() as cursor:
        update_row = f"UPDATE `{table}` SET {value} WHERE {where_key} = {where_value}"
        cursor.execute(update_row)
        connection.commit()
        cursor.close()

# --------------------------------------------------------------------------------------------------
# Код который ниже написан не связан с базами данных

async def exitBot():  # делает выход из активной переписки
    return
    # try:
    #     exit(0)
    # except:
    #     pass

async def pretty(num):
    num1 = re.sub(r'\d(?=(?:\d{3})+(?!\d))', r'\g<0> ', str(num))
    return num1


def regularCheck(key, value):
    # data = database.getUserData(message.from_id)
    # database.setUserData(message.from_id, 'state', "'settings.addMail_check'")
    validate = re.match(rf'{key}', value, flags=re.IGNORECASE)
    validate = str(validate)
    if validate == 'None':
        return 0, value
    else:
        return 1, value