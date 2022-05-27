-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 27 2022 г., 09:05
-- Версия сервера: 10.4.24-MariaDB
-- Версия PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `game`
--

-- --------------------------------------------------------

--
-- Структура таблицы `bisness`
--

CREATE TABLE `bisness` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `owner` text NOT NULL,
  `owner_id` int(11) NOT NULL,
  `coast` int(11) NOT NULL,
  `bisness_image` int(11) NOT NULL,
  `inventory` text NOT NULL,
  `products` text NOT NULL,
  `vices` text NOT NULL,
  `EnterPrice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `centralmarket`
--

CREATE TABLE `centralmarket` (
  `id` int(11) NOT NULL,
  `status` text NOT NULL,
  `items` text NOT NULL,
  `vk_id` int(11) NOT NULL,
  `history` text NOT NULL,
  `hash` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `centralmarket`
--

INSERT INTO `centralmarket` (`id`, `status`, `items`, `vk_id`, `history`, `hash`) VALUES
(1, 'продажа', '[[3, 100, 984]]', 687861725, '[\'Вы продали предмет (ID: 3) в кол-ве 2 и заработали 1986\', \'Вы продали предмет (ID: 3) в кол-ве 2 и заработали 200\', \'Вы продали предмет (ID: 3) в кол-ве 5 и заработали 500\', \'Вы продали предмет (ID: 3) в кол-ве 1 и заработали 100\', \'Вы продали предмет (ID: 3) в кол-ве 1 и заработали 100\']', '734462344238'),
(2, 'продажа', '[]', 340311937, '[]', '5898836124'),
(3, 'продажа', '[[1, 500, 1000], [0, 10000, 5], [6, 700000, 20], [5, 320000, 20], [4, 70000, 20]]', 340311937, '', '51894011510'),
(4, 'free', '[]', 0, '', ''),
(5, 'free', '[]', 0, '', ''),
(6, 'free', '[]', 0, '', ''),
(7, 'free', '[]', 0, '', ''),
(8, 'free', '[]', 0, '', ''),
(9, 'free', '[]', 0, '', ''),
(10, 'free', '[]', 0, '', ''),
(11, 'free', '[]', 0, '', ''),
(12, 'free', '[]', 0, '', '');

-- --------------------------------------------------------

--
-- Структура таблицы `event`
--

CREATE TABLE `event` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `count` int(11) NOT NULL,
  `playersOnline` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `event`
--

INSERT INTO `event` (`id`, `name`, `count`, `playersOnline`) VALUES
(0, 'Собиратели', 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `fractions`
--

CREATE TABLE `fractions` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `leader` text NOT NULL,
  `link_beseda` text NOT NULL,
  `advert` text NOT NULL,
  `NAME_RANGS` text NOT NULL,
  `SALARY_RANGS` text NOT NULL,
  `bank` int(11) NOT NULL,
  `open_sobes` int(11) NOT NULL,
  `resumes` text CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `fractions`
--

INSERT INTO `fractions` (`id`, `name`, `leader`, `link_beseda`, `advert`, `NAME_RANGS`, `SALARY_RANGS`, `bank`, `open_sobes`, `resumes`) VALUES
(1, 'Мэрия', 'Не назначен!', '', '', '[\'Губернатор\', \'Зам. губернатора\', \'Руководитель мэрии\', \'Аудитор \', \'Ст. сотрудник правительства\', \'Руководство СБ\', \'Старший Агент СБ\', \'Агент СБ \', \'Охранник \', \'Водитель\']', '[100000, 80000, 65000, 55000, 45000, 30000, 25000, 15000, 10000, 7500]', 0, 0, '[]'),
(2, 'Полиция 1', 'Не назначен!', '', '', '[\'Шеф\', \'Заместитель шефа\', \'Инспектор\', \'Командор\', \'Капитан\', \'Лейтенант\', \'Детектив\', \'Сержант\', \'Офицер\', \'Кадет\']', '[90000, 70000, 60000, 55000, 50000, 35000, 25000, 15000, 10000, 4500]', 0, 0, '[]'),
(3, 'Полиция 2', 'Не назначен!', '', '', '[\'Шеф\', \'Заместитель шефа\', \'Инспектор\', \'Командор\', \'Капитан\', \'Лейтенант\', \'Детектив\', \'Сержант\', \'Офицер\', \'Кадет\']', '[90000, 70000, 60000, 55000, 50000, 35000, 25000, 15000, 10000, 4500]', 0, 0, '[]'),
(4, 'Полиция 3', 'Не назначен!', '', '', '[\'Шеф\', \'Заместитель шефа\', \'Инспектор\', \'Командор\', \'Капитан\', \'Лейтенант\', \'Детектив\', \'Сержант\', \'Офицер\', \'Кадет\']', '[90000, 70000, 60000, 55000, 50000, 35000, 25000, 15000, 10000, 4500]', 0, 0, '[]'),
(5, 'FBI', 'Не назначен!', '', '', '[\'Директор \', \'Зам. директора\', \' Глава отдела \', \'Зам. гл. отдела \', \'Старший агент\', \'Агент\', \'Мл. агент\', \'Курсант III\', \'Курсант II\', \'Курсант I\']', '[120000, 100000, 80000, 65000, 55000, 50000, 40000, 20000, 10000, 5000]', 0, 0, '[]'),
(6, 'Радиостанция 1', 'Jackson', '', '', '[\'Директор \', \'Главный редактор\', \' Редактор\', \'Режиссер\', \'Репортер\', \'Ведущий\', \'Корреспондент\', \'Журналист\', \'Корректор\', \'Практикант\']', '[95000, 80000, 70000, 65000, 55000, 50000, 30000, 20000, 7500, \'5000\']', 10000000, 1, '[[576224130, \'Я lost Samurai,мне 18, да я местный, но без прописки. Я выбрал вашу работу и за того, что хочу работать на радио,просто душа просит\', \'Lost Samurai\', 2, \'Мужчина\'], [642129380, \'Московия за Российскую империю!\', \'Грейзель\', 1308, \'Мужчина\']]');

-- --------------------------------------------------------

--
-- Структура таблицы `homes`
--

CREATE TABLE `homes` (
  `id` int(11) NOT NULL,
  `owner` text NOT NULL,
  `owner_id` int(11) NOT NULL,
  `coast` int(11) NOT NULL,
  `home_image` int(11) NOT NULL,
  `home_interior` int(11) NOT NULL,
  `inventory` text NOT NULL,
  `updates` text NOT NULL,
  `class` text NOT NULL,
  `garage` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `hotels`
--

CREATE TABLE `hotels` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `promo`
--

CREATE TABLE `promo` (
  `id` int(11) NOT NULL,
  `creator_vk_id` int(11) NOT NULL,
  `code` text NOT NULL,
  `lvl` int(11) NOT NULL,
  `activation_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `promo`
--

INSERT INTO `promo` (`id`, `creator_vk_id`, `code`, `lvl`, `activation_count`) VALUES
(1, 340311937, '#jackson', 9, 501),
(2, 3404, '#test', 10, 2),
(3, 642129380, '#SlavaRimskoyimperii', 1, 2),
(4, 321988444, '#Оооооо,Магаааа', 1, 0),
(5, 529365911, '#TW1NKE', 1, 0),
(6, 551012435, '#atiks', 1, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `report`
--

CREATE TABLE `report` (
  `id` int(11) NOT NULL,
  `vk_id_user` int(11) NOT NULL,
  `nick_user` text NOT NULL,
  `vk_id_admin` int(11) NOT NULL,
  `nick_admin` text NOT NULL,
  `text` text CHARACTER SET utf8mb4 NOT NULL,
  `answer` text CHARACTER SET utf8mb4 NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `report`
--

INSERT INTO `report` (`id`, `vk_id_user`, `nick_user`, `vk_id_admin`, `nick_admin`, `text`, `answer`, `data`) VALUES
(1, 99156029, 'BTest', 340311937, 'Jackson', '123123', 'Спасибо за ваш ответ!', '21.4.2022 14:44:22'),
(2, 340311937, 'Jackson', 340311937, 'Jackson', 'Test', 'dfas', '21.4.2022 14:52:4'),
(3, 340311937, 'Jackson', 340311937, 'Jackson', 'Привет', 'Добрый день', '21.4.2022 15:31:5'),
(4, 642129380, 'Грейзель', 340311937, 'Jackson', 'Дайте донат на дошик плиз?', 'Выдал. Читай беседу в Discord', '22.4.2022 16:48:53'),
(5, 642129380, 'Грейзель', 340311937, 'Jackson', 'Есть живой?', 'Есть, а как ты узнал, что я живой? 🍕', '23.4.2022 14:3:41');

-- --------------------------------------------------------

--
-- Структура таблицы `settings`
--

CREATE TABLE `settings` (
  `id` int(11) NOT NULL,
  `name_project` text NOT NULL,
  `name_server` text NOT NULL,
  `project_link` text NOT NULL,
  `server_link` text NOT NULL,
  `open_registration` int(11) NOT NULL,
  `rules_server` text CHARACTER SET utf8mb4 NOT NULL,
  `rules_admin` text CHARACTER SET utf8mb4 NOT NULL,
  `faq_admin` text CHARACTER SET utf8mb4 NOT NULL,
  `statistics_friend` int(11) NOT NULL,
  `statistics_list_chatbot` int(11) NOT NULL,
  `statistics_search` int(11) NOT NULL,
  `statistics_youtube` int(11) NOT NULL,
  `statistics_other` int(11) NOT NULL,
  `pay_mailing_project` int(11) NOT NULL,
  `pay_mailing_server` int(11) NOT NULL,
  `cource_wallet` text NOT NULL,
  `bonus_dollars` int(11) NOT NULL,
  `bonus_lvl` int(11) NOT NULL,
  `bonus_donate` int(11) NOT NULL,
  `multi_payday` int(11) NOT NULL,
  `stocks` text CHARACTER SET utf8mb4 NOT NULL,
  `donate_buyXP` int(11) NOT NULL,
  `donate_buyDollars` int(11) NOT NULL,
  `cource_donate` int(11) NOT NULL,
  `multi_exp` int(11) NOT NULL,
  `multi_salary` int(11) NOT NULL,
  `advert_access` text CHARACTER SET utf8mb4 NOT NULL,
  `advert_edit` text CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `settings`
--

INSERT INTO `settings` (`id`, `name_project`, `name_server`, `project_link`, `server_link`, `open_registration`, `rules_server`, `rules_admin`, `faq_admin`, `statistics_friend`, `statistics_list_chatbot`, `statistics_search`, `statistics_youtube`, `statistics_other`, `pay_mailing_project`, `pay_mailing_server`, `cource_wallet`, `bonus_dollars`, `bonus_lvl`, `bonus_donate`, `multi_payday`, `stocks`, `donate_buyXP`, `donate_buyDollars`, `cource_donate`, `multi_exp`, `multi_salary`, `advert_access`, `advert_edit`) VALUES
(1, 'American Project', 'Test', 'news.americanproject', 'test.americanproject', 1, 'Главный администратор еще не написал правила для данного сервера', 'Главный администратор еще не написал устав для администрации', 'Главный администратор еще не написал FAQ админ-панели для администрации', 5, 1, 2, 0, 7, 10000, 10000, '[0.91,128.07,0.76,1.09, 138.53, 0.82, 0.0078, 0.0072, 0.0059, 1.31, 1.21, 168,22]', 200, 1, 3000, 4, ' • Скоро новое обновление', 3, 1000, 1, 1, 1, '[]', '[]');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `vk_id` int(11) NOT NULL,
  `state` text NOT NULL,
  `nick` text NOT NULL,
  `mail` text NOT NULL,
  `telephone` text NOT NULL,
  `lvl` int(11) NOT NULL,
  `exp` int(11) NOT NULL,
  `sex` text NOT NULL,
  `age` int(11) NOT NULL,
  `nationality` text NOT NULL,
  `admin` int(11) NOT NULL,
  `dollars` int(11) NOT NULL,
  `euro` int(11) NOT NULL,
  `yen` int(11) NOT NULL,
  `pounds` int(11) NOT NULL,
  `bank_dollars` int(11) NOT NULL,
  `bank_euro` int(11) NOT NULL,
  `bank_yen` int(11) NOT NULL,
  `bank_pounds` int(11) NOT NULL,
  `donate` int(11) NOT NULL,
  `VIP` text NOT NULL,
  `member` text NOT NULL,
  `rang` int(11) NOT NULL,
  `license` text NOT NULL,
  `warns` text NOT NULL,
  `clothes` text NOT NULL,
  `work` text NOT NULL,
  `fighting` text NOT NULL,
  `skillArmor` text NOT NULL,
  `skillWorks` text NOT NULL,
  `blacklist` text NOT NULL,
  `history_punish` text NOT NULL,
  `history_nicks` text NOT NULL,
  `history_reports` text NOT NULL,
  `passport` text NOT NULL,
  `passport_serial` int(11) NOT NULL,
  `passport_number` int(11) NOT NULL,
  `marriage` text NOT NULL,
  `military_card` text NOT NULL,
  `admin_info` text NOT NULL,
  `mailing_project` text NOT NULL,
  `mailing_server` text NOT NULL,
  `bank_card` text NOT NULL,
  `temporary_var` text CHARACTER SET utf8mb4 NOT NULL,
  `limit_report` int(11) NOT NULL,
  `last_message` int(11) NOT NULL,
  `reDesign` int(11) NOT NULL,
  `inventory` text NOT NULL,
  `family` text NOT NULL,
  `timeEventCollectors` int(11) NOT NULL,
  `notes_telephone` text NOT NULL,
  `promocode` text NOT NULL,
  `warn_fraction` int(11) NOT NULL,
  `temporary_var2` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `vk_id`, `state`, `nick`, `mail`, `telephone`, `lvl`, `exp`, `sex`, `age`, `nationality`, `admin`, `dollars`, `euro`, `yen`, `pounds`, `bank_dollars`, `bank_euro`, `bank_yen`, `bank_pounds`, `donate`, `VIP`, `member`, `rang`, `license`, `warns`, `clothes`, `work`, `fighting`, `skillArmor`, `skillWorks`, `blacklist`, `history_punish`, `history_nicks`, `history_reports`, `passport`, `passport_serial`, `passport_number`, `marriage`, `military_card`, `admin_info`, `mailing_project`, `mailing_server`, `bank_card`, `temporary_var`, `limit_report`, `last_message`, `reDesign`, `inventory`, `family`, `timeEventCollectors`, `notes_telephone`, `promocode`, `warn_fraction`, `temporary_var2`) VALUES
(2, 321988444, 'telephone.ForbesLVL', 'AZAZA7075', '❌ Отсутствует', 'Xiaomi Mi 11 Lite', 7, 19, 'Мужчина', 44, 'Американец', 0, -196835, 0, 0, 0, 300, 0, 0, 0, 0, '[\'no vip\', 0]', 'Без организации', 0, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Доставщик пиццы', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[7503, 0, 5000, 0, 0]', '[\'24.4.2022 — Радиостанция 1\']', '[\'23.04.2022 — бан на 30 дней\', \'23.04.2022 — мут на 30 минут\']', '[]', '[]', '✅ Имеется', 2289, 923535, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '❌ Не подписан', '✅ Имеется', '[0, \'скупка\', 687861725]', 0, 1651161334, 0, '[0, 0, 0, 0, 140, 0, 0]', '-1', 1650743311, '❌ Заметок нет', '#SlavaRimskoyimperii', 0, ''),
(3, 642129380, 'mainMenu.Mini', 'Грейзель', 'qreyzel@vk.com', 'iPhone 13', 1308, 1933, 'Мужчина', 20, 'Украинец', 0, 40200, 0, 0, 0, 66310, 3244, 0, 0, 14651, '[\'PREMIUM\', 10]', 'Без организации', 0, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Доставщик пиццы', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[7520, 0, 5000, 10000, 0]', '[\'24.4.2022 — Радиостанция 1\']', '[]', '[]', '[]', '✅ Имеется', 8928, 534103, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '✅ Подписан', '✅ Имеется', '[0, \'скупка\', 687861725, 3]', 1650712001, 1651168493, 1, '[0, 0, 0, 4, 0, 0, 0]', '-1', 1650743575, 'Хеллоу мазафака', '#test', 0, ''),
(4, 525047383, 'mainMenu.Mini', 'Denis', '❌ Отсутствует', '❌ Отсутствует', 1, 0, 'Мужчина', 18, 'Украинец', 0, 650, 0, 0, 0, 0, 0, 0, 0, 1100, '[\'no vip\', 0]', 'Без организации', 0, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Фермер', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[7509, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '❌ Отсутствует', 0, 0, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '❌ Не подписан', '❌ Не подписан', '❌ Отсутствует', '2', 0, 1650750037, 1, '[0, 0, 0, 0, 0, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, ''),
(6, 340311937, 'CentralMarket.ArendaMenu', 'Jackson', '❌ Отсутствует', 'iPhone 13', 13, 16, 'Мужчина', 22, 'Американец', 8, 10491655, 5487, 2561, 0, 360000, 0, 0, 0, 15425, '[\'no vip\', 0]', 'Радиостанция 1', 4, '[\'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Работник склада', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[29, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '❌ Отсутствует', 0, 0, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '❌ Не подписан', '❌ Не подписан', '✅ Имеется', '3', 1650544445, 1653252660, 1, '[0, 0, 0, 124, 0, 0, 1]', '-1', 1650743086, 'Привет заметочная!', '#test', 0, '[4, 70000, 20]'),
(8, 161335001, 'farm.rab4_13', 'KilonPlay', '❌ Отсутствует', '❌ Отсутствует', 1, 0, 'Мужчина', 18, 'Русский', 0, 300, 0, 0, 0, 0, 0, 0, 0, 1100, '[\'no vip\', 0]', 'Без организации', 0, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Фермер', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[7503, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '✅ Имеется', 7083, 788899, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '❌ Не подписан', '❌ Отсутствует', '1', 0, 1650554904, 0, '[0, 0, 0, 0, 0, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, ''),
(9, 99156029, 'mainMenu.Show', 'BTest', '❌ Отсутствует', '❌ Отсутствует', 1, 1, 'Мужчина', 21, 'Японец', 0, 240, 0, 0, 0, 0, 0, 0, 0, 1500, '[\'no vip\', 0]', 'Без организации', 0, '[\'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Фермер', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[32, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '✅ Имеется', 9445, 859001, 'Не женат(а)', '❌ Отсутствует', '[\'Тестер\', \'18\', \'Москва\', \'Ваша Честь, прошу учесть!#3816\', \'Тестер\', \'Администратор снят\', [\'21.4.2022 — поставлен на 1 уровень\', \'21.4.2022 — снят с поста администратора\'], [\'21.4.2022 — поставлен на 1 уровень\', \'21.4.2022 — изменен на 8 уровень\', \'21.4.2022 — снят с поста администратора 8 уровня\'], \'Администратор\', \'Администратор\']', '✅ Подписан', '❌ Не подписан', '❌ Отсутствует', '[]', 1650541642, 1650542888, 1, '[0, 0, 0, 0, 0, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, ''),
(10, 551012435, 'mainMenu.Show', 'ATiks', '❌ Отсутствует', 'Xiaomi Redmi Note 8 Pro', 9, 13, 'Мужчина', 18, 'Русский', 0, 25592, 184, 0, 0, 1142, 2, 256, 4, 1190, '[\'Bronze\', 1653218532]', 'Без организации', 0, '[\'❌ Отсутствует\', \'✅ Имеется\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Доставщик пиццы', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[12, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '✅ Имеется', 5019, 445393, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '❌ Не подписан', '✅ Имеется', '2', 0, 1650905840, 0, '[0, 0, 0, 15, 1, 1, 0]', '-1', 1650823210, '.', '#jackson', 0, ''),
(11, 529365911, 'CentralMarket.Arenda', 'Egor Marlis', '❌ Отсутствует', 'SAMSUNG Galaxy S21', 8, 9, 'Мужчина', 25, 'Русский', 0, 175950, 0, 0, 0, 5150, 0, 0, 0, 1001, '[\'Silver\', 10]', 'Радиостанция 1', 1, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Доставщик пиццы', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[0, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '✅ Имеется', 4256, 233976, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '❌ Не подписан', '✅ Имеется', '[1, \'продажа\', 687861725, \'734462344238\']', 0, 1653235242, 0, '[0, 0, 0, 16, 0, 0, 0]', '-1', 1650742901, 'я крутой', '#SlavaRimskoyimperii', 0, ''),
(12, 576224130, 'farm.rab4_16', 'Lost Samurai', '❌ Отсутствует', '❌ Отсутствует', 2, 4, 'Мужчина', 18, 'Русский', 0, 2465, 0, 0, 0, 5914, 9, 0, 0, 2597, '[\'no vip\', 0]', 'Без организации', 0, '[\'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\', \'✅ Имеется\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Фермер', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[7587, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '✅ Имеется', 9905, 858485, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '✅ Подписан', '❌ Не подписан', '✅ Имеется', '2', 0, 1653244245, 0, '[0, 0, 0, 1, 0, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, ''),
(14, 687861725, 'characterAction.Show', 'Platomn', '❌ Отсутствует', '❌ Отсутствует', 1, 1, 'Мужчина', 22, 'Американец', 0, 544840, 0, 0, 0, 0, 0, 0, 0, 3000, '[\'no vip\', 0]', 'Без организации', 0, '[\'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Безработный', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[0, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '❌ Отсутствует', 0, 0, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '❌ Не подписан', '❌ Не подписан', '❌ Отсутствует', '[0, \'скупка\', 687861725, 3]', 0, 1653217982, 1, '[0, 0, 0, 178, 200, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, ''),
(15, 443081089, 'mainMenu.Show', 'Nick', '❌ Отсутствует', '❌ Отсутствует', 1, 1, 'Мужчина', 22, 'Канадец', 0, 200, 0, 0, 0, 0, 0, 0, 0, 3000, '[\'no vip\', 0]', 'Без организации', 0, '[\'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\', \'❌ Отсутствует\']', '[]', '[\'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\', \'Пусто\']', 'Безработный', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[0, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '❌ Отсутствует', 0, 0, 'Не женат(а)', '❌ Отсутствует', '[\'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\']', '❌ Не подписан', '❌ Не подписан', '❌ Отсутствует', '[2, \'продажа\', 340311937, \'75596516755\']', 0, 1653238214, 0, '[0, 0, 0, 0, 0, 0, 0]', '-1', 0, '❌ Заметок нет', '', 0, '');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `bisness`
--
ALTER TABLE `bisness`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `cars`
--
ALTER TABLE `cars`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `centralmarket`
--
ALTER TABLE `centralmarket`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `fractions`
--
ALTER TABLE `fractions`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `homes`
--
ALTER TABLE `homes`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `hotels`
--
ALTER TABLE `hotels`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `promo`
--
ALTER TABLE `promo`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `report`
--
ALTER TABLE `report`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `settings`
--
ALTER TABLE `settings`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `bisness`
--
ALTER TABLE `bisness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `centralmarket`
--
ALTER TABLE `centralmarket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `event`
--
ALTER TABLE `event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `fractions`
--
ALTER TABLE `fractions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `homes`
--
ALTER TABLE `homes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `hotels`
--
ALTER TABLE `hotels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `promo`
--
ALTER TABLE `promo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `report`
--
ALTER TABLE `report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
