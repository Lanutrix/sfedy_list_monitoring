from program_options import ProgramOptions
from data_manager import DataManager
from validation_snils import ValidationSnils

class UniversityApplicationSystem:
    def __init__(self):
        self.program_options = ProgramOptions()
        self.data_manager = DataManager()

    def run(self):
        valid = ValidationSnils()
        valid.student_snils = input("Приветствую! Я бот, который поможет тебе отслеживать свою позицию в конкурсных списках на поступление в ВУЗ.\n\nДля начала, пожалуйста, введи свой СНИЛС: ")
        self.program_options.display_program_options()
        program_choice = self.program_options.get_program_choice()
        student_data = self.data_manager.get_student_data(program_choice, valid.student_snils)
        if student_data is None:
            return "СНИЛС введен неверно. Пожалуйста, попробуйте еще раз."
        else:
            message = self.data_manager.format_student_data(student_data)
            return message
