from abc import ABC, abstractmethod


class Connector(ABC):
    pass


class ConnectorJson(Connector):
    pass

class ConnectorTxt(Connector):
    pass
class ConnectorCsv(Connector):
    pass
