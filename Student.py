class Student:
    def __init__(self, snils, position, score):
        self.snils = snils
        self.position = position
        self.score = score

    def __str__(self):
        return f"СНИЛС: {self.snils}, Позиция: {self.position}, Баллы: {self.score}"