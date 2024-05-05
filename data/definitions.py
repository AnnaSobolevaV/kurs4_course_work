import os

DATA_PATH = os.path.abspath('data')
file_worker_hh = os.path.join(DATA_PATH, 'file_worker_hh.json')
file_json = os.path.join(DATA_PATH, 'vacancies.json')
file_txt = os.path.join(DATA_PATH, 'vacancies.txt')
file_csv = os.path.join(DATA_PATH, 'vacancies.csv')
user_choice_default = {'region': 'Москва', 'vacancy': 'Python'}
strings_for_print = {
    "to_start": "Добро пожаловать на наш сервис!\nБыстро и удобно поможем найти лучшую для Вас работу.",
    "request_site": "Выберете сайт для поиска вакансии (введите 1, 2 или 3):\n1. hh.ru\n2. rabota.ru\n3. avito.ru",
    "request_region": "Введите регион: (пример: Санкт-Петербург, Москва, Саратовская область,...)",
    "request_vacancy": "Введите интересующую Вас вакансию: (пример: менеджер по продажам)",
    "request_salary": "Введите ожидаемую зарплату - от: (пример: 50000), либо 0, если зарплата может быть любой",
    "request_waiting": "Ваш запрос обрабатывается",
    "execution_phase": "Введите 0, 1, 2 или 3:\n0: закончить программу\n1: отправить запрос\n2: добавить результат "
                       "запроса в файл\n3: удалить вакансию из файла""",
    "choice": "Ваш выбор: ",
    "error_input": "Некорректный ввод, попробуйте еще раз",
    "add_vacancy": "Выберете формат файла, в котором необходимо сохранить данные:\n1. .json\n2. .txt\n3. .csv",
    "del_vacancy": "Введите id вакансии, которую необходимо удалить: "
    }
