#!/usr/bin/env python3

""" Check if valid python code was entered """

import ast
import sys

def is_valid_python(code):
   try:
       ast.parse(code)
   except SyntaxError:
       return False
   return True

if __name__ == "__main__":
    python_command = " ".join(sys.argv[1:])

    if (is_valid_python(python_command)): 
        print("Valid python, well done Gazbock.")
        print("The result is:") 
        exec(python_command)
    else:
        print("Not valid python, DU GAZBOCK!")
