"""Python Docstring to Markdown
Attempts to parse a python document and resolve a markdown file with unique formatting.  
Assumes Google's Docstring formatting.
"""

import ast
import re
import sys

class HtmlMarkdownBuilder:
    
    def __init__(self):
        self._indentation = 0
        self._lines = []
        self._block = []
    
    def append(self, markdown, div = True):
        if self._indentation > 0 and div:
            self._lines.append('<div markdown="1" style="margin-left: {}px;">'.format(self._indentation * 30))
        self._lines.append(markdown)
        if self._indentation > 0 and div:
            self._lines.append('</div>')
    
    def append_to_block(self, block):
        self._block.append(block)

    def complete_block(self):
        if self._block:
            self.append('\n'.join(self._block))
            self._block = []

    def indent(self):
        self._indentation += 1

    def deindent(self):
        self._indentation -= 1

    def build(self):
        return '\n\n'.join(self._lines)


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

    builder = HtmlMarkdownBuilder()

    if document_summaries:
        for summary in document_summaries:
            builder.append('<h1>{}</h1>'.format(summary.title()))
            builder.append('<h2>Summary</h2>')
            for line in summary.body():
                if line.strip():
                    builder.append_to_block('> {}'.format(line))
            builder.complete_block()

    if document_classes:
        builder.append('<h2>Classes</h2>')
        for class_def in document_classes:
            builder.append_to_block('```python')
            builder.append_to_block('class {}'.format(class_def.name()))
            builder.append_to_block('```')
            builder.complete_block()
            builder.indent()
            ctors = class_def.constructors()
            if ctors:
                builder.append('<h4>Constructors</h4>')
                for ctor in ctors:
                    builder.append_to_block('```python')
                    builder.append_to_block(ctor.name().replace('__init__', class_def.name()))
                    builder.append_to_block('```')
                    builder.complete_block()

                    if ctor.is_valid():
                        builder.indent()
                        builder.append(ctor.short_description())
                        args = ctor.arguments()
                        if args:
                            builder.append('Args:')
                            for arg in args:
                                builder.append_to_block('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                            builder.complete_block()
                        builder.deindent()
            mtds = class_def.methods()
            if mtds:
                builder.append('<h4>Methods</h4>')
                for mtd in mtds:
                    builder.append_to_block('```python')
                    builder.append_to_block('def {}'.format(mtd.name()))
                    builder.append_to_block('```')
                    builder.complete_block()                    
                    if mtd.is_valid():
                        builder.indent()
                        builder.append(mtd.short_description())
                        args = mtd.arguments()
                        if args:
                            builder.append('Args:')
                            for arg in args:
                                builder.append_to_block('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                            builder.complete_block()
                        ret = mtd.return_description()
                        builder.deindent()
            if class_def != document_classes[len(document_classes) - 1]:
                builder.append('------', False)
            builder.deindent()

    if document_functions:
        builder.append('<h2>Intrinsic Functions</h2>')
        for model in document_functions:
            builder.append_to_block('```python')
            builder.append_to_block('def {}'.format(model.name()))
            builder.append_to_block('```')
            builder.complete_block()

            if model.is_valid():
                builder.indent()
                builder.append(model.short_description())
                args = model.arguments()
                if args:
                    builder.append('Args:')
                    for arg in args:
                        builder.append_to_block('* **{}** *{}*: {}'.format(arg.name(), arg.arg_type(), arg.description()))
                    builder.complete_block()
                ret = model.return_description()
                if ret:
                    builder.append('Returns *{}*: {}'.format(ret.return_type(), ret.description()))
                builder.deindent()
            if model != document_functions[len(document_functions) - 1]:
                builder.append('------', False)
    
    return builder.build()


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
