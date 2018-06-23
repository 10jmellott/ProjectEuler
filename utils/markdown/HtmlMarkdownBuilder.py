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