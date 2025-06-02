
import re

# Token tipleri
TOKEN_TYPES = {
    "KEYWORD": r'\b(if|while)\b',
    "NUMBER": r'\b\d+\b',
    "IDENTIFIER": r'\b[a-zA-Z_]\w*\b',
    "OPERATOR": r'[+\-*/=]',
    "PUNCTUATION": r'[();]',
    "WHITESPACE": r'\s+',
    "UNKNOWN": r'.'
}

class Token:
    def __init__(self, type_, value, start, end):
        self.type = type_
        self.value = value
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.type}({self.value})"

def tokenize(text):
    tokens = []
    position = 0
    while position < len(text):
        match = None
        for type_, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(text, position)
            if match:
                if type_ != "WHITESPACE":  # Boşlukları atla
                    token = Token(type_, match.group(), match.start(), match.end())
                    tokens.append(token)
                position = match.end()
                break
        if not match:
            tokens.append(Token("UNKNOWN", text[position], position, position + 1))
            position += 1
    return tokens
