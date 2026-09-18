import sys

from error_handler import ErrorHandler
from scanner import Scanner


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


def run_prompt():
    print(">>>>> Mongo Interactive Shell <<<<<")
    while True:
        try:
            print("> ", end="")
            line = sys.stdin.readline()
            if not line:
                break
            line = line.rstrip("\n")
        except KeyboardInterrupt:
            break
        run(line)
        ErrorHandler.had_error = False


def run(source):
    print(source)
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)


if __name__ == "__main__":
    main(sys.argv)