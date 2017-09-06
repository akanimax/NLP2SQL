# coding: utf-8

"""
Basic queries for sample_quepy_project quepy.

This module simply presents a semantic representation of the input natural language sentences
"""

# regex stuff required for nlp. 
from refo import Group, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate

from dsl import *


# regex template for the "What is ... " type of question.
class WhatIs(QuestionTemplate):
    """
    Regex for questions like "What is ..."
    Ex: "What is a car"
    """

    target = Question(Pos("DT")) + Group(Pos("NN"), "target")
    regex = Lemma("what") + Lemma("be") + target + Question(Pos("."))

    def interpret(self, match):
	""" Define the interpret method by using the dsl module to convert this into a sql query. """

	thing = match.target.tokens
	target = HasKeyword(thing)
	definition = IsDefinedIn(target)
	return definition
