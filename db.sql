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

После перевода пришлите квитанцию об оплате.'),
(11,	'have_order',	'У вас уже имеется заказ от {date}

ID заказа: {ids}'),
(12,	'user_send_recipt',	'Ваша квитанция {file_name}
Отправлена оператору'),
(13,	'u_a_apply_recipt',	'Оплата принята!

Пожалуйста, пришлите одним сообщением  вашу электронную почту и скопированную  ссылку из браузера на страницу с формой оплаты (например, как на скриншоте). Отправьте их в этот чат, и мы проведем оплату в течении нескольких минут.'),
(14,	'came_recipt',	'От пользователя {username}
По заказу {ids}
На сумму {sum}
Пришла квитанция:'),
(16,	'user_came_email',	'Спасибо!
Ссылка отправлена операотру, ожидайте ответа!'),
(15,	'came_email_url',	'От пользоватлея: {username}
ID заказа: {ids}
Сумма: {sum}
От: {date}

Пришла почта и ссылку на оплату:
email: `{email}`
Ссылка: {url}'),
(17,	'u_a_cancle_recipt',	'Извините, ваша квитанция не действительна');

DROP TABLE IF EXISTS "orders";
DROP SEQUENCE IF EXISTS order_id_seq;
CREATE SEQUENCE order_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."orders" (
    "id" integer DEFAULT nextval('order_id_seq') NOT NULL,
    "username" text NOT NULL,
    "sum" text NOT NULL,
    "email" text,
    "url" text,
    "date" date NOT NULL,
    "state" text NOT NULL,
    "chat_id" text NOT NULL,
    "ids" text NOT NULL,
    "status" character(10) NOT NULL,
    CONSTRAINT "order_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "orders" ("id", "username", "sum", "email", "url", "date", "state", "chat_id", "ids", "status") VALUES
(5,	'None',	'73.7',	'Xd@gmail.com',	'https://vk.com/pay/',	'2024-04-29',	'receipt',	'6908096537',	'dd60b5e3-3317-4991-a862-a166f1dd9f54',	'active    '),
(4,	'None',	'29.700000000000003',	'Xd@gmail.com',	'https://vk.com/pay/',	'2024-04-29',	'order_complete',	'6908096537',	'335669ed-bd45-4b49-8c06-043eee9f726d',	'complete  '),
(1,	'None',	'33.0',	'Xd@gmail.com',	'https://vk.com/pay/',	'2024-04-29',	'receipt',	'6908096537',	'ba6a736a-06f9-49bc-97e2-a76bd20d565e',	'complete  '),
(2,	'None',	'22.0',	'Xd@gmail.com',	'https://vk.com/pay/',	'2024-04-29',	'receipt',	'6908096537',	'3cbe2ac3-c68c-4a2c-8912-5db8655da773',	'complete  '),
(3,	'None',	'27.500000000000004',	'Xd@gmail.com',	'https://vk.com/pay/',	'2024-04-29',	'receipt',	'6908096537',	'29400a0b-3d17-4127-a190-ba14006ac736',	'cancle    ');

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
(3,	'Summer_Death',	'1194700554',	'email&url',	'Gleb Petrov'),
(4,	'--Xd Out',	'6908096537',	'order_complete',	'Xd Out');

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

-- 2024-04-29 15:47:42.60764+00
