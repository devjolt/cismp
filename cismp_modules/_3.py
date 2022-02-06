from random import randint

from ._3_logic import *



questions = {
    'uk_government_data_classifications_in_order':uk_government_data_classifications_in_order,

    'UK government data classifications': {
        'question':'Which of the following statements is PLACEHOLDER a UK government data classification?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('official'),
            ('secret'),
            ('top secret'),
        ),
        'incorrect': (
            'official-secret',
            'official top-secret',
            'classified',
            'unclassified',
            'sensitive',
            'unofficial'
        ),
    },
    

    'Creation of policies': {
        'question':'Regarding the creation of acceptable use policies, which of the following statements is PLACEHOLDER best practise?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('define target audience'),
            ('the policy should be built according to IS027003'),
            ('consider the impact of the policy'),
            ('establish rules, compliance and legal concerns'),
            ('gather feedback from stakeholders'),
            ('consider updating existing policy'),
            ('consider using a template'),
            ('consider being explicit about legal use of a product'),
            ('defensive coding makes sure that only valid data is processed by the system'),
            ('security requirements must be a part the overall requirement specification'),
        ),
        'incorrect': (
            'share the completed policy with GDPR',
            'mark the completed policy as top-secret',
            'always generate an original structure to avoid copyright issues',
            'keep language vague to increase buy-in',
            'do not overcomplicate with different headings and sections',
            'do not refer to the laws of the land - keeping them is implicit',
            'establish penalties for disobeying rules',
        ),
    },
}

"""
'UK government data classifications': {
        'question':'Regarding acceptable use policies, Which of the following statements is PLACEHOLDER?',
        'question_type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            ('a policy should direct behaviour'),
            ('the policy should be built according to IS027003'),
            ('a policy should establish rules, compliance and legal concerns'),
        ),
        'incorrect': (
        ),
    },



policy should direct
intro
scope
policy


upper case or lower case is a standard

Question:
policy should use ISO27003
categories
Which categories should x document have

How would you go about making a policy?

"""

    
    



