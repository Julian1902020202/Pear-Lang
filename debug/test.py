import re

# Definiere eine Funktion, um den Code lesbarer zu machen
def make_code_readable(code):
    # Ersetze if-Bedingungen mit einer pythonischen Syntax
    code = re.sub(r'if\s*\((.*?)\)\s*{', r'if \1:', code)
    
    # Ersetze else-Blöcke mit einer pythonischen Syntax
    code = re.sub(r'else\s*{', r'else:', code)
    
    return code

# Beispielcode
code = '''
if (condition) {
    // do something
} else {
    // do something else
}
'''

# Wende die Funktion an
readable_code = make_code_readable(code)
print(readable_code)
