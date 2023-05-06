from .HandlerInterface import HandlerInterface
from asum.utils.functions import safe_get
import re

if_pattern = r"<#if (?P<expression>.*)#>"
elif_pattern = r"<#elif (?P<expression>.*)#>"
INDEX = 0
STATEMENT = 1


class IfHandler(HandlerInterface):

    def handle_expression(self, start_index, stop_index, content):
        if_balancer = 0
        if_statements = [[start_index, content[start_index]]]
        # Находятся пары всех выражений и их тел
        for index, token in enumerate(content[start_index: stop_index]):
            if re.match(if_pattern, token):
                if_balancer += 1
            if re.match(if_pattern, token) and if_balancer == 1:
                if_statements.append([index, token])
            if '<#endif#>' in token:
                if_balancer -= 1
        # Среди пар выбирается первое верное выражение и возвращается соответствующее тело
        for number, statement in enumerate(if_statements):
            groups = re.search(if_pattern, statement[STATEMENT])
            expression = groups['expression']
            if eval(expression):
                from asum.template.Interpreter import Interpreter
                interpreter = Interpreter(content[statement[INDEX]: if_statements[number+1][INDEX]], self.data['data'], self.data['path'])
                return stop_index+1, interpreter.interpret() + '\n'


