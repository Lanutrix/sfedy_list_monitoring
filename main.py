from data_manager import DataManager
from bot import Bot

if __name__ == "__main__":
    url = "https://example.com/students"
    data_manager = DataManager(url)
    data_manager.parse_webpage()

    bot = Bot(data_manager)
    bot.run()
