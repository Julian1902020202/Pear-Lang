import re

from tokens import tokens, Stokens

def translate_custom_file(filename):
    with open(filename, 'r') as file:
        code = file.read()

    # Sicherstellen, dass nur Pear Code und keine Python-Syntax vorhanden ist
    if re.search(r'\bimport\b|\bexec\b|\beval\b|\bdef\b|\bprint\b|\belif\b', code):
        raise ValueError("Python code is not allowed in .p files")

    # Pear Code zu Python Code übersetzen
    code = code.replace("'", tokens.QOUTATION_MARK)
    code = code.replace("console.out(", Stokens.PRINT)
    code = code.replace("Console.Out(", Stokens.PRINT)
    code = code.replace("console.Out(", Stokens.PRINT)
    code = code.replace("Console.out(", Stokens.PRINT)
    code = code.replace("include", Stokens.IMPORT)
    code = re.sub(r'if\s*\((.*?)\)\s*{', r'if \1:', code)
    code = re.sub(r'}\s*else\s*{', r'else:', code)
    
    def for_to_while(match):
        init, condition, increment = match.groups()
        increment = re.sub(r'(\w+)\+\+', r'\1 += 1', increment)
        increment = re.sub(r'(\w+)\-\-', r'\1 -= 1', increment)
        return f'{init}\nwhile {condition}:\n    # Loop body\n    {increment}'

    code = re.sub(r'for\s*\((.*?);\s*(.*?);\s*(.*?)\)\s*{', for_to_while, code)
    code = re.sub(r'while\s*\((.*?)\)\s*{', r'while \1:', code)
    code = re.sub(r'}', '', code)

    return code

def execute_translated_code(code):
    exec(code)
