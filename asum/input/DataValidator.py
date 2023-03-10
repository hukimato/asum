from pathlib import Path


class DataValidator:

    def __init__(self, list_of_arguments_name: dict):
        self.list_of_arguments_name = list_of_arguments_name

    def validate(self, data: dict):
        for param_name, param_type in self.list_of_arguments_name.items():
            my_file = Path(data[param_name])
            if param_type == 'file':
                if not my_file.is_file():
                    raise Exception(f'File {data[param_name]} does not exists')
            elif param_type == 'dir':
                if not my_file.is_dir():
                    raise Exception(f'Directory {data[param_name]} does not exists')
            else:
                raise Exception(f'Unexpected type {param_type}')
