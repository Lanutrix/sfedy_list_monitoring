from bs4 import BeautifulSoup
import requests

from student import Student

class DataManager:
    def __init__(self, urls):
        self.urls = urls
        self.student_data = {}

    def format_snils(self, snils):
        return ''.join(snils.split())

    def extract_snils(self, cells):
        for cell in cells:
            if cell.text.strip().isdigit() and len(cell.text.strip()) == 11:
                return cell
        return None

    def parse_webpage(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        student_rows = soup.find_all('tr')[1:]

        for row in student_rows:
            cells = row.find_all('td')
            snils = self.extract_snils(cells)
            if snils:
                position = int(cells[cells.index(snils) - 1].text.strip()) # Получаем позицию по индексу -1 относительно класса td со снилсом
                score_cells = cells[cells.index(snils) + 6:cells.index(snils) + 24]
                score = ''.join([cell.text.strip() for cell in score_cells])
                program = self.get_program_from_url(url)
                self.student_data[self.format_snils(snils.text.strip())] = Student(self.format_snils(snils.text.strip()), position, score, program)

    def get_program_from_url(self, url):
        if f"{https://sfedu.ru/abitur/list/09.03.04_%D0%9A%D0%A2_%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F.%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%B8%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F_%D0%9E%D0%9E_%D0%93%D0%91}" in url:
            return "Программная инженерия"
        elif f"{https://sfedu.ru/abitur/list/09.03.02_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B%20%D0%B8%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8.%20%D0%9F%D0%B5%D1%80%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8_%D0%9E%D0%9E_%D0%93%D0%91}" in url:
            return "Информационные системы и технологии"
        elif f"{https://sfedu.ru/abitur/list/09.03.01_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B0_%D0%9E%D0%9E_%D0%93%D0%91}" in url:
            return "Информатика и вычислительная техника"
        else:
            return "Неизвестно"

    def get_student_data(self, snils, program):
        formatted_snils = self.format_snils(snils)
        if formatted_snils in self.student_data:
            if self.student_data[formatted_snils].program == program:
                return self.student_data[formatted_snils]
        return None

    def get_total_applicants(self, program):
        count = 0
        for student in self.student_data.values():
            if student.program == program:
                count += 1
        return count

            
                