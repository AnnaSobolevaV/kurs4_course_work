import json
from src.parser import HH
from data.definitions import strings_for_print
from src.my_exeption import MyException


def int_input(prompt, range_):
    input_int = 0
    ok = False
    while not ok:
        try:
            input_int = int(input(prompt))
        except ValueError:
            print(strings_for_print["error_input"])
        else:
            if input_int in range(range_[0], range_[1]+1):
                ok = True
            else:
                print(strings_for_print["error_input"])
    return input_int


def float_input(prompt):
    input_float = 0
    ok = False
    while not ok:
        try:
            input_float = float(input(prompt))
        except ValueError:
            print(strings_for_print["error_input"])
        else:
            ok = True
    return input_float


def user_interactions(start):
    request = []
    if start:
        print(strings_for_print["to_start"])
    print(strings_for_print["execution_phase"])
    user_answer = int_input(strings_for_print["choice"], [0, 3])
    if user_answer == 0:
        return True, request
    elif user_answer == 1:
        print(strings_for_print["request_site"])
        request_site = int_input(strings_for_print["choice"], [1, 3])
        print(strings_for_print["request_region"])
        request_region = input(strings_for_print["choice"])
        print(strings_for_print["request_vacancy"])
        request_vacancy = input(strings_for_print["choice"])
        print(strings_for_print["request_salary"])
        request_salary = float_input(strings_for_print["choice"])
        print(strings_for_print["request_waiting"])
        request = ['request', request_site, request_region, request_vacancy, request_salary]
        return False, request

    elif user_answer == 2:
        print(strings_for_print["add_vacancy"])
        add_vacancy = str(input(strings_for_print["choice"]))
        request = ['add', add_vacancy]
        return False, request
    elif user_answer == 3:
        print(strings_for_print["del_vacancy"])
        del_vacancy = str(input(strings_for_print["choice"]))
        request = ['del', del_vacancy]
        return False, request
    else:
        print(strings_for_print["error_input"])
        request = []
        return False, request


def main():
    end = False
    start = True
    while not end:
        end, request = user_interactions(start)
        start = False
        if request:
            print(request)
            data = []


if __name__ == '__main__':
    main()
