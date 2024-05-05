import json
from src.parser import HH
from data.definitions import strings_for_print, file_worker_hh, user_choice_default
from src.my_exeption import RequestErrorException
from src.vacancies import Vacancy


def load_data(file_json):
    """
    Загружает данные из файла json
    """
    if file_json != '':
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


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
    print(strings_for_print["execution_phase"])
    user_answer = int_input_in_range(strings_for_print["choice"], [0, 3])
    if user_answer == 0:
        return True, request
    elif user_answer == 1:
        print(strings_for_print["request_site"])
        site = int_input_in_range(strings_for_print["choice"], [1, 3])
        print(strings_for_print["request_region"])
        region = input(strings_for_print["choice"])
        if region == '':
            region = user_choice_default['region']
        print(strings_for_print["request_vacancy"])
        vacancy = input(strings_for_print["choice"])
        if vacancy == '':
            vacancy = user_choice_default['vacancy']
        print(strings_for_print["request_salary"])
        salary_from = int_input_in_range(strings_for_print["choice"])
        print(strings_for_print["request_waiting"])
        # if salary_from == 0:
        #     salary_from = 1
        request = {'name': 'request', 'site': site, 'region': region, 'vacancy': vacancy,
                   'salary_from': salary_from}
        return False, request

    elif user_answer == 2:
        print(strings_for_print["add_vacancy"])
        add_vacancy = input(strings_for_print["choice"])
        request = {'name': 'add'}
        return False, request
    elif user_answer == 3:
        print(strings_for_print["del_vacancy"])
        del_vacancy = input(strings_for_print["choice"])
        request = {'name': 'del'}
        return False, request


def main():
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
                        parser_hh.load_vacancies(user_request)
                    except RequestErrorException as e:
                        print('RequestError ', e, '\n')
                    else:
                        parser_hh.save_data_in_file(file_worker_hh)

                if user_request['site'] == 2:
                    print('Function is not implemented')
                if user_request['site'] == 3:
                    print('Function is not implemented')
            elif user_request['name'] == 'add':
                vacancies = []
                print(user_request)
                if file_worker_hh != '':
                    data = load_data(file_worker_hh)
                    for item in data:
                        vacancy = Vacancy(item['name'], item['department'], item['salary'], item['snippet'],
                                          item['schedule'], item['professional_roles'], item['experience'])

                        vacancies.append(vacancy)
                        print(vacancy.name, vacancy.salary)

            elif user_request['name'] == 'del':
                print(user_request)


if __name__ == '__main__':
    main()
