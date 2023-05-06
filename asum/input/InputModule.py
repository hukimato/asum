from asum.input.DataCollector import DataCollector
from asum.input.DataValidator import DataValidator


class InputModule:

    def __init__(self, list_of_arguments_name: dict):
        # Получение имен и типов параметров
        self.list_of_arguments_name = list_of_arguments_name

    # Метод получения данных
    def get_input_data(self):
        # Инициализация компонентов получения и валидации данных
        data_collector = DataCollector(list(self.list_of_arguments_name.keys()))
        data_validator = DataValidator(self.list_of_arguments_name)

        # Получение данных из DataCollector
        result = data_collector.get_data()
        try:
            # Валидация данных
            data_validator.validate(result)
            return result
        except Exception as e:
            raise e
