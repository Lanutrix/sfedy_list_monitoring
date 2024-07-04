import requests
from bs4 import BeautifulSoup

class DataManager:
    def __init__(self,url):
        self.url = url
        self.student_data = {}
        self.total_applications = None
        self.passing_scores = {}
        self.parse_webpage()
    
    def parse_webpage(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Парсинг данных о студентах
        student_rows = soup.find_all('tr', class_='student-row')
        for row in student_rows:
            cells = row.find_all('td')
            snils = self.extract_snils(cells)
            if snils:
                position = cells[cells.index(snils) - 1].text.strip()
                score_cells = cells[cells.index(snils) + 6:cells.index(snils) + 24]
                score = ''.join([cell.text.strip() for cell in score_cells])
                self.student_data[self.format_snils(snils.text.strip())] = Student(self.format_snils(snils.text.strip()), position, score)        
        
        # Извлечение данных об общем количестве заявлений
        total_applications_element = soup.find('div', class_='total-applications')
        self.total_applications = int(total_applications_element.text.strip())

        # Извлечение данных о проходных баллах прошлых лет
        #
        #
    
    def extract_snils(self, cells):
        snils_pattern = r'\d{3}-\d{3}-\d{3}\s\d{2}'
        for cell in cells:
            text = cell.text.strip()
            if re.search(snils_pattern,text):
                return cell
            
    def format_snils(self, snils):
        return snils
    
    def get_student_data(self, snils):
        formatted_snils = self.format_snils(snils)
        if formatted_snils in self.student_data:
            return self.student_data[formatted_snils]
        else:
            return None
        
    def get_total_applications(self):
        return self.total_applications
            
                