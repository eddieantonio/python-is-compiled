# Code for "Python is a compiled language"

This consists of Python code that shows that errors are caught at different stages:
 - decoding
 - scanning (lexical analysis/lexing)
    - this is interleaved with parsing in older versions of Python but occurs
      before parsing with the introduction of the PEG parser in Python 3.9
 - parsing (syntactic analysis)
 - in older versions of Python, there is a stage that checks assignment targets
 - finally, runtime!

This is to demonstrate that Python actually does have compilation stages, and
errors that are directed at certain stages are detected BEFORE runtime. Not
everything is a runtime error in Python!

# License

Code is © 2023 Eddie Antonio Santos. Copying is subject to the terms of the
AGPL-3.0 license -- see `LICENSE` for details.