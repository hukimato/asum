from asum.input.DataCollectorInterface import DataCollectorInterface
from sys import argv


class DataCollector(DataCollectorInterface):

    def __init__(self, list_of_arguments_name: list):
        # Получение имен параметров
        self.list_of_arguments_name = list_of_arguments_name

    # Получение данных из глобальной переменной argv
    def get_data(self) -> dict:
        # argv_test = ['main.py', 'specification_file=../specifications/openapi.json',
        #              'template_file=../templates/template.php', 'destination_dir=../generated/']
        parameters = self.__filter_params(argv)
        #parameters = self.__filter_params(argv_test)
        if self.__check_required_params(parameters):
            return parameters
        else:
            raise Exception("Required parameters are missed")

    # Составление словаря из списка параметров
    def __filter_params(self, argv_data: list) -> dict:
        parameters = {}
        for argument in argv_data:
            argument_parsed = argument.split('=')
            if len(argument_parsed) != 2:
                continue
            argument_name = argument_parsed[0]
            argument_value = argument_parsed[1]
            # Проверка возможного параметра
            if argument_name not in self.list_of_arguments_name:
                continue
            parameters[argument_name] = argument_value
        return parameters

    # Проверка наличия обязательных параметров
    def __check_required_params(self, parameters: dict) -> bool:
        return all([param in parameters.keys() for param in self.list_of_arguments_name])
