class PathDTO:
    url_path: str
    parameters: {

    }
    request_body = {
        'required': False,
        'content': {}
    }
    responses = {

    }

    def __init__(self):
        self.parameters = {}

    def add_url_path(self, url_path):
        self.url_path = url_path

    def add_parameter(self, parameter_name, parameter_data):
        self.parameters[parameter_name] = parameter_data

    def add_response(self, response_code, response_data):
        self.responses[response_code] = response_data

    def add_request_body(self, body_data):
        self.request_body = body_data

    def __getitem__(self, item):
        return self.__getattribute__(item)

