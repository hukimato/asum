from .ParseAlgo import ParseAlgo
from .JsonParseAlgo import JsonParseAlgo
from .YamlParseAlgo import YamlParseAlgo


class ParseAlgoFactory:

    def __new__(cls, file_ext: str) -> ParseAlgo:
        if file_ext == 'json':
            return JsonParseAlgo()
        elif file_ext in ['yaml', 'yml']:
            return YamlParseAlgo()
        else:
            raise Exception(f'Unexpected file extension {file_ext}')

