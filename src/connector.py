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
        print("**", obj)
        obj_dict = obj.__dict__()
        return obj_dict

    def load_data(self):
        """
        Загружает данные из файла json
        """
        if self.file != '':
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


class ConnectorTxt(Connector):
    pass


class ConnectorCsv(Connector):
    pass
