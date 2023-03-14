from asum.DTO.PathDTO import PathDTO


class DTOBuilder:

    def __init__(self):
        self.new_dto = PathDTO()

    def build(self, url_path: str, raw_data: dict) -> PathDTO:
        self.__build_url_path(url_path)
        self.__build_parameters(raw_data.get('parameters'))
        self.__build_request_bodies(raw_data.get('requestBody'))
        self.__build_responses(raw_data.get('responses'))
        return self.new_dto

    def __build_parameters(self, raw_parameters_data: list):
        if raw_parameters_data is None:
            return
        for parameter in raw_parameters_data:
            self.new_dto.add_parameter(parameter['name'], parameter)

    def __build_request_bodies(self, raw_request_body: dict):
        if raw_request_body is None:
            return
        self.new_dto.add_request_body(raw_request_body)

    def __build_responses(self, raw_response_data):
        if raw_response_data is None:
            return
        for status, response in raw_response_data.items():
            self.new_dto.add_response(status, response)

    def __build_url_path(self, url_path):
        self.new_dto.add_url_path(url_path)
