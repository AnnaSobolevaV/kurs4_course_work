from abc import ABC, abstractmethod
import json


class Connector(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def write_list_in_file(self, list_: list):
        pass

    @abstractmethod
    def add_list_in_file(self, list_: list):
        pass


class ConnectorJson(Connector):
    def __init__(self, file_json):
        super().__init__(file_json)

    def __repr__(self):
        return f"<{self.__class__}, {self.__dict__}>"

    @staticmethod
    def class_to_dict(obj):
        obj_dict = obj.__dict__()
        return obj_dict

    def load_data(self):
        """
        Загружает данные из файла json
        """
        if self.file:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data

    def write_list_in_file(self, list_):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(list_, f, ensure_ascii=False, indent=4, default=self.class_to_dict)

    def add_list_in_file(self, list_):
        data = self.load_data()
        data.extend(list_)
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, default=self.class_to_dict)

    def del_list_in_file(self, list_):
        data_new = []
        data = self.load_data()
        for data_item in data:
            for currency in data_item['with_salary_to']['на руки']:
                print(currency)
                for item in data_item['with_salary_to']['на руки'][currency]:
                    print(item['id'])
                    if item['id'] in list_:
                        print(f'Вакансия с id {item['id']} удалена из файла')
                        list_.remove(item['id'])
                    else:
                        data_new.append(item)
            for currency in data_item['with_salary_to']['до вычета налогов']:
                print(currency)
                for item in data_item['with_salary_to']['до вычета налогов'][currency]:
                    print(item['id'])
                    if item['id'] in list_:
                        print(f'Вакансия с id {item['id']} удалена из файла')
                        list_.remove(item['id'])
                    else:
                        data_new.append(item)
            for currency in data_item['with_salary_from']['на руки']:
                print(currency)
                for item in data_item['with_salary_from']['на руки'][currency]:
                    print(item['id'])
                    if item['id'] in list_:
                        print(f'Вакансия с id {item['id']} удалена из файла')
                        list_.remove(item['id'])
                    else:
                        data_new.append(item)
            for currency in data_item['with_salary_from']['до вычета налогов']:
                print(currency)
                for item in data_item['with_salary_from']['до вычета налогов'][currency]:
                    print(item['id'])
                    if item['id'] in list_:
                        print(f'Вакансия с id {item['id']} удалена из файла')
                        list_.remove(item['id'])
                    else:
                        data_new.append(item)
            for item in data_item['without_salary']:
                print(item['id'])
                if item['id'] in list_:
                    print(f'Вакансия с id {item['id']} удалена из файла')
                    list_.remove(item['id'])
                else:
                    data_new.append(item)

            #if data_item['id']:
            print(data_item)

                if data_item['id'] in list_:
                    print(f'Вакансия с id {data_item['id']} удалена из файла')
                    list_.remove(data_item["id"])
                else:
                    data_new.append(data_item)

            if list_:
                print(f'Вакансии с id {list_} НЕ найдены в файле')

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data_new, f, ensure_ascii=False, indent=4, default=self.class_to_dict)


class ConnectorTxt(Connector):
    pass


class ConnectorCsv(Connector):
    pass
