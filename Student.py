class Student:
    def __init__(self, snils, position, score, program):
        self.snils = snils
        self.position = position
        self.score = score
        self.program = program

    def __str__(self):
        return f"СНИЛС: {self.snils}, Направление: {self.program}, Позиция: {self.position}, Баллы: {self.score}"
