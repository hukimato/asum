from ParseAlgo import ParseAlgo
import json


class JsonParseAlgo(ParseAlgo):

    def parse(self, file_data: str) -> dict:
        return json.loads(file_data)