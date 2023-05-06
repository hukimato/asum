from .HandlerInterface import HandlerInterface
from asum.utils.functions import safe_get
import re

for_pattern = r"<#for (?P<array>\S+) as (?P<item>\S+)#>"


class ForHandler(HandlerInterface):

    def handle_expression(self, start_index, stop_index, content):
        groups = re.search(for_pattern, content[start_index])
        array_keys = groups['array']
        list_of_keys = (array_keys.strip()).split('.')
        # Получает массив из спецификации
        to_change = safe_get(self.data, list_of_keys)
        array_item_name = groups['item']
        inner_content = ''.join(content[start_index + 1:stop_index])
        result_text = ''
        # Для каждого элемента выполняется интерпретация тела выражения
        for key, val in to_change.items():
            from asum.template.Interpreter import Interpreter
            interpreter = Interpreter(inner_content, self.data['data'], self.data['path'],
                                      {array_item_name: {'key': key, 'value': val}})
            result_text += interpreter.interpret() + '\n'
        return stop_index+1, result_text
