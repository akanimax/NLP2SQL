# coding: utf-8

"""
Domain specific language for sample_quepy_project quepy.
"""

from quepy.dsl import FixedRelation

class IsDefinedIn(FixedRelation):
    relation = " = "
    reverse = True

