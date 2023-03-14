from abc import ABC, abstractmethod


class HandlerInterface(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def handle_expression(self, start_index, stop_index, content):
        pass
