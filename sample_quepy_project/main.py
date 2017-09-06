# coding: utf-8

"""
Main script for sample_quepy_project quepy.
"""

import quepy
sample_quepy_project = quepy.install("sample_quepy_project")


if __name__ == "__main__": 
	target, query, metadata = sample_quepy_project.get_query("what is a blowtorch?")
	print query
