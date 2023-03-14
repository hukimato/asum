from .Interpreter import Interpreter


class TemplateModule:

    def __init__(self):
        self.file_extension = None
        self.result_files = {}

    def generate_file_content(self, path_to_template_file: str, dict_of_dto: dict):
        template_content = self.get_template_content(path_to_template_file)

        for dto_path, dto_data in dict_of_dto.items():
            new_file_name = self.get_result_file_name(dto_path)
            interpreter = Interpreter(template_content, dto_data, new_file_name)
            self.result_files[new_file_name] = interpreter.interpret()
        return self.result_files

    def get_template_content(self, path_to_template_file: str) -> str:
        with open(path_to_template_file) as temp_file:
            template_content = temp_file.read()
        return template_content

    def get_result_file_name(self, dto_path: str):
        dto_path = dto_path.replace('{', '')
        dto_path = dto_path.replace('}', '')
        dto_path = dto_path.replace('/', '_')
        return self.to_camel_case(dto_path)

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + ''.join(x.title() for x in components[1:])

    def get_result_file_extension(self, path_to_template_file: str):
        splited_file_name = path_to_template_file.split('.')
        self.file_extension = splited_file_name[-1]
        return self.file_extension
