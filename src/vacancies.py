
class Vacancy:
    """
    Класс для работы с вакансиями
    """
    query_id: str
    name: str
    employer: dict
    area: dict
    __salary: dict
    snippet: dict
    schedule: dict
    professional_roles: dict
    experience: dict
    date: str
    type: dict
    salary_print: str
    id = 0
    vacancy_lists = {'without_salary': [], 'with_salary_to': {'до вычета налогов': {}, 'на руки': {}},
                     'with_salary_from': {'до вычета налогов': {}, 'на руки': {}}}

    def __init__(self, query_id, name, employer, area, salary, snippet, schedule, professional_roles, experience,
                 date, type_vac):
        Vacancy.id += 1
        self.id = query_id + '_' + str(Vacancy.id)
        self.name = name
        self.employer = employer
        self.area = area
        self.__salary = salary
        self.snippet = snippet
        self.schedule = schedule
        self.professional_roles = professional_roles
        self.experience = experience
        self.date = date
        self.type = type_vac
        self.salary_print = ''
        Vacancy.add_vacancy_to_sorted_list(self)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_value):
        self.__salary = salary_value

    def get_vacancy_list(self):
        """
        Метод преобразует отсортированный по зарплате словарь в общий список всех вакансий
        """

        list_ = []
        for currency in self.vacancy_lists['with_salary_to']['на руки']:
            for item in self.vacancy_lists['with_salary_to']['на руки'][currency]:
                list_.append(item)
        for currency in self.vacancy_lists['with_salary_to']['до вычета налогов']:
            for item in self.vacancy_lists['with_salary_to']['до вычета налогов'][currency]:
                list_.append(item)
        for currency in self.vacancy_lists['with_salary_from']['на руки']:
            for item in self.vacancy_lists['with_salary_from']['на руки'][currency]:
                list_.append(item)
        for currency in self.vacancy_lists['with_salary_from']['до вычета налогов']:
            for item in self.vacancy_lists['with_salary_from']['до вычета налогов'][currency]:
                list_.append(item)
        for item in self.vacancy_lists['without_salary']:
            list_.append(item)
        return list_

    @classmethod
    def add_vacancy_to_sorted_list(cls, self):
        """
        Метод позволяет добавить вакансию в отсортированный по зарплате словарь
        """

        if not self.__salary:
            cls.vacancy_lists['without_salary'].append(self)
            self.salary_print = "Зарплата не определена"
        else:
            if self.__salary["gross"]:
                gross = "до вычета налогов"
            else:
                gross = "на руки"
            if not self.__salary['from']:
                if self.__salary['to']:
                    self.salary_print = f'Зарплата до: {self.__salary['to']}, {self.__salary['currency']}, {gross}'
                    cls.vacancy_lists['with_salary_to'][gross].setdefault(self.__salary['currency'], [])
                    cls.vacancy_lists['with_salary_to'][gross][self.__salary['currency']].append(self)
                    cls.vacancy_lists['with_salary_to'][gross][self.__salary['currency']].sort(reverse=True)
            elif not self.__salary['to']:
                self.salary_print = f'Зарплата от: {self.__salary['from']}, {self.__salary['currency']}, {gross}'
                cls.vacancy_lists['with_salary_from'][gross].setdefault(self.__salary['currency'], [])
                cls.vacancy_lists['with_salary_from'][gross][self.__salary['currency']].append(self)
                cls.vacancy_lists['with_salary_from'][gross][self.__salary['currency']].sort(reverse=True)

            else:
                self.salary_print = (f'Зарплата от: {self.__salary['from']}  до: {self.__salary['to']}, '
                                     f'{self.__salary['currency']}, {gross}')
                cls.vacancy_lists['with_salary_to'][gross].setdefault(self.__salary['currency'], [])
                cls.vacancy_lists['with_salary_to'][gross][self.__salary['currency']].append(self)
                cls.vacancy_lists['with_salary_to'][gross][self.__salary['currency']].sort(reverse=True)

    def __str__(self):
        professional_roles_str = ''
        for index in range(len(self.professional_roles)):
            professional_roles_str += self.professional_roles[index]['name'] + '\n'
        return (
            f"Вакансия {self.id}: {self.name}\n {self.employer['name']}\n {self.area['name']}\n {self.salary_print}\n"
            f"{self.experience['name']}\n{self.snippet['requirement']}\n{self.snippet['responsibility']}\n"
            f"{self.schedule['name']}\n {professional_roles_str} {self.employer['vacancies_url']}\n"
            f"дата публикации {self.date}\n"
            f"тип вакансии {self.type['name']}\n\n")

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "employer": self.employer,
            "area": self.area,
            "salary": self.__salary,
            "snippet": self.snippet,
            "schedule": self.schedule,
            "professional_roles": self.professional_roles,
            "experience": self.experience,
            "date": self.date,
            "type_vac": self.type,
            "salary_print": self.salary_print
        }

    def __lt__(self, other):
        if self.salary['to'] and other.salary['to'] and self.salary['from'] and other.salary['from']:
            if self.salary['to'] < other.salary['to'] or (
                    self.salary['to'] == other.salary['to'] and self.salary['from'] < other.salary['from']):
                return True
            else:
                return False
        elif self.salary['to'] and other.salary['to'] and not self.salary['from'] and not other.salary['from']:
            if self.salary['to'] < other.salary['to']:
                return True
            else:
                return False
        elif self.salary['to'] and other.salary['to'] and not self.salary['from'] and other.salary['from']:
            if self.salary['to'] < other.salary['to'] or self.salary['to'] == other.salary['to']:
                return True
            else:
                return False
        elif self.salary['to'] and other.salary['to'] and self.salary['from'] and not other.salary['from']:
            if self.salary['to'] < other.salary['to']:
                return True
            else:
                return False
        elif self.salary['from'] and other.salary['from'] and not self.salary['to'] and not other.salary['to']:
            if self.salary['from'] < other.salary['from']:
                return True
            else:
                return False

    def __eq__(self, other):
        if self.salary['from'] == other.salary['from'] and self.salary['to'] == other.salary['to']:
            return True
        else:
            return False
