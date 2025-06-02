
import tkinter as tk
from tokenizer import tokenize
from utils import apply_highlighting

class SyntaxHighlighterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Syntax Highlighter")

        self.text = tk.Text(root, wrap="word", font=("Consolas", 14))
        self.text.pack(expand=True, fill="both")
        self.text.bind("<KeyRelease>", self.on_key_release)

        from utils import HIGHLIGHT_COLORS
        for token_type, color in HIGHLIGHT_COLORS.items():
            self.text.tag_configure(token_type, foreground=color)

    def on_key_release(self, event=None):
        content = self.text.get("1.0", "end-1c")
        tokens = tokenize(content)
        apply_highlighting(self.text, tokens)

if __name__ == "__main__":
    root = tk.Tk()
    app = SyntaxHighlighterApp(root)
    root.mainloop()
