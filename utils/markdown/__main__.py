"""Python Docstring to Markdown
Attempts to parse a python document and resolve a markdown file with unique formatting.  
Assumes Google's Docstring formatting.
"""

import ast
import sys

# Import the local files
from . import DocumentDocstring
from . import GoogleDocstring
from . import HtmlMarkdownBuilder


def parse_file(filename):
    with open(filename) as fd:
        file_contents = fd.read()
    module = ast.parse(file_contents)

    document_summaries = []
    document_classes = []
    document_functions = []
    
    for module in module.body:
        if isinstance(module, ast.Expr) and isinstance(module.value, ast.Str):
            document_summaries.append(DocumentDocstring.DocumentDocstring(module))
        if isinstance(module, ast.ClassDef):
            document_classes.append(GoogleDocstring.GoogleClassDocstring(module))
        if isinstance(module, ast.FunctionDef):
            document_functions.append(GoogleDocstring.GoogleFunctionDocstring(module))

    builder = HtmlMarkdownBuilder.HtmlMarkdownBuilder()

    if document_summaries:
        for summary in document_summaries:
            builder.append('<h1>{}</h1>'.format(summary.title()))
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
            desc = class_def.description()
            if desc:
                builder.append(desc)
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
    """Command line interface. Parses input file and optional output file from the command line in sys.argv index 1 and 2 respectively.
    """
    if len(sys.argv) <= 1:
        print('Invalid arguments')
        print('build_markdown.py input [output]')
    else:
        input_filename = sys.argv[1]
        result = parse_file(input_filename)
        # if nothing went wrong
        if result:
            # if an output file was supplied, write the markdown there
            if len(sys.argv) >= 3:
                output_filename = sys.argv[2]
                with open(output_filename, 'w') as fd:
                    fd.write(result)
            # print the result to output if no file was supplied
            else:
                print(result) 


if __name__ == '__main__':
    # Execute the command line interface parsing
    cli()
