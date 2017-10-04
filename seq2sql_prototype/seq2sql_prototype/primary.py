# coding: utf-8

"""
Basic queries for Seq2Sql_prototype quepy.
"""

from refo import Group, Question, Literal
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token

from dsl import *

# Regex for the questions of the type: [What is <firstname's> lastname?]
class WhatIsLastName(QuestionTemplate):
    '''
        Regex for questions like: [What is <target> lastname?]
        ex: What is Heidi lastname? # The questions are with respect to the mock data table
    '''

    regex = Lemma("what") + Lemma("be") + Group(Pos("NNP"), "target") + Token("lastname") + Question(Pos("."))
    print "Question template: What <is / are> <person> lastname?"

    def interpret(self, match):
        employee_name = match.target.tokens

        # reset the HasKeyword relation
        HasKeyword.relation = "proatt:firstname"
        emp_id = HasKeyword(employee_name)

        solution = Lastname(emp_id)

        return solution

# Regex for the questions of the type: [What is <firstname's> lastname?]
class WhatisHiredate(QuestionTemplate):
    '''
        Regex for questions like: [What is <target> hiredate?]
        ex: What is Heidi hiredate? # The questions are with respect to the mock data table
    '''

    regex = Lemma("what") + Lemma("be") + Group(Pos("NNP"), "target") + Token("hiredate") + Question(Pos("."))
    print "Qustion template: What <is / are> <person> hiredate?"

    def interpret(self, match):
        employee_name = match.target.tokens

        # reset the HasKeyword relation
        HasKeyword.relation = "proatt:firstname"
        emp_id = HasKeyword(employee_name)

        solution = Hiredate(emp_id)

        return solution

# Regex for questions of the type: [Who is <firstname>?]
class WhoIs(QuestionTemplate):
    '''
        Regex for questions like: [Who is <target>?]
        ex: Who is Heidi? # The questions are with respect to the mock data table
    '''

    target = Group(Pos("NNP"), "target")
    regex = Lemma("who") + Lemma("be") + target + Question(Pos("."))
    print "Question template: Who <is / are> <person>?"

    # method to interpret this regular expression pattern:
    def interpret(self, match):
        thing = match.target.tokens

        # reset the HasKeyword relation
        HasKeyword.relation = "proatt:firstname"
        pro_id = HasKeyword(thing)

        # find the position of those matched people
        solution = Position(pro_id)

        # return the so constructed pattern:
        return solution
