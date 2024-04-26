-- Adminer 4.8.1 PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1) dump

\connect "paybot";

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
(3,	'info',	'Регион карты — 🇰🇿 Казахстан
Ограничения по оплате:
1) Убедитесь, что в аккаунте/магазине выставлен корректный регион.
2) Нельзя привязать карту в аккаунт PayPal

В какой валюте будет списание?
Пожалуйста, убедитесь, что в сервисе выполняется покупка именно в указанной вами валюте. '),
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

После перевода пришлите квитанцию об оплате.');

DROP TABLE IF EXISTS "orders";
DROP SEQUENCE IF EXISTS order_id_seq;
CREATE SEQUENCE order_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."orders" (
    "id" integer DEFAULT nextval('order_id_seq') NOT NULL,
    "username" text NOT NULL,
    "money_type" text NOT NULL,
    "sum" text NOT NULL,
    "email" text,
    "link" text,
    "date_order" date NOT NULL,
    "state" text NOT NULL,
    "chat_id" text NOT NULL,
    "order_code" text NOT NULL,
    CONSTRAINT "order_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "orders" ("id", "username", "money_type", "sum", "email", "link", "date_order", "state", "chat_id", "order_code") VALUES
(4,	'Summer_Death',	'dollar',	'22.0',	NULL,	NULL,	'2024-04-26',	'yes',	'1194700554',	'0a4a46b2-de55-4496-aad3-f4095664ab91'),
(1,	'Summer_Death',	'dollar',	'22.0',	NULL,	NULL,	'2024-04-26',	'yes',	'1194700554',	'69007de7-3f3d-48e0-af3c-614cb1eadc47'),
(2,	'Summer_Death',	'dollar',	'22.0',	NULL,	NULL,	'2024-04-26',	'yes',	'1194700554',	'00e86a7a-50e9-4a0a-a021-c20dc3670f45'),
(3,	'None',	'dollar',	'22.0',	NULL,	NULL,	'2024-04-26',	'yes',	'6908096537',	'7706fe66-4027-4e33-8b52-38ff4d208e41'),
(5,	'None',	'dollar',	'33.0',	NULL,	NULL,	'2024-04-26',	'yes',	'6908096537',	'407b4062-6f8e-402c-9e48-a040a9f6b16a'),
(6,	'None',	'dollar',	'11.0',	NULL,	NULL,	'2024-04-26',	'yes',	'6908096537',	'2a544896-e2b2-48ac-8d46-850431cb9740');

DROP TABLE IF EXISTS "users";
DROP SEQUENCE IF EXISTS users_id_seq;
CREATE SEQUENCE users_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."users" (
    "id" integer DEFAULT nextval('users_id_seq') NOT NULL,
    "username" text NOT NULL,
    "chat_id" text NOT NULL,
    "state" text,
    "full_name" text,
    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "users" ("id", "username", "chat_id", "state", "full_name") VALUES
(3,	'Summer_Death',	'1194700554',	NULL,	'Gleb Petrov'),
(4,	'--Xd Out',	'6908096537',	NULL,	'Xd Out');

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
(1,	'course_usd                                                                                          ',	'91.2'),
(2,	'course_euro                                                                                         ',	'105.5'),
(3,	'phone                                                                                               ',	'+7-913-320-29-81'),
(4,	'trade_type                                                                                          ',	'Сбербанк');

-- 2024-04-26 17:20:26.258161+00
