# Real-Time Grammar-Based Syntax Highlighter with GUI

This project is a simple real-time syntax highlighter built using Python and Tkinter. It performs lexical and syntax analysis using formal grammars and highlights five different token types in real-time.

## 🎯 Features

- Real-time syntax highlighting
- Highlights 5+ token types:
  - Keywords (`if`, `while`)
  - Identifiers
  - Numbers
  - Operators
  - Punctuation
- GUI-based using Tkinter
- Custom lexer and parser (no syntax highlighting libraries used)

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/syntax-highlighter.git
cd syntax-highlighter

2. Run the Application

python main.py

📁 File Structure
File	            Description
main.py	            Launches the GUI and applies highlighting
tokenizer.py	    Lexical analyzer
parser.py	        Syntax analyzer (recursive descent parser)
utils.py	        Utility functions for coloring text
requirements.txt	Required Python packages (tkinter)
README.md	        This file

📜 Grammar Used
The following is a simplified grammar used in the parser:
stmt      → KEYWORD ( expr ) stmt
          | IDENTIFIER = expr ;
expr      → term ((+|−) term)*
term      → factor ((*|/) factor)*
factor    → NUMBER | IDENTIFIER | ( expr )

📸 Demo
A demonstration video is available at: https://youtu.be/v_c8ZOrIh4g

📜You can access my article from: https://medium.com/@kubilayinanc4/building-a-real-time-grammar-based-syntax-highlighter-in-python-60bea532f134

