# Lab 5 Variables
Name: Mongo
File extension: .mng
Written in Python

## Grammar

program --- declaration* EOF ;
declaration --- varDecl | statement ;
varDecl --- "var" IDENTIFIER ( "=" expression )? ";" ;
statement --- exprStmt | printStmt | block ;
exprStmt --- expression ";" ;
printStmt --- "print" expression ";" ;
block --- "{" declaration* "}" ;

expression --- assignment ;
assignment --- IDENTIFIER "=" assignment | equality ;
equality --- comparison ( ( "!=" | "==" ) comparison )* ;
comparison --- term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term --- factor ( ( "-" | "+" ) factor )* ;
factor --- unary ( ( "/" | "*" ) unary )* ;
unary --- ( "!" | "-" ) unary | primary ;
primary --- NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")" | IDENTIFIER ;

## Design Choices

Same as chapter 8 in the book but in Python.

Variable access before declaration
its a runtime error, not a syntax error. it gives Undefined variable 'a'. with the line
and exits with 70. assigning to a variable that was never declared is the same error.

Missing initializer in the declaration
allowed. var a; makes a and sets it to nil.

Redeclaration
allowed. var a = 1; then var a = 2; just replaces the old value. declaring a with the
same name inside a block makes a new a that shadows the outer one.

assignment is an expression so print a = 3; assigns 3 and prints 3.

## Files

src/environment.py    environment class, define get and assign, enclosing for scope
src/expr.py           added Assign and Variable
src/stmt.py           added Block and Var
src/parser.py         parses var declarations, assignment, variables and blocks
src/interpreter.py    runs var, assign, variable and blocks with the environment
src/ast_printer.py    added assign and variable so it still works
src/scanner.py, src/token.py, src/token_type.py, src/error_handler.py, src/runtime_error.py, src/mongo.py  from labs 1 to 4
test/lab5/            the tests

## Setup

Nothing to install. Just Python.

## Running

ran it from my root folder.

Interactive mode
python src\mongo.py

Source file mode
python src\mongo.py test\lab5\variables.mng

tests
python src\mongo.py test\lab5\variables.mng
python src\mongo.py test\lab5\scope.mng
python src\mongo.py test\lab5\missing_brace.mng
python src\mongo.py test\lab5\extra_brace.mng
python src\mongo.py test\lab5\invalid_assignment.mng
python src\mongo.py test\lab5\var_syntax_errors.mng
python src\mongo.py test\lab5\undefined_variable.mng
python src\mongo.py test\lab5\undefined_assignment.mng

## Test 1 variables.mng

declaration, access and assignment

var a = 1;
var b = 2;
print a + b;
var c;
print c;
c = "assigned";
print c;
print a = 3;
print a;
var a = "redeclared";
print a;

Expected
3
nil
assigned
3
3
redeclared

Actual
3
nil
assigned
3
3
redeclared

matches

## Test 2 scope.mng

the code from the book

var a = "global a";
var b = "global b";
var c = "global c";
{
  var a = "outer a";
  var b = "outer b";
  {
    var a = "inner a";
    print a;
    print b;
    print c;
  }
  print a;
  print b;
  print c;
}
print a;
print b;
print c;

Expected
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c

Actual
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c

matches

each block makes a new environment that points to the one around it. getting a
variable looks in the current environment first and if its not there it goes out to
the enclosing one until it finds it.

in the inner block a is declared there so it prints inner a. b isnt in the inner block
so it goes out one and finds outer b. c isnt in either block so it goes out to global c.

when the inner block ends its environment is gone so the outer block prints outer a,
outer b and global c again.

when the outer block ends the global ones were never changed so it prints global a,
global b and global c.

## Test 3 missing_brace.mng

{
  var a = 1;
  print a;

Expected: [line 3] Error at end: Expect '}' after block.
Actual: [line 3] Error at end: Expect '}' after block.
matches

the block never closes so it hits the end looking for the }.

## Test 4 extra_brace.mng

var a = 1;
}
print a;

Expected: [line 2] Error at '}': Expect expression.
Actual: [line 2] Error at '}': Expect expression.
matches

there is no block open so the } isnt the start of any statement.

## Test 5 invalid_assignment.mng

var a = 1;
var b = 2;
var c = 3;
a + b = c;

Expected: [line 4] Error at '=': Invalid assignment target.
Actual: [line 4] Error at '=': Invalid assignment target.
matches

a + b isnt a variable so it cant be assigned to.

## Test 6 var_syntax_errors.mng

var = 1;
var a = 1
print a;

Expected
[line 1] Error at '=': Expect variable name.
[line 3] Error at 'print': Expect ';' after variable declaration.

Actual
[line 1] Error at '=': Expect variable name.
[line 3] Error at 'print': Expect ';' after variable declaration.

matches

no name after var on line 1. no ; after the declaration on line 2 so it errors on the
print. it synchronizes after the first one so both get reported.

## Test 7 undefined_variable.mng

print a;

Expected
Undefined variable 'a'.
[line 1]

Actual
Undefined variable 'a'.
[line 1]

matches

a is accessed before its declared.

## Test 8 undefined_assignment.mng

a = 1;

Expected
Undefined variable 'a'.
[line 1]

Actual
Undefined variable 'a'.
[line 1]

matches

assignment cant make a new variable, it has to be declared with var first.
