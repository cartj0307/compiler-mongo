import sys

from token_type import TokenType


class ErrorHandler:
    had_error = False
    had_runtime_error = False

    @staticmethod
    def error(line, message, where=""):
        ErrorHandler.report(line, where, message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        ErrorHandler.had_error = True

    @staticmethod
    def token_error(token, message):
        if token.type == TokenType.EOF:
            ErrorHandler.report(token.line, " at end", message)
        else:
            ErrorHandler.report(token.line, f" at '{token.lexeme}'", message)

    @staticmethod
    def runtime_error(error):
        print(f"{error}\n[line {error.token.line}]", file=sys.stderr)
        ErrorHandler.had_runtime_error = True
