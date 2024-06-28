import re

def run_custom_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    # general 
        code = code.replace("'", "")
    # print
        code = code.replace("console.out(", "print(")
        code = code.replace("Console.Out(", "print(")
        code = code.replace("console.Out(", "print(")
        code = code.replace("Console.out(", "print(")
    # import
        code = code.replace("include", "import")
    # if&else
        code = re.sub(r'if\s*\((.*?)\)\s*{', r'if \1:', code)
        code = re.sub(r'}\s*else\s*{', r'else:', code)
    # while & for
    # Ersetze for-Schleifen mit einer pythonischen Syntax
    def for_to_while(match):
        init, condition, increment = match.groups()
        # Ersetze i++ durch i += 1 und i-- durch i -= 1
        increment = re.sub(r'(\w+)\+\+', r'\1 += 1', increment)
        increment = re.sub(r'(\w+)\-\-', r'\1 -= 1', increment)
        return f'{init}\nwhile {condition}:\n    {increment}'
    
    code = re.sub(r'for\s*\((.*?);\s*(.*?);\s*(.*?)\)\s*{', for_to_while, code)
    
    # Ersetze while-Schleifen mit einer pythonischen Syntax
    code = re.sub(r'while\s*\((.*?)\)\s*{', r'while \1:', code)

    code = re.sub(r'}', '', code)

    exec(code)
