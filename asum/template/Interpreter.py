from .ForHandler import ForHandler
from .IfHandler import IfHandler
from .TerminalHandler import TerminalHandler
import re

for_pattern = r"<#for (?P<array>\S+) as (?P<item>\S+)#>"
if_pattern = r'<#\s*if (?P<bool_expression>.+)\s+#>'
terminal_pattern = r'<#(?P<terminal_expression>.+)#>'

# Вспомогательная функция
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result


class Interpreter:

    def __init__(self, content, data, dto_path, extra_args={}):
        self.content = content
        self.data = {
            'data': data,
            'path': dto_path
        }
        for key, val in extra_args.items():
            self.data[key] = val

    def interpret(self):
        # Разбивает контент шаблона на слова
        interpreted_content = []
        splited_content = self.content.split(' ')
        splited_content = intersperse(splited_content, ' ')
        splited_content = self.get_token_list(splited_content)
        splited_content = list(filter(lambda item: item != '', splited_content))

        index = 0
        while index < len(splited_content):
            if '<#' in splited_content[index]:
                index, expression = self.interpret_expression(index, splited_content)
                interpreted_content.append(expression)
            else:
                interpreted_content.append(splited_content[index])
            index += 1
        return ''.join(interpreted_content)

    # Интерпретирует выражение в зависимости от токена
    def interpret_expression(self, start_index, splited_content):
        token = splited_content[start_index]
        if re.match(for_pattern, token) is not None:
            stop_index = self.find_end_of_for(start_index, splited_content)
            handler = ForHandler(self.data)
            return handler.handle_expression(start_index, stop_index, splited_content)
        elif re.match(if_pattern, token) is not None:
            stop_index = self.find_end_of_if(start_index, splited_content)
            handler = IfHandler(self.data)
            return handler.handle_expression(start_index, stop_index, splited_content)
        elif re.match(terminal_pattern, token) is not None:
            handler = TerminalHandler(self.data)
            return handler.handle_expression(start_index, start_index, splited_content)
        else:
            raise Exception(f'Unexpected token {token}')

    # Находит индекс слова, на котором заканчивается выражение for
    @staticmethod
    def find_end_of_for(start_index, content):
        endif_balance = 1
        stop_index = start_index
        while endif_balance != 0:
            stop_index += 1
            if 'for ' in content[stop_index]:
                endif_balance += 1
            elif 'endfor' in content[stop_index]:
                endif_balance -= 1
        return stop_index

    # Находит индекс слова, на котором заканчивается выражение if
    @staticmethod
    def find_end_of_if(start_index, content):
        endif_balance = 1
        stop_index = start_index
        while endif_balance != 0:
            stop_index += 1
            if 'if ' in content[stop_index] and 'elif' not in content[stop_index]:
                endif_balance += 1
            elif 'endif' in content[stop_index]:
                endif_balance -= 1
        return stop_index

    # Получает содержимое шаблона разделенное на токены
    @staticmethod
    def get_token_list(splited_content):
        splited_by_tokens = []
        content_index = 0
        while content_index < len(splited_content):
            if '<#' not in splited_content[content_index]:
                splited_by_tokens.append(splited_content[content_index])
                content_index += 1
            else:
                token = splited_content[content_index]
                while '#>' not in splited_content[content_index]:
                    content_index += 1
                    token += splited_content[content_index]
                splited_by_tokens.append(token)
                content_index += 1
        return splited_by_tokens

