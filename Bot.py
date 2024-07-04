class Bot:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def run(self):
        snils = input("Введите СНИЛС студента: ")
        student_data = self.data_manager.get_student_data(snils)
        if student_data:
            print(student_data)
        else:
            print("Студент не найден.")
