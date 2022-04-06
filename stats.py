import os.path


def get_best_score():
    if os.path.exists("space_save.txt"):
        with open("space_save.txt", 'r') as score:
            sc = score.read()
    else:
        with open("space_save.txt", 'w+'):
            sc = 0
    return sc if sc or sc == 0 else 0


class Stat:
    def __init__(self):
        self.score = 0
        self.best_score = get_best_score()

    def set_best_score(self):
        with open("space_save.txt", "w") as score:
            score.write(str(self.score))
            self.best_score = self.score
