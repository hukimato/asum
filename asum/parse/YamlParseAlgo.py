from ParseAlgo import ParseAlgo
import yaml


class YamlParseAlgo(ParseAlgo):

    def parse(self, file_data: str) -> dict:
        return yaml.safe_load(file_data)
