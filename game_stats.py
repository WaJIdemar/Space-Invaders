import json


class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        with open("high_score.txt") as file:
            self.high_score = json.load(file)
        self.old_high_score = self.high_score

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def new_high_score(self):
        if self.old_high_score < self.high_score:
            with open("high_score.txt", 'w') as file:
                json.dump(self.high_score, file)
