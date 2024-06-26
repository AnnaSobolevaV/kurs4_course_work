# kurs4_course_work
Курсовая работа по курсу ООП
Программа, которая получает информацию о вакансиях с платформы hh.ru в России, сохраняет ее в файл и позволяет удобно
работать с ней: добавлять, фильтровать, удалять.

Создан абстрактный класс для работы с API сервиса с вакансиями -class Parser(ABC). 
Реализован класс - class HH(Parser),
наследующийся от абстрактного класса, для работы с платформой hh.ru. 
Класс подключается к API и получает вакансии.
Создан класс для работы с вакансиями - class Vacancy. В этом классе есть следующие атрибуты:
        query_id: str               - id запроса, в котором получена вакансия;
        id: str                     - id вакансии;
        name: str                   - название вакансии;
        employer: dict              - работодатель;
        area: dict                  - место нахождение работодателя;
        __salary: dict              - зарплата;
        snippet: dict               - требования и обязанности;
        schedule: dict              - график работы;
        professional_roles: dict    - профессиональные роли;
        experience: dict            - опыт;
        date: str                   - дата публикации вакансии;
        type: dict                  - тип вакансии;
        salary_print: str           - зарплата для вывода на печать;
        Vacancy.id: int             - номер вакансии - классовый атрибут;
        vacancy_lists: dict         - словарь списков вакансий, отсортированный по зарплате.
В классе есть методы сравнения вакансий между собой по зарплате.

Создан абстрактный класс - class Connector(ABC), который обязывает реализовать методы для добавления вакансий в файл, 
получения данных из файла и удаления информации о вакансиях. 
Создан класс для сохранения информации о вакансиях в JSON-файл - class ConnectorJson(Connector).

Создана функция для взаимодействия с пользователем через консоль - def user_interactions(start).
Возможности этой функции:
-ввод ключевых слов для запроса вакансий из hh.ru: название вакансии, ожидаемая зарплата, регион поиска работы;
-вывод топ N вакансий по зарплате (N запрашивает у пользователя);
-получение вакансий с ключевым словом в описании.

Все классы и функции объединены в единую программу.

Выходные данные:
Информация о вакансиях, полученная с разных платформ, 
(в данной реализации только с платформы hh.ru) сохраненная в JSON-файл.
Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.