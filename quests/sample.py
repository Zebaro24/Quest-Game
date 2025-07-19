from telebot import TeleBot


# from typing import List


class SampleQuest:
    name = "Немає назви"
    max_count = 5
    description = "А де опис, він не написаний"
    stage_num = 0
    stage_func_get = {0: lambda: 0}

    def __init__(self, all_people_dict: dict, bot: TeleBot):
        self.bot = bot
        self.quest_people = {}
        self.all_people_dict = all_people_dict
        self.count = 0
        self.confirm_people = []

    def add_people(self, id_people, name):
        self.quest_people[id_people] = {"name": name, "class": self}
        self.all_people_dict[id_people] = self.quest_people[id_people]
        self.count += 1

    def del_people(self, id_people):
        self.confirm_people.clear()
        del self.quest_people[id_people]
        del self.all_people_dict[id_people]
        self.count -= 1

    def text_list_players(self):
        text = f"<b>{self.name}</b>\n"
        text += "Опис квесту:\n"
        text += f"{self.description}\n"
        text += "В даний момент приєднані:\n"
        number = 1
        for id_people, info in self.quest_people.items():
            text += f'{number}) <a href="tg://user?id={id_people}">{info["name"]}</a>\n'
            number += 1
        for j in range(self.max_count - len(self.quest_people)):
            text += f"{number}) ---\n"
            number += 1
        return text

    def send_text_all(self, text: str, no_people_id=None):
        for id_people in self.quest_people:
            if id_people != no_people_id:
                self.bot.send_message(id_people, text)

    def get_text(self, text: str, id_people):
        self.send_text_all(f"{self.quest_people[id_people]['name']}: {text}", id_people)
        self.stage_func_get[self.stage_num]()
        pass

    def confirm(self, id_people, message_id):
        if self.max_count > self.count:
            self.confirm_people.clear()
            self.bot.edit_message_text("Команда ще не зібрана!", id_people, message_id)
            return

        if id_people in self.confirm_people:
            self.bot.edit_message_text("Ви вже підтвердили свою участь", id_people, message_id)
            return

        self.confirm_people.append(id_people)
        self.bot.edit_message_text("Ви підтвердили свою участь", id_people, message_id)
        self.send_text_all(f"Гравець {self.quest_people[id_people]['name']} підтвердив участь!", id_people)

        if self.count == len(self.confirm_people):
            self.send_text_all("Всі приєдналися, гра почалася!")
            self.stage_num = 1
            self.func_start()  # Или поменять на функцию старта
            return

    def func_start(self):
        self.send_text_all("Функція початку квесту ще не написана!")
