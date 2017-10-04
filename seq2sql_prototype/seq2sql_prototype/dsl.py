# coding: utf-8

"""
Domain specific language for Seq2Sql_prototype quepy.
"""

from quepy.dsl import FixedRelation, FixedDataRelation, FixedType

# class defining the relation to obtain the position:
class Position(FixedRelation):
    relation = "proatt:position"
    reverse = True

# class defining the relation to obtain the lastname
class Lastname(FixedRelation):
    relation = "proatt:lastname"
    reverse = True

class Hiredate(FixedRelation):
    relation = "proatt:hiredate"
    reverse = True
