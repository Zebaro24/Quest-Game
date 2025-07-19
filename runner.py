from main import bot


class Runner:
    @staticmethod
    def run():
        bot.polling()


if __name__ == '__main__':
    Runner().run()
