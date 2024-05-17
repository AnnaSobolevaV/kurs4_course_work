from src.my_exeption import CompareErrorException
from operator import itemgetter, attrgetter


class Vacancy:
    id = 0
    vacancy_lists = {'without_salary': [], 'with_salary_to': {'до вычета налогов': {}, 'на руки': {}},
                     'with_salary_from': {'до вычета налогов': {}, 'на руки': {}}}

    def __init__(self, name, employer, area, salary, snippet, schedule, professional_roles, experience,
                 date, type_vac):
        Vacancy.id += 1
        self.id = Vacancy.id
        self.name = name
        self.employer = employer
        self.area = area
        self._salary = salary
        self.snippet = snippet
        self.schedule = schedule
        self.professional_roles = professional_roles
        self.experience = experience
        self.date = date
        self.type = type_vac
        self.salary_print = ''
        Vacancy.add_vacancy_to_list(self)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary_value):
        self._salary = salary_value

    @classmethod
    def add_vacancy_to_list(cls, self):
        if not self._salary:
            cls.vacancy_lists['without_salary'].append(self)
            self.salary_print = "Зарплата не определена"
        else:
            if self._salary["gross"]:
                gross = "до вычета налогов"
            else:
                gross = "на руки"
            if not self._salary['from']:
                if self._salary['to']:
                    self.salary_print = f'Зарплата до: {self._salary['to']}, {self._salary['currency']}, {gross}'
                    cls.vacancy_lists['with_salary_to'][gross].setdefault(self._salary['currency'], [])
                    cls.vacancy_lists['with_salary_to'][gross][self._salary['currency']].append(self)
                    cls.vacancy_lists['with_salary_to'][gross][self._salary['currency']].sort(reverse=True)
            elif not self._salary['to']:
                self.salary_print = f'Зарплата от: {self._salary['from']}, {self._salary['currency']}, {gross}'
                cls.vacancy_lists['with_salary_from'][gross].setdefault(self._salary['currency'], [])
                cls.vacancy_lists['with_salary_from'][gross][self._salary['currency']].append(self)
                cls.vacancy_lists['with_salary_from'][gross][self._salary['currency']].sort(reverse=True)

            else:
                self.salary_print = (f'Зарплата от: {self._salary['from']}  до: {self._salary['to']}, '
                                     f'{self._salary['currency']}, {gross}')
                cls.vacancy_lists['with_salary_to'][gross].setdefault(self._salary['currency'], [])
                cls.vacancy_lists['with_salary_to'][gross][self._salary['currency']].append(self)
                cls.vacancy_lists['with_salary_to'][gross][self._salary['currency']].sort(reverse=True)

    def __str__(self):
        professional_roles_str = ''
        for index in range(len(self.professional_roles)):
            professional_roles_str += self.professional_roles[index]['name'] + '\n'
        return (
            f"Вакансия {self.id}: {self.name}\n {self.employer['name']}\n {self.area['name']}\n {self.salary_print}\n"
            f"{self.experience['name']}\n{self.snippet['requirement']}\n{self.snippet['responsibility']}\n"
            f"{self.schedule['name']}\n {professional_roles_str} {self.employer['vacancies_url']}\nдата публикации {self.date}\n"
            f"тип вакансии {self.type['name']}\n\n")

#    def __repr__(self):
#        return f"<{self.__class__}, {self.__dict__}>"

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "employer": self.employer,
            "area": self.area,
            "salary": self._salary,
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
