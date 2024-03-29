from pathlib import Path


class DataValidator:

    def __init__(self, list_of_arguments_name: dict):
        self.list_of_arguments_name = list_of_arguments_name

    def validate(self, data: dict):
        # Для каждого параметра и его типа из конфигурации
        for param_name, param_type in self.list_of_arguments_name.items():
            # Создается объект Path из модуля pathlib
            # param_name - путь до файла/директории
            my_file = Path(data[param_name])
            if param_type == 'file':
                # Проверяется, валидность и существование файла
                if not my_file.is_file():
                    raise Exception(f'File {data[param_name]} does not exists')
            elif param_type == 'dir':
                # Проверяется, валидность и существование директории
                if not my_file.is_dir():
                    raise Exception(f'Directory {data[param_name]} does not exists')
            else:
                raise Exception(f'Unexpected type {param_type}')
