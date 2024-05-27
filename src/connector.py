from abc import ABC, abstractmethod
import json


class Connector(ABC):
    """
    Абстрактный класс для работы с хранилищами данных разного типа
    """

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def load_data(self):
        """
        Метод для загрузки данных из хранилища
        """
        pass

    @abstractmethod
    def write_list_in_file(self, list_: list):
        """
        Метод позволяет перезаписать данные в хранилище
        """
        pass

    @abstractmethod
    def add_list_in_file(self, list_: list):
        """
        Метод позволяет дописать данные в хранилище
        """
        pass

    @abstractmethod
    def del_list_from_file(self, list_):
        """
        Удаляет данные из хранилища
        """
        pass


class ConnectorJson(Connector):
    """
    Класс для взаимодействия с файлами в формате json
    """

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
        """
        Перезаписывает файл новыми данными в формате json
        """

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(list_, f, ensure_ascii=False, indent=4, default=self.class_to_dict)

    @staticmethod
    def there_is_item_in_list(item_from_list_, data):
        """
        Проверяет есть ли уже в списке добавляемые данные
        """
        for data_item in data:
            if (item_from_list_.id == data_item["id"] and
                    item_from_list_.name == data_item["name"] and
                    item_from_list_.employer == data_item["employer"] and
                    item_from_list_.area == data_item["area"] and
                    item_from_list_.salary == data_item["salary"] and
                    item_from_list_.snippet == data_item["snippet"] and
                    item_from_list_.schedule == data_item["schedule"] and
                    item_from_list_.professional_roles == data_item["professional_roles"] and
                    item_from_list_.experience == data_item["experience"] and
                    item_from_list_.date == data_item["date"] and
                    item_from_list_.type == data_item["type_vac"] and
                    item_from_list_.salary_print == data_item["salary_print"]):
                return True
        return False

    def add_list_in_file(self, list_):
        """
        Добавляет список в файл json
        """

        data = self.load_data()
        for item in list_:
            if self.there_is_item_in_list(item, data):
                print(f"Вакансия с id {item.id} уже присутствует в файле")
            else:
                print(f"Вакансия с id {item.id} добавлена в файл")
                data.extend([item.__dict__()])

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, default=self.class_to_dict)

    def del_list_from_file(self, list_):
        """
        Удаляет данные из файла json
        """

        data_new = []
        data = self.load_data()
        for item in data:
            if item['id'] in list_:
                print(f"Вакансия с id {item['id']} удалена из файла")
                list_.remove(item['id'])
            else:
                data_new.append(item)

        if list_:
            print(f'Вакансии с id {list_} НЕ найдены в файле')

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data_new, f, ensure_ascii=False, indent=4, default=self.class_to_dict)


class ConnectorTxt(Connector):
    def load_data(self):
        pass

    def write_list_in_file(self, list_: list):
        pass

    def add_list_in_file(self, list_: list):
        pass

    def del_list_from_file(self, list_):
        pass


class ConnectorCsv(Connector):
    def load_data(self):
        pass

    def write_list_in_file(self, list_: list):
        pass

    def add_list_in_file(self, list_: list):
        pass

    def del_list_from_file(self, list_):
        pass
