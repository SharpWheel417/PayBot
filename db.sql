-- Adminer 4.8.1 PostgreSQL 16.2 (Debian 16.2-1.pgdg120+2) dump

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

Продолжить?');

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
(4,	'Summer_Death',	'dollar',	'22.0',	NULL,	NULL,	'2024-04-26',	'query',	'1194700554',	'0a4a46b2-de55-4496-aad3-f4095664ab91');

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
(3,	'Summer_Death',	'1194700554',	NULL,	'Gleb Petrov');

-- 2024-04-26 10:50:15.201183+00
