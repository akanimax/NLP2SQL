# coding: utf-8

"""
Main script for Seq2Sql_prototype quepy.
"""

import signal
import quepy
seq2sql_prototype = quepy.install("seq2sql_prototype")

done = False # The commandline tool is running
def signal_handler(signum, frame):
    print "\n\t\t\t!!! Thank you for using the application !!!\n\n"
    exit()


if __name__ == "__main__":
    # start the application from here:
    print "\n\t\t\t!!! Welcome To the NL2SPARQL Prototype !!!\n"

    # define the signal to exit the program.
    signal.signal(signal.SIGINT, signal_handler)

    while not done:
        # keep looping until you are done:
        nl_question = str(raw_input("\n\nask>>>> "))

        target, query, metadata = seq2sql_prototype.get_query(nl_question)

        if query != None:
            print "\nQuery Formed>>> " + query

        else:
            print "\nException>> Question out of context, query cannot be formed\n"
