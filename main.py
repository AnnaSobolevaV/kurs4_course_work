from src.parser import HH
from data.definitions import strings_for_print, user_choice_default, user_file_json
from src.my_exeption import RequestErrorException
from src.vacancies import Vacancy
from src.connector import ConnectorJson


def int_input_in_range(prompt, range_=None):
    """
    Функция проверяет что пользователем введено целое число и оно принадлежит промежутку
    """

    input_int = 0
    ok = False
    while not ok:
        try:
            input_int = int(input(prompt))
        except ValueError:
            print(strings_for_print["error_input"])
        else:
            if range_:
                if input_int in range(range_[0], range_[1] + 1):
                    ok = True
                else:
                    print(strings_for_print["error_input"])
            else:
                ok = True
    return input_int


def input_str_to_list(prompt):
    """
    Функция преобразует строку с разделенными запятой строками в список строк
    """

    ok = False
    input_list = []
    while not ok:

        input_str = input(prompt).replace(' ', '')
        input_list = input_str.split(",")
        if input_list == ['']:
            print(strings_for_print["error_input"])
        else:
            ok = True

    return input_list


def user_interactions(start):
    """
    Функция производящая взаимодействие с пользователем
    возвращает словарь с выбранными пользователем параметрами запроса
    """

    request = []
    if start:  # выбор пользователь при старте приложения
        print(strings_for_print["execution_phase_start"])
        user_answer = int_input_in_range(strings_for_print["choice"], [0, 1])
    else:  # выбор пользователь не при старте приложения
        print(strings_for_print["execution_phase"])
        user_answer = int_input_in_range(strings_for_print["choice"], [0, 4])
    if user_answer == 0:  # если закончить программу
        return True, request
    elif user_answer == 1:  # если отправить запрос по API
        print(strings_for_print["request_site"])
        site = int_input_in_range(strings_for_print["choice"], [1, 3])  # выбор сайта вакансий
        print(strings_for_print["request_vacancy"])
        vacancy = input(strings_for_print["choice"])  # вводим ключевые слова для запроса
        if vacancy == '':
            vacancy = user_choice_default['vacancy']
        print(strings_for_print["request_salary"])
        salary = int_input_in_range(strings_for_print["choice"])  # вводим ожидаемую зарплату
        print(strings_for_print["request_region"])
        region = input(strings_for_print["choice"])  # вводим регион для поиска вакансии
        if region == '':
            region = user_choice_default['region']
        request = {'name': 'request', 'site': site, 'region': region, 'vacancy': vacancy,
                   'salary': salary}
        return False, request
    elif user_answer == 2:  # если вывести топ вакансий
        print(strings_for_print["top_n_vacancy"])
        num_vacancies = int_input_in_range(strings_for_print["choice"])  # вводим число вакансий для просмотра
        print(strings_for_print["only_with_salary"])
        # если хотим увидеть топ ранжированных вакансий по зарплате
        only_with_salary = int_input_in_range(strings_for_print["choice"], [0, 1])
        request = {'name': 'top', 'num_vacancies': num_vacancies, 'only_with_salary': only_with_salary}
        return False, request
    elif user_answer == 3:  # если добавить вакансии в файл
        print(strings_for_print["add_vacancy_list"])
        add_vacancy_list = input_str_to_list(strings_for_print["choice"])  # вводим список вакансий
        print(strings_for_print["add_vacancy_type_file"])
        file_type = int_input_in_range(strings_for_print["choice"], [1, 3])  # выбираем тип файла куда сохранить
        print(strings_for_print["add_vacancy_rewrite"])
        rewrite_file = int_input_in_range(strings_for_print["choice"], [0, 1])  # перезаписать файл или добавить
        request = {'name': 'add', 'add_vacancy_list': add_vacancy_list,
                   'file_type': file_type, 'rewrite_file': rewrite_file, }
        return False, request
    elif user_answer == 4:  # если удалить вакансии из файла
        print(strings_for_print["del_vacancy"])
        del_vacancy_lst = input_str_to_list(strings_for_print["choice"])  # вводим список вакансий
        print(strings_for_print["del_vacancy_type_file"])
        file_type = int_input_in_range(strings_for_print["choice"], [1, 3])  # выбираем тип файла откуда удалить
        request = {'name': 'del', 'file_type': file_type, 'del_vacancy_lst': del_vacancy_lst}
        return False, request


def main():
    vacancy = None
    connector_json = ConnectorJson(user_file_json)  # создаем объект для работы с Json файлом
    end = False  # флаг выхода из программы
    start = True  # флаг старта программы
    print(strings_for_print["to_start"])
    while not end:  # пока не конец программы
        end, user_request = user_interactions(start)  # запускаем взаимодействие с пользователем
        if user_request:
            if user_request['name'] == 'request':  # пользователь отправляет запрос к API
                if user_request['site'] == 1:  # выбран сайт hh.ru
                    parser_hh = HH()
                    try:
                        area_id = None
                        area_id_lst = []
                        # получаем список id регионов для поиска вакансии
                        # (по ключевому слову из запроса пользователя)
                        area_lst = parser_hh.get_region_lst(user_request['region'])
                        for area in area_lst:
                            area_id_lst.append(area['id'])
                            print(f"id {area['id']} {area['text']}")
                        print('Введите id региона:')
                        # выбираем один id региона для поиска вакансии
                        while not area_id:
                            area_id = str(input(strings_for_print["choice"]))
                            if area_id not in area_id_lst:
                                print('area_id ', area_id)
                                area_id = None
                                print("Неверно введен id региона, попробуйте еще раз")
                        user_request['region'] = area_id
                        print(strings_for_print["request_waiting"])
                        # отправляем запрос в API и получаем список вакансий
                        print(parser_hh.load_vacancies(user_request))
                    except RequestErrorException as e:
                        print('RequestError ', e, '\n')
                    else:
                        print(f'Получено  {len(parser_hh)} вакансий (на hh.ru ограничение в 2000 вакансий на один '
                              f'запрос)')
                        # из списка вакансий, полученных из запроса, формируем объекты типа Vacancy
                        for item in parser_hh.vacancies:
                            vacancy = Vacancy(parser_hh.id, item['name'], item['employer'],
                                              item['area'], item['salary'],
                                              item['snippet'],
                                              item['schedule'], item['professional_roles'], item['experience'],
                                              item['published_at'], item['type'])
                        start = False

                if user_request['site'] == 2:  # выбран сайт rabota.ru
                    print('-------- Упс! Функция еще не реализована')
                if user_request['site'] == 3:  # выбран сайт avito.ru
                    print('-------- Упс! Функция еще не реализована')
            elif user_request['name'] == 'top':  # пользователь хочет вывести топ вакансий
                only_with_salary = 0
                if user_request['only_with_salary']:  # выводим список вакансий с указанной зарплатой
                    for currency in vacancy.vacancy_lists['with_salary_to']['на руки']:  # зарплата "до" "на руки"
                        print(f'---"Зарплата до", "на руки", "{currency}" - всего найдено: ',
                              len(vacancy.vacancy_lists["with_salary_to"]["на руки"][currency]))
                        only_with_salary += len(vacancy.vacancy_lists['with_salary_to']['на руки'][currency])
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_to']['на руки'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item)
                                numerate += 1
                            else:
                                break
                    # зарплата "до" "до вычета налогов"
                    for currency in vacancy.vacancy_lists['with_salary_to']['до вычета налогов']:
                        print(f'---"Зарплата до", "до вычета налогов",  "{currency}" - всего найдено: ',
                              len(vacancy.vacancy_lists["with_salary_to"]["до вычета налогов"][currency]))
                        only_with_salary += len(vacancy.vacancy_lists['with_salary_to']['до вычета налогов'][currency])
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_to']['до вычета налогов'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item)
                                numerate += 1
                            else:
                                break
                    # зарплата "от" "на руки"
                    for currency in vacancy.vacancy_lists['with_salary_from']['на руки']:
                        print(f'---"Зарплата от", "на руки", "{currency}" - всего найдено: ',
                              len(vacancy.vacancy_lists['with_salary_from']['на руки'][currency]))
                        only_with_salary += len(vacancy.vacancy_lists['with_salary_from']['на руки'][currency])
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_from']['на руки'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item)
                                numerate += 1
                            else:
                                break
                    # зарплата "от" "до вычета налогов"
                    for currency in vacancy.vacancy_lists['with_salary_from']['до вычета налогов']:
                        print(f'---"Зарплата от", "до вычета налогов",  "{currency}" - всего найдено: ',
                              len(vacancy.vacancy_lists['with_salary_from']['до вычета налогов'][currency]))
                        only_with_salary += (
                            len(vacancy.vacancy_lists['with_salary_from']['до вычета налогов'][currency]))
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_from']['до вычета налогов'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item)
                                numerate += 1
                            else:
                                break
                    if not only_with_salary:
                        print("Вакансий с указанной зарплатой нет")
                else:
                    numerate = 0
                    print('---"Зарплата не определена"  - всего найдено: ',
                          len(vacancy.vacancy_lists['without_salary']))
                    for item in vacancy.vacancy_lists['without_salary']:
                        if numerate < user_request['num_vacancies']:
                            print(item)
                            numerate += 1
                        else:
                            break

            elif user_request['name'] == 'add':  # пользователь хочет добавить вакансии в файл
                list_to_add = []
                if user_request['file_type'] == 1:  # в файл json
                    list_ = vacancy.get_vacancy_list()
                    if len(user_request['add_vacancy_list']) == 1 and user_request['add_vacancy_list'][0] == '0':
                        list_to_add.extend(list_)
                    else:
                        for item in list_:
                            if item.id in user_request['add_vacancy_list']:
                                list_to_add.append(item)
                                print(f'Вакансия с id {item.id} добавлена в список')
                                user_request['add_vacancy_list'].remove(item.id)
                        if user_request['add_vacancy_list']:
                            print(f"Вакансии с id {user_request['add_vacancy_list']} НЕ добавлены в список")

                    if user_request['rewrite_file']:
                        connector_json.write_list_in_file(list_to_add)
                    else:
                        connector_json.add_list_in_file(list_to_add)
                if user_request['file_type'] == 2:  # в файл txt
                    print('-------- Упс! Функция еще не реализована')
                if user_request['file_type'] == 3:  # в файл csv
                    print('-------- Упс! Функция еще не реализована')

            elif user_request['name'] == 'del':  # пользователь хочет удалить вакансии из файла
                if user_request['file_type'] == 1:  # из файла json
                    connector_json.del_list_from_file(user_request['del_vacancy_lst'])
                if user_request['file_type'] == 2:  # из файла txt
                    print('-------- Упс! Функция еще не реализована')
                if user_request['file_type'] == 3:  # из файла csv
                    print('-------- Упс! Функция еще не реализована')


if __name__ == '__main__':
    main()
