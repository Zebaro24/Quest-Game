from sample import SampleQuest


class QuestVtrach(SampleQuest):
    name = "?Втраченена година¿"
    max_count = 5
    description = ""

    stage_func_get = {0: lambda: 0}
