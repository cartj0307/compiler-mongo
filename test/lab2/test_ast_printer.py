import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from expr import Binary, Grouping, Literal, Unary
from token import Token
from token_type import TokenType
from ast_printer import AstPrinter

# Test 1 book example
expression = Binary(
    Unary(
        Token(TokenType.MINUS, "-", None, 1),
        Literal(123)),
    Token(TokenType.STAR, "*", None, 1),
    Grouping(
        Literal(45.67)))

print(AstPrinter().print(expression))

# Test 2 literals
expression = Binary(
    Binary(
        Literal(1),
        Token(TokenType.EQUAL_EQUAL, "==", None, 1),
        Literal("one")),
    Token(TokenType.BANG_EQUAL, "!=", None, 1),
    Binary(
        Literal(True),
        Token(TokenType.EQUAL_EQUAL, "==", None, 1),
        Binary(
            Literal(False),
            Token(TokenType.BANG_EQUAL, "!=", None, 1),
            Literal(None))))

print(AstPrinter().print(expression))

# Test 3 comparison operators
expression = Binary(
    Binary(
        Binary(
            Literal(1),
            Token(TokenType.LESS, "<", None, 1),
            Literal(2)),
        Token(TokenType.EQUAL_EQUAL, "==", None, 1),
        Binary(
            Literal(3),
            Token(TokenType.LESS_EQUAL, "<=", None, 1),
            Literal(4))),
    Token(TokenType.BANG_EQUAL, "!=", None, 1),
    Binary(
        Binary(
            Literal(5),
            Token(TokenType.GREATER, ">", None, 1),
            Literal(6)),
        Token(TokenType.EQUAL_EQUAL, "==", None, 1),
        Binary(
            Literal(7),
            Token(TokenType.GREATER_EQUAL, ">=", None, 1),
            Literal(8))))

print(AstPrinter().print(expression))

# Test 4 math and unary
expression = Unary(
    Token(TokenType.BANG, "!", None, 1),
    Grouping(
        Binary(
            Binary(
                Literal(1),
                Token(TokenType.PLUS, "+", None, 1),
                Literal(2)),
            Token(TokenType.MINUS, "-", None, 1),
            Binary(
                Binary(
                    Literal(3),
                    Token(TokenType.STAR, "*", None, 1),
                    Literal(4)),
                Token(TokenType.SLASH, "/", None, 1),
                Unary(
                    Token(TokenType.MINUS, "-", None, 1),
                    Literal(5))))))

print(AstPrinter().print(expression))

# Test 5 slide example
expression = Binary(
    Binary(
        Binary(
            Literal(1),
            Token(TokenType.MINUS, "-", None, 1),
            Grouping(
                Binary(
                    Literal(2),
                    Token(TokenType.STAR, "*", None, 1),
                    Literal(3)))),
        Token(TokenType.LESS, "<", None, 1),
        Literal(4)),
    Token(TokenType.EQUAL_EQUAL, "==", None, 1),
    Literal(False))

print(AstPrinter().print(expression))

# Test 6 edge cases
expression = Grouping(
    Grouping(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Unary(
                Token(TokenType.MINUS, "-", None, 1),
                Literal(1)))))

print(AstPrinter().print(expression))

expression = Literal(42)

print(AstPrinter().print(expression))

expression = Binary(
    Literal(""),
    Token(TokenType.PLUS, "+", None, 1),
    Literal("a b"))

print(AstPrinter().print(expression))