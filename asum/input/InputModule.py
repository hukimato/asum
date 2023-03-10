from asum.input.DataCollector import DataCollector
from asum.input.DataValidator import DataValidator


class InputModule:

    def __init__(self, list_of_arguments_name: dict):
        """
        Construct InputModel
        :param list_of_arguments_name: Словарь (имя_переменной: тип_данных)
        :type list_of_arguments_name: dict
        """
        self.list_of_arguments_name = list_of_arguments_name

    def get_input_data(self):
        data_collector = DataCollector(list(self.list_of_arguments_name.keys()))
        data_validator = DataValidator(self.list_of_arguments_name)

        try:
            result = data_validator.validate(data_collector.get_data())
        except Exception as e:
            raise e

        return result

