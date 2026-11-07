# Lab 4 Statements
Name: Mongo
File extension: .mng
Written in Python

## Grammar

program → statement* EOF ;
statement → exprStmt | printStmt ;
exprStmt → expression ";" ;
printStmt → "print" expression ";" ;

expression → equality ;
equality → comparison ( ( "!=" | "==" ) comparison )* ;
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term → factor ( ( "-" | "+" ) factor )* ;
factor → unary ( ( "/" | "*" ) unary )* ;
unary → ( "!" | "-" ) unary | primary ;
primary → NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")" ;

expression grammar is the same as lab 3. the statement rules are new.

## Design Choices

Same as chapter 7 and chapter 8.1 in the book but in Python.

runtime errors print the message and the line like the book and exit with 70.

stringify prints nil, true and false instead of the python None, True and False and
drops the .0 off whole numbers.

## Files

src/interpreter.py    the interpreter, runs expressions and statements
src/stmt.py           statement classes and visitor
src/runtime_error.py  runtime error class
src/parser.py         now parses statements and does panic mode recovery
src/mongo.py          entry point now runs the interpreter instead of the AST printer
src/error_handler.py  added runtime_error
src/scanner.py, src/token.py, src/token_type.py, src/expr.py, src/ast_printer.py  from labs 1 to 3
test/lab4/            the tests

## Setup

Nothing to install. Just Python.

## Running

ran it from my root folder.

Interactive mode
python src\mongo.py

Source file mode
python src\mongo.py test\lab4\syntax_errors.mng

tests
python src\mongo.py test\lab4\syntax_errors.mng
python src\mongo.py test\lab4\statements.mng

## Test 1 syntax_errors.mng

syntax errors and panic mode recovery

"one"
true;
print 2 +

Expected
[line 2] Error at 'true': Expect ';' after expression.
[line 3] Error at end: Expect expression.

Actual
[line 2] Error at 'true': Expect ';' after expression.
[line 3] Error at end: Expect expression.

matches

## Test 2 statements.mng

expression statement and print statements

4 + 2;
print "one";
print true;
print 1 + 2;
print nil;

Expected
one
true
3
nil

Actual
one
true
3
nil

matches