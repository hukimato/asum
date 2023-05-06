from .ParseAlgoFactory import ParseAlgoFactory


class ParseModule:
    def run(self, path_to_specification: str):
        # Определяется расширение файла спецификации
        parsed_file_path = path_to_specification.split('.')
        # Инициализируется парсер для файла
        parser = ParseAlgoFactory(parsed_file_path[-1])
        return parser.run(path_to_specification)

