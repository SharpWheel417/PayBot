-- Adminer 4.8.1 PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1) dump

DROP TABLE IF EXISTS "data";
DROP SEQUENCE IF EXISTS data_id_seq;
CREATE SEQUENCE data_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."data" (
    "id" integer DEFAULT nextval('data_id_seq') NOT NULL,
    "type" text NOT NULL,
    "text" text NOT NULL,
    CONSTRAINT "data_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "data" ("id", "type", "text") VALUES
(2,	'start_two',	'Мы проводим оплаты ежедневно с 8:00 МСК по 20:00 МСК. Если вы начали работу с ботом до конца рабочего дня, но не успели воспользоваться его услугами, то бот продолжает для вас работу. Если бот не получает сообщений от вас в течении 10 минут, то он закрывает заказ. '),
(1,	'start',	'Здравствуйте!  Данный бот создан @Mar1osh.

Если у вас возникли какие-либо вопросы, ошибки в работе бота или вам нужна дополнительная услуга, то пишите мне в личные сообщения с тегом

#Оплата_через_бота.'),
(4,	'to_pay',	'К оплате: {summ}₽ с учетом комисси банка и бота.

Если совершить оплату сервиса/услуги не удастся, мы совершим возврат средств в полном обьеме.

Продолжить?'),
(8,	'to_pay_pay',	'К оплате {sum}₽ по номеру телефона {number} в {trade_type} (!) с комментарием: Оплата зарубежных сервисов.
Стоимость в рублях фиксируется на 10 минут. Если оплата от вас не поступит, то бот закроет заказ. Пожалуйста, перед переводом заранее подготовьте окно на сайте, в котором хотите совершить покупку для ввода реквизитов.

После перевода пришлите квитанцию об оплате.'),
(5,	'dollar',	'Введите нужную вам сумму в долларах'),
(6,	'euro',	'Введите нужную сумму в евро'),
(7,	'order_request',	'Поступил новый заказ!

ID заказа: {ids}
От пользователя: {username}:
На сумму: {sum}
'),
(10,	'no',	'Ваш заказ отменен!
'),
(9,	'yes',	'К оплате {sum}₽ по номеру телефона {phone} в {trade_type} (!) с комментарием: Оплата зарубежных сервисов.
Стоимость в рублях фиксируется на 10 минут. Если оплата от вас не поступит, то бот закроет заказ. Пожалуйста, перед переводом заранее подготовьте окно на сайте, в котором хотите совершить покупку для ввода реквизитов.

После перевода пришлите квитанцию об оплате.'),
(11,	'have_order',	'У вас уже имеется заказ от {date}

ID заказа: {ids}'),
(13,	'user_send_recipt',	'Квитанция отправлена оператору'),
(14,	'came_recipt',	'Пришла квитанция от юзера {username}
ID заказа: {ids}
На сумму: {sum}'),
(16,	'came_email_url',	'Пришли ссылка и емайл

email: {email}
url: {url}

ID заказа: {ids}
От пользователя @{username}
Сумма: {sum}
От: {date}'),
(15,	'u_a_apply_recipt',	'Оплата принята!

Пожалуйста, пришлите одним сообщением  вашу электронную почту и скопированную  ссылку из браузера на страницу с формой оплаты (например, как на скриншоте). Отправьте их в этот чат, и мы проведем оплату в течении нескольких минут. '),
(17,	'u_a_cancle_recipt',	'Квитанция не принята'),
(3,	'info',	'Регион карты — 🇰🇿 Казахстан
Ограничения по оплате:
1) Убедитесь, что в аккаунте/магазине выставлен корректный регион.
2) Нельзя привязать карту в аккаунт PayPal

Бот оплачивает сервисы с валютой $.
Пожалуйста, убедитесь, что в сервисе выполняется покупка именно в указанной вами валюте. '),
(12,	'await_admin',	'Ожидайте, пока оператор обрабатывает ваш заказ'),
(19,	'user_came_email',	'Ссылка и почта получены

Подождите, пока оператор обрабатывает квитанцию');

DROP TABLE IF EXISTS "orders";
DROP SEQUENCE IF EXISTS order_id_seq;
CREATE SEQUENCE order_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."orders" (
    "id" integer DEFAULT nextval('order_id_seq') NOT NULL,
    "username" text NOT NULL,
    "sum" text NOT NULL,
    "email" text,
    "url" text,
    "date" timestamp NOT NULL,
    "state" text NOT NULL,
    "chat_id" text NOT NULL,
    "ids" text NOT NULL,
    "course" text,
    "marje" text,
    "profit" text,
    "status" text,
    "timechk" text,
    CONSTRAINT "order_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "orders" ("id", "username", "sum", "email", "url", "date", "state", "chat_id", "ids", "course", "marje", "profit", "status", "timechk") VALUES
(1,	'None',	'2436.0',	NULL,	NULL,	'2024-05-14 16:31:18.350337',	'cancle',	'6908096537',	'93b2a496-a7f0-4003-844a-3c682fb73ffe',	'145.0',	'1.12',	'261.0',	'cancle',	'cancle'),
(2,	'None',	'5684.0',	'xd@gmail.com',	'https://vk.com',	'2024-05-14 16:31:51.765646',	'order_complete',	'6908096537',	'31c155e3-a9b1-4dd8-95d2-318d46af5352',	'145.0',	'1.12',	'609.0',	'complete',	'complete'),
(3,	'None',	'4872.0',	'gk@gmail.com',	'https://youtube.com',	'2024-05-14 16:33:19.64134',	'order_complete',	'6908096537',	'a7ba500c-c36a-458d-b0ee-c4ed0126c993',	'145.0',	'1.12',	'522.0',	'complete',	'complete');

DROP TABLE IF EXISTS "users";
DROP SEQUENCE IF EXISTS users_id_seq;
CREATE SEQUENCE users_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."users" (
    "id" integer DEFAULT nextval('users_id_seq') NOT NULL,
    "username" text NOT NULL,
    "chat_id" text NOT NULL,
    "state" text,
    "full_name" text,
    "date" timestamp,
    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "users" ("id", "username", "chat_id", "state", "full_name", "date") VALUES
(2,	'chat',	'-4181748266',	'',	'Chat Logging',	NULL),
(1,	'Summer_Death',	'1194700554',	'await_recipt',	'Gleb Petrov',	'2024-05-14 14:31:21.068361'),
(3,	'--Xd Out',	'6908096537',	'order_complete',	'Xd Out',	'2024-05-14 14:49:25.736372');

DROP TABLE IF EXISTS "vars";
DROP SEQUENCE IF EXISTS vars_id_seq;
CREATE SEQUENCE vars_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."vars" (
    "id" integer DEFAULT nextval('vars_id_seq') NOT NULL,
    "type" character(100) NOT NULL,
    "text" text NOT NULL,
    CONSTRAINT "vars_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "vars" ("id", "type", "text") VALUES
(3,	'phone                                                                                               ',	'42332'),
(4,	'trade_type                                                                                          ',	'3r42rewfd'),
(5,	'marje                                                                                               ',	'1.12'),
(1,	'course_usd                                                                                          ',	'145.0');

-- 2024-05-14 09:36:13.55009+00
