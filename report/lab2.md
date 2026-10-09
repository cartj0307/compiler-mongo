# Lab 2 AST Printer
Name: Mongo
File extension: .mng
Written in Python

## Grammar

expression → literal | unary | binary | grouping ;
literal → NUMBER | STRING | "true" | "false" | "nil" ;
grouping → "(" expression ")" ;
unary → ( "-" | "!" ) expression ;
binary → expression operator expression ;
operator → "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" ;

Literals are numbers, strings, true, false and nil. Unary is - and !. Binary is
== != < <= > >= + - * /.

## Design Choices

Same as chapter 5 in the book but in Python. Grammar is the same as Lox.

wrote expr.py by hand instead of using GenerateAst since you said in the slides it
wasnt required. the classes arent nested in Expr so you can call Binary( ) like the
lab example.

## Files

src/expr.py           expression classes and visitor
src/ast_printer.py    the AST printer
test/lab2/test_ast_printer.py  the tests

## Setup

Nothing to install. Just Python.

## Running

ran it from my root folder.

book example
python src\ast_printer.py

tests
python test\lab2\test_ast_printer.py

## Test 1 book example

Binary(Unary(-, Literal(123)), *, Grouping(Literal(45.67)))

Expected: (* (- 123) (group 45.67))
Actual: (* (- 123) (group 45.67))
matches

## Test 2 literals

every literal type

Binary(Binary(Literal(1), ==, Literal("one")), !=, Binary(Literal(True), ==, Binary(Literal(False), !=, Literal(None))))

Expected: (!= (== 1 one) (== True (!= False nil)))
Actual: (!= (== 1 one) (== True (!= False nil)))
matches

## Test 3 comparison operators

Binary(Binary(Binary(Literal(1), <, Literal(2)), ==, Binary(Literal(3), <=, Literal(4))), !=, Binary(Binary(Literal(5), >, Literal(6)), ==, Binary(Literal(7), >=, Literal(8))))

Expected: (!= (== (< 1 2) (<= 3 4)) (== (> 5 6) (>= 7 8)))
Actual: (!= (== (< 1 2) (<= 3 4)) (== (> 5 6) (>= 7 8)))
matches

## Test 4 math and unary

Unary(!, Grouping(Binary(Binary(Literal(1), +, Literal(2)), -, Binary(Binary(Literal(3), *, Literal(4)), /, Unary(-, Literal(5))))))

Expected: (! (group (- (+ 1 2) (/ (* 3 4) (- 5)))))
Actual: (! (group (- (+ 1 2) (/ (* 3 4) (- 5)))))
matches

## Test 5 slide example

1 - (2 * 3) < 4 == false

Binary(Binary(Binary(Literal(1), -, Grouping(Binary(Literal(2), *, Literal(3)))), <, Literal(4)), ==, Literal(False))

Expected: (== (< (- 1 (group (* 2 3))) 4) False)
Actual: (== (< (- 1 (group (* 2 3))) 4) False)
matches

## Test 6 edge cases

group in a group and minus in a minus

Grouping(Grouping(Unary(-, Unary(-, Literal(1)))))

Expected: (group (group (- (- 1))))
Actual: (group (group (- (- 1))))
matches

literal by itself

Literal(42)

Expected: 42
Actual: 42
matches

empty string and string with a space

Binary(Literal(""), +, Literal("a b"))

Expected: (+  a b)
Actual: (+  a b)
matches