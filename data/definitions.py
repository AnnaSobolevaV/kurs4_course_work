import os

"""
Файл с некоторыми предопределенными переменными 
"""

DATA_PATH = os.path.abspath('data')
file_worker_hh = os.path.join(DATA_PATH, 'file_worker_hh.json')
user_file_json = os.path.join(DATA_PATH, 'vacancies.json')
user_file_txt = os.path.join(DATA_PATH, 'vacancies.txt')
user_file_csv = os.path.join(DATA_PATH, 'vacancies.csv')
user_choice_default = {'region': 'Мурманск', 'vacancy': 'менеджер по продажам'}
strings_for_print = {
    "to_start": "Добро пожаловать на наш сервис!\nБыстро и удобно поможем найти лучшую для Вас работу.",
    "request_site": "Выберете сайт для поиска вакансии (введите 1, 2 или 3):\n1. hh.ru\n"
                    "2. rabota.ru (функция временно не доступна)\n3. avito.ru (функция временно не доступна)",
    "request_region": "Введите регион: (пример: Мурманск, Санкт-Петербург, Саратовская область,...)",
    "request_vacancy": "Введите интересующую Вас вакансию: (пример: менеджер по продажам)",
    "request_salary": "Введите ожидаемую зарплату - от: (пример: 50000), либо 0, если зарплата может быть любой",
    "request_waiting": "Ваш запрос обрабатывается",
    "execution_phase": "Введите 0, 1, 2, 3 или 4:\n0: закончить программу\n1: отправить запрос\n2: вывести на экран N "
                       "вакансий\n3: добавить результат в файл\n4: удалить вакансии из файла""",
    "execution_phase_start": "Введите 0 или 1:\n0: закончить программу\n1: отправить запрос""",
    "top_n_vacancy": "Введите количество вакансий, которые необходимо вывести на экран: ",
    "only_with_salary": "Введите 1, чтобы получить N вакансий ранжированных по зарплате\n"
                        "(будут выведены по N вакансий для каждой группы зарплат: "
                        "'Зарплата от', 'Зарплата до', с разбиением по:'до вычета налогов', 'на руки',  "
                        "сгруппированные для каждой валюты)\n"
                        " или 0, чтобы вывести N вакансий, в которых 'Зарплата не определена'",
    "": "",
    "choice": "Ваш выбор: ",
    "error_input": "Некорректный ввод, попробуйте еще раз",
    "add_vacancy_type_file": "Выберете формат файла, в котором необходимо сохранить данные:\n"
                             "1. .json\n2. .txt (функция временно не доступна)\n3. .csv (функция временно не доступна)",
    "add_vacancy_rewrite": "Введите 1, если файл надо перезаписать данными или 0, если данные нужно добавить в файл",
    "add_vacancy_list": "Введите id вакансий (через запятую), которые надо сохранить в файл\n"
                        "(пример: queryHH_1_1, queryHH_1_2, queryHH_1_4, queryHH_1_7)\n "
                        "или 0, если необходимо сохранить все вакансии",
    "del_vacancy_type_file": "Выберете формат файла, из которого удалим данные:\n1. .json\n"
                             "2. .txt (функция временно не доступна)\n3. .csv (функция временно не доступна)",
    "del_vacancy": "Введите id вакансий, которые необходимо удалить\n "
                   "(пример: queryHH_1_1, queryHH_1_2, queryHH_1_4, queryHH_1_7) "
    }
