class Tokens:
    def __init__(self):
        self.tokens = {
            "QOUTATION_MARK": '"'
        }

    def __getattr__(self, name):
        if name in self.tokens:
            return self.tokens[name]
        else:
            raise AttributeError(f"'Tokens' object has no attribute '{name}'")

tokens = Tokens()

class STokens:
    def __init__(self):
        self.tokens = {
            "PRINT": "print(",
            "IMPORT": "import"
        }

    def __getattr__(self, name):
        if name in self.tokens:
            return self.tokens[name]
        else:
            raise AttributeError(f"'STokens' object has no attribute '{name}'")

Stokens = STokens()
