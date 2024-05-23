from abc import ABC, abstractmethod
from src.my_exeption import RequestErrorException

import requests
import json


class Parser(ABC):
    """
    Абстрактный класс для работы с API различных сайтов по поиску вакансий
    """

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
    id = 0

    def __init__(self, file_worker):
        HH.id += 1
        self.id = 'queryHH_' + str(HH.id)
        self.url_area = 'https://api.hh.ru/suggests/areas'
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {"text": "",
                       'area': '',
                       'period': 7,
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

    def save_list_in_file(self):
        with open(self.file_worker, 'w', encoding='utf-8') as f:
            json.dump(self.vacancies, f, ensure_ascii=False, indent=4)

    def get_region_lst(self, region_name):
        param = {"text": region_name}
        response = requests.get(self.url_area, param)
        area_lst = response.json()['items']
        return area_lst

    def load_vacancies(self, keywords):
        found = 'Что-то пошло не так!'
        self.params['text'] = keywords['vacancy']
        if keywords['salary'] != 0:
            self.params['salary'] = keywords['salary']
        pages = 1
        self.params['area'] = keywords['region']
        self.params['page'] = 0
        while self.params['page'] < pages:
            response = requests.get(self.url, self.params)
            if response.status_code == 200:
                found = response.json()['found']
                page = response.json()['page']
                per_page = response.json()['per_page']
                pages = response.json()['pages']
                if pages >= 20:
                    pages = 20
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.params['page'] = page + 1
            else:
                raise RequestErrorException(f"**{response.status_code}, **{response.json()}")
        return f"Найдено вакансий по запросу: {found}"
