import os.path


class Stat:
    def __init__(self):
        self.score = 0
        self.best_score = self.get_best_score()


    def get_best_score(self):
        if os.path.exists("space_save.txt"):
            with open("space_save.txt", 'r') as score:
                sc = score.read()
        else:
            with open("space_save.txt", 'w+') as score:
                score.write(str(self.score))
                sc = score.read()
        return sc
    

    def set_best_score(self):
        with open("space_save.txt", "w") as score:
            score.write(str(self.score))
            self.best_score = self.score


