#managing risk

from random import randint

from ._2_logic import *

questions = {
    'terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['impact','likelihood'], ['one of the two terms used in combination to define levels of risk']),
            ('risk appetite', ['the amount and type of risk that an organisation is prepared to pursue, retain or take']),
            ('risk tolerance', ['the amount and type of risk that an organisation takes']),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['the MOST IMPORTANT role of senior management in regard to information security'], ['Providing visible and material support for information security within the organisation']),
            (['Privacy'], ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            ),
        
        'fillers': ()
    },
}