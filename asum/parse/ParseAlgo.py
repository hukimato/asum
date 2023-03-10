from abc import ABC, abstractmethod


class ParseAlgo(ABC):

    def run(self, file_path) -> dict:
        with open(file_path) as file:
            file_data = file.read()
            parsed_file_data = self.parse(file_data)
        return parsed_file_data

    @abstractmethod
    def parse(self, file_data: str) -> dict:
        return {'raw_file_data': file_data}
