import sys
from interpreter import translate_custom_file, execute_translated_code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py main.py <filename.p>")
        sys.exit(1)

    filename = sys.argv[1]
    translated_code = translate_custom_file(filename)
    execute_translated_code(translated_code)

