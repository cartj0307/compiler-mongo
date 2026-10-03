import sys


class ErrorHandler:
    had_error = False

    @staticmethod
    def error(line, message, where=""):
        ErrorHandler.report(line, where, message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        ErrorHandler.had_error = True
