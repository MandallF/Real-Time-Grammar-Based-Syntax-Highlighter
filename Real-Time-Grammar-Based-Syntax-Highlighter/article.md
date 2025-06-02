# Building a Real-Time Grammar-Based Syntax Highlighter in Python

In this article, I walk through how I created a custom syntax highlighter using Python from scratch — without using any syntax highlighting libraries. This project was part of a programming languages course, and the goal was to build a tool that performs both lexical and syntax analysis in real-time with a working GUI.

## Motivation

Syntax highlighting helps developers read and debug code more easily. Instead of relying on prebuilt libraries, I wanted to understand what goes on under the hood — especially the grammar and lexical analysis parts.

## Lexical Analysis

I implemented a lexer using regular expressions in Python. The lexer recognizes:

- **Keywords**: `if`, `while`
- **Identifiers**: variables like `x`, `counter`
- **Numbers**: any sequence of digits
- **Operators**: `+`, `-`, `*`, `/`, `=`
- **Punctuation**: `(`, `)`, `;`

## Syntax Analysis

A recursive descent parser was implemented for a small grammar with assignment and arithmetic expressions. The parser validates the token stream against a simple CFG.

## Real-Time Highlighting

The GUI is built using `tkinter`. On every key release, the code re-tokenizes the input and applies color-coded tags using the `Text` widget’s tagging mechanism.

## Challenges

- Managing character positions for correct highlighting
- Keeping the highlighter responsive on large inputs
- Making the parser tolerant of incomplete inputs while typing

## Conclusion

This project deepened my understanding of syntax and lexical analysis and gave me a practical appreciation for how code editors highlight syntax in real-time.

## Source Code

Available on GitHub: https://github.com/MandallF/Real-Time-Grammar-Based-Syntax-Highlighter

## Demo Video

Available on YouTube: https://youtu.be/v_c8ZOrIh4g
