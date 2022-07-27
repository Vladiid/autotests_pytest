from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com.ua/search?q=avatar&sxsrf=ALiCzsbEZaoekWFm1XMMoUhqZNu4lAi7"
                                "kw:1658948568541&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvp4OB4Zn5AhWHvosKHZxkBAs"
                                "Q_AUoAXoECAIQAw&biw=2327&bih=1172&dpr=1.1#imgrc=sh1dyb_R5yG2JM"):
        self.result['avatar'] = avatar

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self

    def build(self):
        return self.result


z = Player().build()
print(z)