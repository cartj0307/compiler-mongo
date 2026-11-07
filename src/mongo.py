import sys

from error_handler import ErrorHandler
from interpreter import Interpreter
from parser import Parser
from scanner import Scanner

interpreter = Interpreter()


def main(argv):
    args = argv[1:]
    if len(args) > 1:
        print("Usage: python src/mongo.py [script.mng]")
        sys.exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_prompt()


def run_file(path):
    with open(path) as source_file:
        run(source_file.read())

    if ErrorHandler.had_error:
        sys.exit(65)
    if ErrorHandler.had_runtime_error:
        sys.exit(70)


def run_prompt():
    print(">>>>> Mongo Interactive Shell <<<<<")
    while True:
        try:
            print("> ", end="", flush=True)
            line = sys.stdin.readline()
            if not line:
                break
            line = line.rstrip("\n")
        except KeyboardInterrupt:
            break
        run(line)
        ErrorHandler.had_error = False


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    statements = parser.parse()

    if ErrorHandler.had_error:
        return

    interpreter.interpret(statements)


if __name__ == "__main__":
    main(sys.argv)