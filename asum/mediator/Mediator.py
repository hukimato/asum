class Mediator:

    # Инициализация внутренних модулей
    def __init__(self, config: dict):
        self.input_module = config['modules']['input_module'](config['parameters'])
        self.parse_module = config['modules']['parse_module']()
        self.prepare_module = config['modules']['prepare_module']()
        self.template_module = config['modules']['template_module']()
        self.file_create_module = config['modules']['file_create_module']()

    # Вызов модулей
    def run(self):
        input_parameters = self.input_module.get_input_data()

        path_to_specification = input_parameters['specification_file']
        path_to_template = input_parameters['template_file']
        path_to_destination_dir = input_parameters['destination_dir']

        specification_file_data = self.parse_module.run(path_to_specification)

        list_of_dto = self.prepare_module.prepare_DTO(specification_file_data)

        dict_of_files = self.template_module.generate_file_content(path_to_template, list_of_dto)

        generation_status = self.file_create_module.run(dict_of_files, path_to_destination_dir)

        return generation_status


