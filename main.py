import json
from src.parser import HH
from data.definitions import strings_for_print, file_worker_hh, user_choice_default, user_file_json
from src.my_exeption import RequestErrorException
from src.vacancies import Vacancy
from src.connector import ConnectorJson


def int_input_in_range(prompt, range_=None):
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


def user_interactions(start):
    request = []
    if start:
        print(strings_for_print["to_start"])
        print(strings_for_print["execution_phase_start"])
        user_answer = int_input_in_range(strings_for_print["choice"], [0, 1])
    else:
        print(strings_for_print["execution_phase"])
        user_answer = int_input_in_range(strings_for_print["choice"], [0, 3])
    if user_answer == 0:
        return True, request
    elif user_answer == 1:
        print(strings_for_print["request_site"])
        site = int_input_in_range(strings_for_print["choice"], [1, 3])
        print(strings_for_print["request_vacancy"])
        vacancy = input(strings_for_print["choice"])
        if vacancy == '':
            vacancy = user_choice_default['vacancy']
        print(strings_for_print["request_salary"])
        salary = int_input_in_range(strings_for_print["choice"])
        print(strings_for_print["request_region"])
        region = input(strings_for_print["choice"])
        if region == '':
            region = user_choice_default['region']
        request = {'name': 'request', 'site': site, 'region': region, 'vacancy': vacancy,
                   'salary': salary}
        return False, request
    elif user_answer == 2:
        print(strings_for_print["top_n_vacancy"])
        num_vacancies = int_input_in_range(strings_for_print["choice"])
        print(strings_for_print["only_with_salary"])
        only_with_salary = int_input_in_range(strings_for_print["choice"], [0, 1])
        request = {'name': 'top', 'num_vacancies': num_vacancies, 'only_with_salary': only_with_salary}
        return False, request
    elif user_answer == 3:
        print(strings_for_print["add_vacancy"])
        file_type = int_input_in_range(strings_for_print["choice"], [1, 3])
        print(strings_for_print["add_vacancy_rewrite"])
        rewrite_file = int_input_in_range(strings_for_print["choice"], [0, 1])
        request = {'name': 'add', 'file_type': file_type, 'rewrite_file': rewrite_file,}
        return False, request
    elif user_answer == 4:
        print(strings_for_print["del_vacancy"])
        del_vacancy = input(strings_for_print["choice"])
        request = {'name': 'del'}
        return False, request


def main():
    vacancy = None
    end = False
    start = True
    while not end:
        end, user_request = user_interactions(start)
        start = False
        if user_request:
            if user_request['name'] == 'request':
                if user_request['site'] == 1:
                    parser_hh = HH(file_worker_hh)
                    try:
                        area_id = None
                        area_id_lst = []
                        area_lst = parser_hh.get_region_lst(user_request['region'])
                        for area in area_lst:
                            area_id_lst.append(area['id'])
                            print(f'id {area['id']} {area['text']}')
                        print('Введите id региона:')
                        while not area_id:
                            area_id = str(input(strings_for_print["choice"]))
                            print('area_id ', area_id, 'area_lst ', area_lst)
                            if area_id not in area_id_lst:
                                area_id = None
                                print("Неверно введен id региона, попробуйте еще раз")
                        user_request['region'] = area_id
                        print(strings_for_print["request_waiting"])
                        print(parser_hh.load_vacancies(user_request))
                    except RequestErrorException as e:
                        print('RequestError ', e, '\n')
                    else:
                        parser_hh.save_list_in_file()
                        print(f'Получено  {len(parser_hh)} вакансий (на hh.ru ограничение в 2000 вакансий на один '
                              f'запрос)')
                        for item in parser_hh.vacancies:
                            vacancy = Vacancy(item['name'], item['employer'], item['area'], item['salary'],
                                              item['snippet'],
                                              item['schedule'], item['professional_roles'], item['experience'],
                                              item['published_at'], item['type'])

                if user_request['site'] == 2:
                    print('Function is not implemented')
                if user_request['site'] == 3:
                    print('Function is not implemented')
            elif user_request['name'] == 'top':
                print(user_request)
                if user_request['only_with_salary']:

                    for currency in vacancy.vacancy_lists['with_salary_to']['на руки']:
                        print(f'with_salary_to на руки {currency} ',
                              len(vacancy.vacancy_lists['with_salary_to']['на руки'][currency]))
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_to']['на руки'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item.salary)
                                numerate += 1
                            else:
                                break

                    for currency in vacancy.vacancy_lists['with_salary_to']['до вычета налогов']:
                        print(f'with_salary_to до вычета налогов  {currency} ',
                              len(vacancy.vacancy_lists['with_salary_to']['до вычета налогов'][currency]))
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_to']['до вычета налогов'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item.salary)
                                numerate += 1
                            else:
                                break

                    for currency in vacancy.vacancy_lists['with_salary_from']['на руки']:
                        print(f'with_salary_from на руки  {currency} ',
                              len(vacancy.vacancy_lists['with_salary_from']['на руки'][currency]))
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_from']['на руки'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item.salary)
                                numerate += 1
                            else:
                                break

                    for currency in vacancy.vacancy_lists['with_salary_from']['до вычета налогов']:
                        print(f'with_salary_from до вычета налогов  {currency} ',
                              len(vacancy.vacancy_lists['with_salary_from']['до вычета налогов'][currency]))
                        numerate = 0
                        for item in vacancy.vacancy_lists['with_salary_from']['до вычета налогов'][currency]:
                            if numerate < user_request['num_vacancies']:
                                print(item.salary)
                                numerate += 1
                            else:
                                break
                else:
                    numerate = 0
                    print('without_salary ', len(vacancy.vacancy_lists['without_salary']))
                    for item in vacancy.vacancy_lists['without_salary']:
                        if numerate < user_request['num_vacancies']:
                            print(item)
                            numerate += 1
                        else:
                            break

            elif user_request['name'] == 'add':

                print(user_request)
                if user_request['file_type'] == 1:
                    connector_json = ConnectorJson(user_file_json)
                    if user_request['rewrite_file']:

                        connector_json.write_list_in_file([vacancy.vacancy_lists])

                    else:
                        connector_json.add_list_in_file(vacancy.vacancy_lists['without_salary'])
                if user_request['file_type'] == 2:
                    print('Function is not implemented')
                if user_request['file_type'] == 3:
                    print('Function is not implemented')

            elif user_request['name'] == 'del':
                print(user_request)


if __name__ == '__main__':
    main()
