from abc import ABC, abstractmethod
from src.my_exeption import RequestErrorException

import json
import requests


class Parser(ABC):
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class RabotaRu(Parser):
    """
    Класс для работы с API Rabota.ru
    """

    def load_vacancies(self, keyword):
        pass


class AvitoRu(Parser):
    """
    Класс для работы с API Avito.ru
    """

    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.url_area = 'https://api.hh.ru/suggests/areas'
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {"text": "",
                       #"salary": 0,
                       #"only_with_salary": "true",
                       'area': '',
                       "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def __repr__(self):
        return f"<{self.__class__}, {self.__dict__}>"

    def __len__(self):
        return len(self.__vacancies)

    @property
    def vacancies(self):
        vacancies_lst = []
        for vacancy in self.__vacancies:
            vacancies_lst.append(vacancy)
        return vacancies_lst

    def save_data_in_file(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(self.__vacancies, f, ensure_ascii=False, indent=4)

    def get_region(self, region_name):
        param = {"text": region_name}
        response = requests.get(self.url_area, param)
        #print(response.status_code)
        #print(response.json())
        area_id = response.json()['items']
        return area_id

    def load_vacancies(self, keywords):
        area_lst = self.get_region(keywords['region'])
        #print(area_lst)
        self.params['text'] = keywords['vacancy']
        if keywords['salary_from'] != 0:
            self.params['salary'] = keywords['salary_from']
        for area in area_lst:
            pages = 1
            self.params['page'] = 0
            print(area, "***", area['id'])
            self.params['area'] = area['id']
            while self.params['page'] <= pages:
                print(self.params)
                response = requests.get(self.url, self.params)
                if response.status_code == 200:
                    found = response.json()['found']
                    page = response.json()['page']
                    per_page = response.json()['per_page']
                    pages = response.json()['pages']
                    print(f'found {found}, page {page}, pages {pages}, per_page {per_page}')
                    if pages >= 20:
                        pages = 19
                    vacancies = response.json()['items']
                    self.__vacancies.extend(vacancies)
                    self.params['page'] = page + 1
                else:
                    # print(response.status_code)
                    # print(response.json())
                    raise RequestErrorException(f"**{response.status_code}, **{response.json()}")
