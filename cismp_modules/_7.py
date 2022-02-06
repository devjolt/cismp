from random import randint
from cismp.utilities import utilities as utl
from ._7_logic import *

questions = {
    
    'operational controls': {
        'question_with_0':'Which of the following describe PLACEHOLDER operational controls?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('procedural', ['checking references for job applicants', 'background checks for job applicants', 'clear desk policy']),
            (['product', 'technical'], ['use of encryption', 'use of passwords', 'use of bitlocker','Writing random data to the same data file for at least seven cycles']),
            (['physical', 'environmental'], ['security guards patroling a perimeter','having a reception area','often the most cost effective','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to {utl.pick_one(['people','assets','data'])}', 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'clean desk policy','deactivating lost devices']),
            
        ),
        'fillers': (
            (['network', 'preventative'], ['never using a device', 'working from home to not catch covid']),
            
        )
    },
    'operational controls true false': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            'physical and environmental controls are often the most cost effective',
            
        ),
        'incorrect': (
            
        ),
    },
    'physical security true false': {
        'question':'Regarding physical security, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            'often the most cost effective',
            'usually the first line of defence',
            f'an example is {utl.pick_one(['having a properly staffed reception area', 'properly protecting back doors and fire escapes', 'use of locked doors for access to sensitive areas', 'keeping keys in safes', 'securing devices', 'accompanying visitors'])}',
            f'an example is {utl.pick_one(['marking equipment', 'using a stand-by power generator', ''])}',
            
            'a switch may be managed or unmanaged',
            'modern swithces may also incorporate a router',
            'modern firewalls work at multiple layers of the OSI model',
            'firewalls may be physical',
            'firewalls may be software based',
            'firewalls allow or deny traffic based on rules and access control lists',
            'firewall rules may be based on application protocols',
            'firewall rules may be based on port number',
            'firewall rules may be based on content',
            'firewall rules may be based on IP address',
        ),
        'incorrect': (
            
        ),
    },

}