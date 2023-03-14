from .DTOBuilder import DTOBuilder


class PreparatorModule:

    def __init__(self):
        self.specification_file_data = {}

    def prepare_DTO(self, specification_file_data: dict) -> list:
        self.specification_file_data = specification_file_data

        specification_with_replaces = self.replace_all_refs(self.specification_file_data)

        dto_map = {}
        for path, data in specification_with_replaces['paths'].items():
            dto_map[path] = {}
            for http_method in data.keys():
                dto_map[path][http_method] = DTOBuilder().build(path, data[http_method])
        return dto_map

    def replace_all_refs(self, data: dict):
        if type(data) is not dict:
            return data
        for key in data.keys():
            if type(data[key]) is dict and len(data[key].keys()) == 1 and '$ref' in data[key].keys():
                ref_link = data[key]['$ref']
                ref_link_parsed = ref_link.split('/')
                data[key] = self.safe_get(ref_link_parsed[1:])
            data[key] = self.replace_all_refs(data[key])
        return data

    def safe_get(self, keys: list):
        dct = self.specification_file_data
        for key in keys:
            try:
                dct = dct[key]
            except KeyError:
                return None
        return dct
