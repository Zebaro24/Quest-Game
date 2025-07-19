from telebot import TeleBot, types
from os import getenv
# import psycopg2

from quests.QuestHacker import QuestHacker
from quests.QuestVirne import QuestVirne
from quests.QuestVtrach import QuestVtrach
from quests.sample import SampleQuest

from time import sleep

# <Константы>
# 771348519 - Мой id
# 758462888 - Id Макса



# <Инициализация>
bot = TeleBot(getenv('TOKEN'))

# conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
# cursor = conn.cursor()

# <Глобальные переменные>
admins = [771348519]

all_people = {}
all_quests = {1: QuestHacker(all_people, bot),
              2: QuestHacker(all_people, bot),
              3: QuestVirne(all_people, bot),
              4: QuestVtrach(all_people, bot),
              5: QuestVirne(all_people, bot)}


# <Полностью перепишу, отложено на потом>
# cursor.execute("SELECT * FROM all_people;")
# for id_name in cursor.fetchall():  # Заполнение списков людьми
#     print(id_name)
#     if id_name[3] == '1':
#         quest_1[id_name[0]] = [id_name[1], id_name[2], id_name[3], id_name[4]]
#     elif id_name[3] == '2':
#         quest_2[id_name[0]] = [id_name[1], id_name[2], id_name[3], id_name[4]]
#     elif id_name[3] == '3':
#         quest_3[id_name[0]] = [id_name[1], id_name[2], id_name[3], id_name[4]]
#
#     people_off[id_name[0]] = id_name[1]

# <Основные доп функции>
# def db_run(execute):
#     cursor.execute(execute + ";")
#     if execute[:6] == "SELECT":
#         res = cursor.fetchall()
#         return res
#     else:
#         conn.commit()


# <Кнопки>
def choice_of_quest():  # Выбор квеста
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for number, quest in all_quests.items():
        item_button = types.KeyboardButton(f"{number} квест: {quest.name} ({quest.count}/{quest.max_count})")
        markup.add(item_button)
    return markup


def del_mark():
    return types.ReplyKeyboardRemove()


def quest_markup(quest):
    if all_quests[quest].max_count <= all_quests[quest].count:
        return None
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton("Приєднатися", callback_data=f"connect {quest}")
    markup.add(item)
    return markup


def update_mar():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item_1 = types.InlineKeyboardButton("Оновити", callback_data=f"upd")
    item_2 = types.InlineKeyboardButton("Залишити команду", callback_data=f"exit")
    markup.add(item_1)
    markup.add(item_2)
    return markup


def confirm_mar():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton("Підтвердити", callback_data=f"confirm")
    markup.add(item)
    return markup


# <Админ функции>
@bot.message_handler(commands=['delete'])
def delete(message):
    all_people.clear()
    for i in all_quests.values():
        i.quest_people.clear()
    bot.send_message(message.chat.id, "Все списки очищены!")


@bot.message_handler(commands=['list'])
def list_def(message):
    print()
    print("Все люди:")
    for i, j in all_people.items():
        print(f"{i}: {j}")
    print()
    print("Участники квестов:")
    for i, j in all_quests.items():
        print(f"{i}: {j.name}")
        for k, l in j.quest_people.items():
            print(f"{k}: {l}")
        print()
    bot.send_message(message.chat.id, "Список участников выведен.")


# <Основные функции>
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    if message.chat.type != "private":
        bot.send_message(message.chat.id, "Квести працюють тільки в особистих!")
        return

    if message.chat.id in all_people:
        bot.send_message(message.chat.id, "Я вже с тобою поздоровкався!")
        return

    ms1 = bot.send_sticker(message.chat.id,
                           'CAACAgQAAxkBAAEQHCBj37DK14i4ZwnXP8i_YlnQIV85mwACPAkAAi_DZAwOXx9tZwUicS4E')  # noqa
    sleep(0.3)
    bot.delete_message(message.chat.id, ms1.message_id)
    ms2 = bot.send_message(message.chat.id, 'Ой, не сюди')
    sleep(1)
    bot.delete_message(message.chat.id, ms2.message_id)

    bot.send_sticker(message.chat.id,
                     'CAACAgQAAxkBAAEJWlthnOPA3gktGeNBQknslb3-X56YYQACJwkAAi_DZAyFnCEJZ4ObqiIE')  # noqa
    bot.send_message(message.chat.id, 'Вітаю мій любий друже!')
    sleep(0.5)
    bot.send_message(message.chat.id, 'Обери квест та команду до якої хочеш приєднатися:',
                     reply_markup=choice_of_quest())


@bot.message_handler(content_types=['text'])
def main_message(message: types.Message):
    if message.chat.type != "private":
        bot.send_message(message.chat.id, "Бот поки не працює у групових чатах або каналах!")
        return

    if message.chat.id not in all_people:
        if message.text[2:7] == "квест":
            if not message.text[:1].isdigit() or int(message.text[:1]) not in all_quests:
                bot.send_message(message.chat.id, "Такого квеста немає!")
                return

            number_quest = int(message.text[0])
            text_list_players = all_quests[number_quest].text_list_players()
            bot.send_message(message.chat.id, text_list_players, "HTML", reply_markup=quest_markup(number_quest))
            # all_quests[int(message.text[:1])].add_people(message.chat.id, message.chat.first_name)
        else:
            bot.send_message(message.chat.id, "Я не розумію вас!", reply_markup=choice_of_quest())
        return

    all_people[message.chat.id]["class"].get_text(message.text, message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if not call.message:
        return

    if call.data[:7] == "connect":
        if call.message.chat.id in all_people:
            bot.edit_message_text("Ви вже приєдналися до іншої команди!", call.message.chat.id, call.message.message_id)
            return

        number_quest = int(call.data[8])
        quest_class: SampleQuest = all_quests[number_quest]
        if quest_class.count >= quest_class.max_count:
            bot.send_message(call.message.chat.id, "Команда вже зібрала максимальну кількість гравців.")
            text_list_players = quest_class.text_list_players()
            bot.edit_message_text(text_list_players, call.message.chat.id, call.message.message_id, parse_mode='HTML')
            return

        quest_class.add_people(call.message.chat.id, call.message.chat.first_name)
        quest_class.send_text_all(f"До вас приєднався гравець: {call.message.chat.first_name}", call.message.chat.id)
        text_list_players = quest_class.text_list_players()
        bot.edit_message_text(text_list_players, call.message.chat.id, call.message.message_id,
                              reply_markup=update_mar(), parse_mode='HTML')
        bot.pin_chat_message(call.message.chat.id, call.message.message_id, True)
        bot.send_message(call.message.chat.id, "Ви були підключені до чату команди!", reply_markup=del_mark())

        if quest_class.max_count == quest_class.count:
            for id_people in quest_class.quest_people:
                bot.send_message(id_people, "Команда зібрана, підтвердьте участь.", reply_markup=confirm_mar())

    elif call.data == 'upd':
        if call.message.chat.id not in all_people:
            bot.edit_message_text("Ви не приєднані до жодної команди!", call.message.chat.id, call.message.message_id)
            bot.unpin_chat_message(call.message.chat.id, call.message.message_id)
            return

        bot.edit_message_text("⏳ Секунду...", call.message.chat.id, call.message.message_id)
        sleep(0.4)
        text_list_players = all_people[call.message.chat.id]["class"].text_list_players()
        bot.edit_message_text(text_list_players, call.message.chat.id, call.message.message_id,
                              reply_markup=update_mar(), parse_mode='HTML')

    elif call.data == 'exit':
        if call.message.chat.id not in all_people:
            bot.edit_message_text("Ви не приєднані до жодної команди!", call.message.chat.id, call.message.message_id)
            bot.unpin_chat_message(call.message.chat.id, call.message.message_id)
            return

        if all_people[call.message.chat.id]["class"].stage_num != 0:
            text_list_players = all_people[call.message.chat.id]["class"].text_list_players()
            bot.edit_message_text(text_list_players, call.message.chat.id, call.message.message_id,
                                  parse_mode='HTML')
            bot.send_message(call.message.chat.id, "Під час гри не можна покинути команду!")
            return

        bot.edit_message_text("Вы були від'єднані від команди!", call.message.chat.id, call.message.message_id)
        bot.unpin_chat_message(call.message.chat.id, call.message.message_id)
        quest_class: SampleQuest = all_people[call.message.chat.id]["class"]
        quest_class.del_people(call.message.chat.id)
        quest_class.send_text_all(f"Команду покинув гравець: {call.message.chat.first_name}")

        bot.send_message(call.message.chat.id, "Обери квест та команду до якої хочеш приєднатися:",
                         reply_markup=choice_of_quest())

    elif call.data == 'confirm':
        if call.message.chat.id not in all_people:
            bot.edit_message_text("Ви не приєднані до жодної команди!", call.message.chat.id, call.message.message_id)
            return

        quest_class: SampleQuest = all_people[call.message.chat.id]["class"]
        quest_class.confirm(call.message.chat.id, call.message.message_id)


if __name__ == '__main__':
    print("<Бот запущен>")
    bot.polling(True)
