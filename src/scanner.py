from error_handler import ErrorHandler


class Scanner:
    def __init__(self, source):
        self.source = source
        self.line = 1

    def scan_tokens(self):
        ErrorHandler.error(self.line, "Scanner Not Implemented")
        return []