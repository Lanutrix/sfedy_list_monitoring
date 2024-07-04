from DataManager import DataManager

class Bot:
    def __init__(self, DataManager):
        self.DataManager = DataManager

    def display_program_options(self):
        print("Доступные направления:")
        print("1. Программная инженерия")
        print("2. Информационные системы и технологии")
        print("3. Информатика и вычислительная техника")

    def get_program_choice(self):
        while True:
            choice = input("Введите номер направления: ")
            if choice == "1":
                return "Программная инженерия"
            elif choice == "2":
                return "Информационные системы и технологии"
            elif choice == "3":
                return "Информатика и вычислительная техника"
            else:
                print("Некорректный выбор. Попробуйте еще раз.")

    def display_menu(self):
        print("\nМеню:")
        print("1. Посмотреть себя в списке")
        print("2. Узнать общее количество подавших заявления")

    def get_menu_choice(self):
        while True:
            choice = input("Введите номер пункта меню: ")
            if choice == "1":
                return 1
            elif choice == "2":
                return 2
            else:
                print("Некорректный выбор. Попробуйте еще раз.")

    def run(self):
        snils = input("Введите СНИЛС студента: ")
        formatted_snils = self.DataManager.format_snils(snils)
        if formatted_snils:
            self.display_program_options()
            program = self.get_program_choice()
            self.display_menu()
            menu_choice = self.get_menu_choice()

            if menu_choice == 1:
                student_data = self.DataManager.get_student_data(formatted_snils, program)
                if student_data:
                    print(student_data)
                else:
                    print("Студент не найден или не зачислен на выбранное направление.")
            elif menu_choice == 2:
                total_applicants = self.DataManager.get_total_applicants(program)
                print(f"Общее количество подавших заявления на {program}: {total_applicants}")
        else:
            print("Некорректный формат СНИЛС.")