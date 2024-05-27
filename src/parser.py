from abc import ABC, abstractmethod
from src.my_exeption import RequestErrorException

import requests


class Parser(ABC):
    """
    Абстрактный класс для работы с API различных сайтов по поиску вакансий
    """

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
    Класс для работы с API HeadHunter:
        Атрибуты:
            HH.id: int          - id запроса, классовый атрибут;
            id: str             - id запроса, строковое представление формата - 'queryHH_' + str(HH.id);
            url_area: str       - url для запроса в API - места нахождение работодателя;
            url = str           - url для запроса в API;
            params: dict        - параметры для запроса в API
                    {"text": "",        --ключевые слова для поиска
                    "area": "",         --id места нахождение работодателя
                     "period": 7,       --временной период от даты публикации до даты поиска - 7 дней
                    "page": 0,          --номер страницы
                    "per_page": 100};   --количество вакансий на странице
            __vacancies: list   - список вакансий, полученных в ответах на запросы;
        Методы:
            get_region_lst(self, region_name): Метод получает список мест нахождения работодателя,
                                            найденных по ключевому слову через запрос к API

            load_vacancies(self, keywords): Метод получает список вакансий,
                                            найденных по ключевым словам через запрос к API;

    """
    id = 0
    id: str
    url_area: str
    url = str
    params: dict
    __vacancies: list

    def __init__(self):
        HH.id += 1
        self.id = 'queryHH_' + str(HH.id)
        self.url_area = 'https://api.hh.ru/suggests/areas'
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {"text": "",
                       "area": "",
                       "period": 7,
                       "page": 0, "per_page": 100}
        self.__vacancies = []

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

    def get_region_lst(self, region_name):
        """
        Метод получает список мест нахождения работодателя, найденных по ключевому слову через запрос к API
        """
        param = {"text": region_name}
        response = requests.get(self.url_area, param)
        area_lst = response.json()['items']
        return area_lst

    def load_vacancies(self, keywords):
        """
        Метод получает список вакансий, найденных по ключевым словам через запрос к API
        """
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
