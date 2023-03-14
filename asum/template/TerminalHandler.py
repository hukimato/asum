from .HandlerInterface import HandlerInterface
from asum.utils.functions import safe_get
import re


class TerminalHandler(HandlerInterface):

    def handle_expression(self, index, stop_index, content):
        preg_search = re.search(r'<#(?P<keys>.+)#>(?P<trash>.*)', content[index])
        list_of_keys = ((preg_search['keys']).strip()).split('.')
        to_change = safe_get(self.data, list_of_keys)
        return index, to_change+preg_search['trash']
