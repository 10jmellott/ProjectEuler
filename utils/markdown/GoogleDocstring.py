import re
import ast

class GoogleDocstringReturn:
    def __init__(self, docstring):
        self._docstring = docstring
        self._reg = re.match(r'(.+): (.+)', docstring.strip())
    
    def return_type(self):
        return self._reg.group(1)

    def description(self):
        return self._reg.group(2)


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
        desc = []
        split = self._docstring.split('\n')
        for i in range(len(split)):
            if 'Returns:' in split[i] or 'Args:' in split[i]:
                break
            desc.append(split[i])
        return '\n'.join(desc)

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

    def description(self):
        return self._docstring

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
