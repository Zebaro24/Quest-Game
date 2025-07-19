from sample import SampleQuest


class QuestHacker(SampleQuest):
    name = "}Х@кер-ст@йл{"
    max_count = 2
    description = "---"

    stage_func_get = {0: lambda: 0}

    # def func_start(self):
    #     pass

    def gg(self):
        self.send_text_all("Проверка")
