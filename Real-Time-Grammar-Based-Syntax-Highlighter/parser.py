
from tokenizer import tokenize

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == expected_type:
            self.pos += 1
            return True
        return False

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def parse(self):
        while self.pos < len(self.tokens):
            self.statement()

    def statement(self):
        if self.match("KEYWORD"):
            if self.current() and self.current().value == "(":
                self.match("PUNCTUATION")
                self.expression()
                if not self.match("PUNCTUATION"):  # ')'
                    raise ParseError("Missing closing parenthesis")
            self.statement()
        elif self.match("IDENTIFIER"):
            if not self.match("OPERATOR"):  # '='
                raise ParseError("Expected '=' after identifier")
            self.expression()
            if not self.match("PUNCTUATION"):  # ';'
                raise ParseError("Missing semicolon")
        else:
            raise ParseError("Unknown statement")

    def expression(self):
        self.term()
        while self.current() and self.current().value in ('+', '-'):
            self.match("OPERATOR")
            self.term()

    def term(self):
        self.factor()
        while self.current() and self.current().value in ('*', '/'):
            self.match("OPERATOR")
            self.factor()

    def factor(self):
        if self.match("NUMBER") or self.match("IDENTIFIER"):
            return
        elif self.match("PUNCTUATION") and self.current().value == "(":
            self.match("PUNCTUATION")
            self.expression()
            if not self.match("PUNCTUATION"):
                raise ParseError("Missing closing parenthesis")
        else:
            raise ParseError("Invalid factor")
