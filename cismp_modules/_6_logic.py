from random import randint, shuffle

from cismp.utilities import utilities as utl


def rings_of_security():
    num_choices=4
    question_text='What are the rings of security from PLACEHOLDER?'
    ascending_order, descending_order='innermost to outermost', 'outermost to innermost'
    correct_list=['kernel','device drivers','applications']#least to most default
    fillers=['physical','datalink','session','presentation','secret','classified', 'queue', 'MAC', 'SOHO', 'NFC', 'bluetooth']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)