"""Python Docstring to Markdown
Attempts to parse a python document and resolve a markdown file with unique formatting.  
Assumes Google's Docstring formatting.
"""

import ast
import re
import sys

class DocumentDocstring:
    def __init__(self, expression):
        self._exp = expression
        self._docstring = expression.value.s


    def title(self):
        return self._docstring.split('\n')[0]


    def body(self):
        b = []
        skipped_lines = 1
        for s in self._docstring.split('\n'):
            if skipped_lines == 0:
                b.append(s)
            else:
                skipped_lines = skipped_lines - 1
        return b


class GoogleDocstringArgument:
    def __init__(self, docstring):
        self._docstring = docstring
        self._reg = re.match(r'(.+) \((.+)\): (.+)', docstring.strip())


    def name(self):
        return self._reg.group(1)
    

    def arg_type(self):
        return self._reg.group(2)


    def description(self):
        return self._reg.group(3)


class GoogleDocstringReturn:
    def __init__(self, docstring):
        self._docstring = docstring
        self._reg = re.match(r'(.+): (.+)', docstring.strip())
    

    def return_type(self):
        return self._reg.group(1)


    def description(self):
        return self._reg.group(2)


class GoogleFunctionDocstring:
    def __init__(self, function_def):
        self._def = function_def
        self._docstring = ast.get_docstring(function_def)


    def is_valid(self):
        return self._docstring != None


    def name(self):
        args = []
        for arg in self._def.args.args:
            if arg.arg != 'self':
                args.append(arg.arg)
        return '{}({})'.format(self._def.name, ', '.join(args))


    def short_description(self):
        return self._docstring.split('\n')[0]


    def arguments(self):
        args = []
        is_argument_section = False
        for s in self._docstring.split('\n'):
            if is_argument_section:
                if s.strip():
                    args.append(s)
                else:
                    is_argument_section = False
            elif s.startswith('Args:'):
                is_argument_section = True
        conv_args = []
        for arg in args:
            conv_args.append(GoogleDocstringArgument(arg))
        return conv_args


    def return_description(self):
        is_return_section = False
        for s in self._docstring.split('\n'):
            if is_return_section:
                if s.strip():
                    return GoogleDocstringReturn(s)
                else:
                    is_return_section = False
            elif s.startswith('Returns:'):
                is_return_section = True

class GoogleClassDocstring:
    def __init__(self, class_def):
        self._def = class_def
        self._docstring = ast.get_docstring(class_def)


    def name(self):
        return self._def.name


    def constructors(self):
        ctors = []
        for module in self._def.body:
            if isinstance(module, ast.FunctionDef):
                if module.name == '__init__':
                    ctors.append(GoogleFunctionDocstring(module))
        return ctors


    def methods(self):
        mtds = []
        for module in self._def.body:
            if isinstance(module, ast.FunctionDef):
                if module.name != '__init__' and module.name.startswith('_') == False:
                    mtds.append(GoogleFunctionDocstring(module))
        return mtds

def parse_file(filename):
    with open(filename) as fd:
        file_contents = fd.read()
    module = ast.parse(file_contents)

    document_summaries = []
    document_classes = []
    document_functions = []

    for module in module.body:
        if isinstance(module, ast.Expr):
            document_summaries.append(DocumentDocstring(module))
        if isinstance(module, ast.ClassDef):
            document_classes.append(GoogleClassDocstring(module))
        if isinstance(module, ast.FunctionDef):
            document_functions.append(GoogleFunctionDocstring(module))

    result = []

    if document_summaries:
        for summary in document_summaries:
            result.append('<h1>{}</h1>'.format(summary.title()))
            result.append('')
            result.append('<h2>Summary</h2>')
            result.append('')
            result.append('<div markdown="1" style="margin-left: 30px;">')
            result.append('')
            for line in summary.body():
                if line.strip():
                    result.append('> {}'.format(line))
            result.append('')
            result.append('</div>')
    
    result.append('')
    result.append('')

    if document_classes:
        result.append('')
        result.append('<h2>Classes</h2>')
        result.append('')
        result.append('<div markdown="1" style="margin-left: 30px;">')
        result.append('')
        for class_def in document_classes:
            result.append('```python')
            result.append('class {}'.format(class_def.name()))
            result.append('```')
            result.append('')
            result.append('<div markdown="1" style="margin-left: 30px;">')
            result.append('')
            ctors = class_def.constructors()
            if ctors:
                result.append('<h3>Constructors</h3>')
                for ctor in ctors:
                    result.append('')
                    result.append('```python')
                    result.append(ctor.name().replace('__init__', class_def.name()))
                    result.append('```')
                    if ctor.is_valid():
                        result.append('')
                        result.append('<div markdown="1" style="margin-left: 30px;">')
                        result.append('')
                        result.append(ctor.short_description())
                        result.append('')
                        args = ctor.arguments()
                        if args:
                            result.append('Args:')
                            result.append('')
                            for arg in args:
                                result.append('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                        result.append('')
                        result.append('</div>')
            mtds = class_def.methods()
            if mtds:
                result.append('')
                result.append('<h3>Methods</h3>')
                for mtd in mtds:
                    result.append('')
                    result.append('```python')
                    result.append('def {}'.format(mtd.name()))
                    result.append('```')
                    if mtd.is_valid():
                        result.append('')
                        result.append('<div markdown="1" style="margin-left: 30px;">')
                        result.append('')
                        result.append(mtd.short_description())
                        result.append('')
                        args = mtd.arguments()
                        if args:
                            result.append('Args:')
                            result.append('')
                            for arg in args:
                                result.append('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                        ret = mtd.return_description()
                        result.append('')
                        result.append('</div>')
            result.append('')
            result.append('</div>')
            if class_def != document_classes[len(document_classes) - 1]:
                result.append('')
                result.append('------')
            result.append('')
        result.append('')
        result.append('</div>')

    result.append('')
    result.append('')

    if document_functions:
        result.append('')
        result.append('<h2>Intrinsic Functions</h2>')
        for model in document_functions:
            result.append('```python')
            result.append('def {}'.format(model.name()))
            result.append('```')

            if model.is_valid():
                result.append('')
                result.append('<div markdown="1" style="margin-left: 30px;">')
                result.append('')
                result.append(model.short_description())
                result.append('')
                args = model.arguments()
                if args:
                    result.append('Args:')
                    result.append('')
                    for arg in args:
                        result.append('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                ret = model.return_description()
                if ret:
                    result.append('')
                    result.append('Returns *{}*: {}'.format(ret.return_type(), ret.description()))
                result.append('')
                result.append('</div>')
            if model != document_functions[len(document_functions) - 1]:
                result.append('')
                result.append('------')
            result.append('')
    
    return '\n'.join(result)


def cli():
    if len(sys.argv) <= 1:
        print('Invalid arguments')
        print('build_markdown.py input [output]')
    else:
        input_filename = sys.argv[1]
        result = parse_file(input_filename)
        if len(sys.argv) >= 3:
            output_filename = sys.argv[2]
            with open(output_filename, 'w') as fd:
                fd.write(result)
        else:
            print(result) 


if __name__ == '__main__':
    cli()
