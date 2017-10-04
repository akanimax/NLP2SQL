# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Settings.
"""

# Generated query language
LANGUAGE = "sparql" # The generated queries will be in sparql format

# NLTK config
NLTK_DATA_PATH = ['/home/animesh/Programming/Research/Access_ReportBot/nltkDATA', '/home/animesh/nltk_data']  # List of paths with NLTK data

# Encoding config
DEFAULT_ENCODING = "utf-8" # the output encoding will be in UTF-8. It has more symbols than the normal ascii

# Sparql config
'''
    The following preamble defines the namespaces and the ontologies to be utilised in the prototype task.
    For interpreting the queries, this preamble always gets printed for every query executed.
'''
SPARQL_PREAMBLE = u"""
PREFIX pronum: <http://www.mobiliya.com/seq2sql-prototype/employee-number/>
PREFIX proatt: <http://www.mobiliya.com/seq2sql-prototype/employee-attribute/>
"""
