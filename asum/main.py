from asum.input.InputModule import InputModule
from asum.generate.GeneratorModule import GeneratorModule
from asum.parse.ParseModule import ParseModule
from asum.prepare.PreparatorModule import PreparatorModule
from asum.template.TemplateModule import TemplateModule
from asum.mediator.Mediator import Mediator

config = {
    'parameters': {
        'specification_file': 'file',
        'template_file': 'file',
        'destination_dir': 'dir'
    },
    'modules': {
        'input_module': InputModule,
        'parse_module': ParseModule,
        'prepare_module': PreparatorModule,
        'template_module': TemplateModule,
        'file_create_module': GeneratorModule,
    },
    'break_on_error': True
}


def main():
    mediator = Mediator(config)
    mediator.run()


if __name__ == 'main.py':
    main()
