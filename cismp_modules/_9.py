from random import randint
from cismp.utilities import utilities as utl
from ._9_logic import *

questions = {
    
    'operational controls': {
        'question_with_0':'Which of the following describe PLACEHOLDER operational controls?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('digial forensics', ['involves preserving data for use in court', 'applied to data breaches and malware']),
            ('cryptography', ['allows data to be transfered securely', 'involves encryption of a message using a key into ciphertext', 'using a decryption key to convert a message into plain text']),
            ('threat intelligence', ['ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to {utl.pick_one(['people','assets','data'])}', 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'clean desk policy','deactivating lost devices']),
        ),
        'fillers': (
            ('network', ['never using a device', 'working from home to not catch covid']),
        )
    },
    'digital forensics': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'applied to data breaches, malware',
            'involves preserving data for use in court',
            'digital evidence is recognised much more in court',
            'a forensiv science encompassing the recover and preservation of evidence from digital devices',
            '',
        ),
        'incorrect': (
            
        ),
    },

    'cryptography': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'symmetric key systems are faster and simpler',
            'hash functions are used to encrypt',
            'asymmetric key systems ',
            '',
            '',
        ),
        'incorrect': (
            
        ),
    },
    'threat intelligence': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'involves understanding what an adversary can do',
            'increases efficiency of security operations',
            'should be timely, relevant and actionable',
            'it is important to have a global reach',
            'it should be able to integrate with existing tools',
            '',
        ),
        'incorrect': (
            'involves understanding your own capabilities',
            'increases efficiency of security operations',
            'should be timely, relevant and actionable',
            'it is important to have a global reach',
            'it should be able to integrate with existing tools',
            '',
        ),
    },

}