from .ParseAlgoFactory import ParseAlgoFactory


class ParseModule:

    def run(self, path_to_specification: str):
        parsed_file_path = path_to_specification.split('.')
        parser = ParseAlgoFactory(parsed_file_path[-1])

        return parser.run(path_to_specification)

