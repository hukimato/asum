from abc import ABC, abstractmethod


class DataCollectorInterface(ABC):

    @abstractmethod
    def get_data(self):
        pass
