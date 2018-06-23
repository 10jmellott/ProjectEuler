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