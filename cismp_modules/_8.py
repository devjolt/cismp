from random import randint
from cismp.utilities import utilities as utl
from ._8_logic import *

questions = {
    
    'operational controls': {
        'question_with_0':'Which of the following describe PLACEHOLDER operational controls?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('procedural', ['checking references for job applicants', 'background checks for job applicants']),
            (['product', 'technical'], ['use of encryption', 'use of passwords', 'use of bitlocker']),
            ('physical', ['ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to {utl.pick_one(['people','assets','data'])}', 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'clean desk policy','deactivating lost devices']),
        ),
        'fillers': (
            ('network', ['never using a device', 'working from home to not catch covid']),
        )
    },
    'disaster recover plan': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'all configuration details should be documented',
            'documentation should be kept up to date',
            'all mission critical aspects should include redundancy',
            'a disaster recovery plan should be kept up to date',
            'all mission critical systems should be monitored',
            'it is preferable to monitor a system for unusual behaviour to avert disaster',
            'monitoring systems should be tested',
            'reaction and response to alerts should be tested',
            'critical data should be backed up',
        ),
        'incorrect': (
            
        ),
    },
    'ISO27001': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'based on managing risk',
            'risk assessment',
            'risk treatment',
            'statement of applicability',
            'help you to identify and correct issues',
            'conduct internal audits',
            'ensure infosec team is confident to perform their roles',
            'reaction and response to alerts should be tested',
            'critical data should be backed up',
        ),
        'incorrect': (
            
        ),
    },

}

"""
risk assessment allows you to prioritise areas more at risk
consider system redundancey


perform assessment

systems monitoring and testing
recovery methods

ISO27001 - standarts for managing an information security management system
framework which helps 
ISMS
latest in sept sept 2013



"""