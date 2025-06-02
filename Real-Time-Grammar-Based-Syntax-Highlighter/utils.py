
HIGHLIGHT_COLORS = {
    "KEYWORD": "red",
    "NUMBER": "blue",
    "IDENTIFIER": "purple",
    "OPERATOR": "dark red",
    "PUNCTUATION": "black",
    "UNKNOWN": "gray"
}

def apply_highlighting(text_widget, tokens):
    for tag in HIGHLIGHT_COLORS:
        text_widget.tag_remove(tag, "1.0", "end")

    for token in tokens:
        start_index = f"1.0 + {token.start} chars"
        end_index = f"1.0 + {token.end} chars"
        if token.type in HIGHLIGHT_COLORS:
            text_widget.tag_add(token.type, start_index, end_index)
