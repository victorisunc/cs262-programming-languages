# Underscoring the Magnitude
#
# Focus: Units 1 and 2, Regular Expressions and Lexical Analysis
#
# In this problem you will use regular expressions to specify tokens for a
# part of a new programming language. You must handle seven types of
# tokens:
#
#
#       PLUS            +
#       MINUS           -
#       TIMES           *
#       DIVIDE          /
#       IDENT           my_variable  Caps_Are_OK
#       STRING          'yes'  "also this"
#       NUMBER          123  123_456_789
#
# The last three merit a more detailed explanation.
#
# An IDENT token is a non-empty sequence of lower- and/or upper-case
# letters and underscores, but the first character cannot be an underscore.
# (Letters are a-z and A-Z only.) The value of an IDENT token is the string
# matched.
#
# A STRING token is zero or more of any character surrounded by 'single
# quotes' or "double quotes". In this language, there are no escape
# sequences, so "this\" is a string containing five characters. The value
# of a STRING token is the string matched with the quotes removed.
#
# A NUMBER is a a non-empty sequence of digits (0-9) and/or underscores,
# except that the first character cannot be an underscore. Many real-world
# languages actually support this, to make large number easier to read.
# All NUMBERs in this language are positive integers; negative signs and/or
# periods are not part of NUMBERs. The value of a NUMBER is the integer
# value of its digits with all of the underscores removed: the value of
# "12_34" is 1234 (the integer).
#
# For this problem we do *not* care about line number information. Only the
# types and values of tokens matter. Whitespace characters are ' \t\v\r'
# (and we have already filled them in for you below).
#
# Complete the lexer below.

import ply.lex as lex

tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'IDENT', 'STRING', 'NUMBER')

#####
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_IDENT(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token

def t_STRING(token):
    r'((?:\")([^"]|(\.))*(?:\"))|((?:\')([^\']|(\.))*(?:\'))'
    token.value = token.value[1:-1]
    return token

def t_NUMBER(token):
    r'[\_]*[0-9]+(?:\_*[0-9]*)+'
    if token.value and token.value[0] == "_":
        return ''
    temp = token.value.replace('_', '')
    if temp and temp[0] == '0' and len(temp) > 1:
        temp = temp[1:]
    token.value = int(temp)
    return token
#####

t_ignore = ' \t\v\r'

def t_error(t):
    print "Lexer: unexpected character " + t.value[0]
    t.lexer.skip(1)

# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.
lexer = lex.lex()

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ]
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [(tok.type,tok.value)]
    return result

question1 = " +   -   /   * "
answer1 = [('PLUS', '+'), ('MINUS', '-'), ('DIVIDE', '/'), ('TIMES', '*')]

print test_lexer(question1) == answer1

question2 = """ 'string "nested" \' "inverse 'nested'" """
answer2 = [('STRING', 'string "nested" '), ('STRING', "inverse 'nested'")]
print test_lexer(question2) == answer2

question3 = """ 12_34 5_6_7_8 0______1 1234 """
answer3 = [('NUMBER', 1234), ('NUMBER', 5678), ('NUMBER', 1), ('NUMBER', 1234)]
print test_lexer(question3) == answer3

question4 = """ 0 """
answer4 = [('NUMBER', 0)]
print test_lexer(question4) == answer4

question5 = """ 4_ """
answer5 = [('NUMBER', 4)]
print test_lexer(question5) == answer5

question6 = """ 'he'llo w0rld 33k """
answer6 = [('STRING', 'he'), ('IDENT', 'llo'), ('IDENT', 'w'), ('NUMBER',
0), ('IDENT', 'rld'), ('NUMBER', 33), ('IDENT', 'k')]
print test_lexer(question6) == answer6

question7 = """ 4__ """
answer7 = [('NUMBER', 4)]
print test_lexer(question7) == answer7

question8 = """ _4 4 4_ 4__ 4__4 """
answer8 = [('NUMBER', 4), ('NUMBER', 4), ('NUMBER', 4), ('NUMBER', 44)]
print test_lexer(question8) == answer8

doc_question1='my_variable Caps_Are_OK'
doc_answer1=[('IDENT','my_variable'),('IDENT','Caps_Are_OK')]
print test_lexer(doc_question1)==doc_answer1

doc_question2=r""" 'yes' "also this" """
doc_answer2=[('STRING','yes'),('STRING','also this')]
print test_lexer(doc_question2)==doc_answer2

# identifiers
dit_question1 = 'a ab a_b A AB aB Ab A_b a_B A_B'
dit_answer1 = [('IDENT','a'),('IDENT','ab'),('IDENT','a_b'),('IDENT','A'),('IDENT','AB'),('IDENT','aB'),('IDENT','Ab'),('IDENT','A_b'),('IDENT','a_B'),('IDENT','A_B')]
print test_lexer(dit_question1) == dit_answer1

# strings
dit_question2=r"""'' "" 'a' "b" '"' "'" """
dit_answer2=[('STRING',''),('STRING',''),('STRING','a'),('STRING','b'),('STRING','"'),('STRING',"'")]
print test_lexer(dit_question2)==dit_answer2

dit_question3=r""" "this\" 'this\' 'th\at' "th\at" "\other" '\other'"""
dit_answer3=[('STRING','this\\'),('STRING','this\\'),('STRING','th\\at'),('STRING','th\\at'),('STRING','\\other'),('STRING','\\other')]
print test_lexer(dit_question3)==dit_answer3