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

        student_rows = soup.find_all('tr', class_='student-row')
        for row in student_rows:
            cells = row.find_all('td')
            snils = self.extract_snils(cells)
            if snils:
                position = cells[cells.index(snils) - 1].text.strip()
                score = ''.join([cell.text.strip() for cell in cells[cells.index(snils) + 1:cells.index(snils) + 18]])
                self.student_data[snils] = {
                    'position': position,
                    'score': score
                }
                