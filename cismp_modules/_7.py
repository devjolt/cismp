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
            (['physical', 'environmental'], ['security guards patroling a perimeter','having a reception area','often the most cost effective','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to people','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to assets','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to data', 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'clean desk policy','deactivating lost devices']),
        ),
        'fillers': (
            (['network', 'preventative'], ['never using a device', 'working from home to not catch covid']),
            
        )
    
    },
    'physical security true false': {
        'question':'Regarding physical security, which of the following PLACEHOLDER  good practise?',
        'type':'correct incorrect',
        'positive':'describes',
        'negative':'does not describe',
        'course_code':'',
        'correct':(
            'often the most cost effective',
            'usually the first line of defence',
            'having a properly staffed reception area', 'properly protecting back doors and fire escapes', 'use of locked doors for access to sensitive areas', 'keeping keys in safes', 'securing devices', 'accompanying visitors',
            'marking equipment', 'using a stand-by power generator',
            'having a backup generator',
            'use of transparent ducts to house network cabling'
        ),
        'incorrect': (
            'often the least cost effective',
            'usually one of the last lines of defence',
            'penetration testing software', 'having a strong password policy',
            'having a properly configured firewall', 'biometric authentication',       
        ),
    },
    'preventative, detective and reactive action':{
        'question_with_0':'Which of the following is an example of PLACEHOLDER action?',
        'question_with_1':'PLACEHOLDER is an example of which type of action?', 
        'type':'pairs',
        'course_code':'7',
        'pairs':(
            ('preventative', ['Checking references for job applicants','A staffed reception area','A non-disclosure agreement', 'Locking windows','Being aware of tailgating', 'Keeping desks clear', 'Locking sensitive areas', 'Securely disposing of waste', 'A Clean desk policy', 'Being wary of shoulder surfing', 'Securing devices to a desk', 'Antivirus not allowing malware to be downloaded', 'background checks for job applicants', 'clear desk policy', 'security guards patroling a perimeter']),
            ('detective', ['An intruder alarm', 'Use of smart water to spray people in sesitive areas', 'Antivirus running checks on a system to identify malware']),
            ('reactive', ['An electrified fences','Antivirus removing malware', 'Deactivating lost devices', 'taking legal action']),
            
        ),
        'fillers': (
            (['adaptive', 'network', 'environmental', 'penetrative', 'official', 'legal'], ['never using a device', 'working from home to not catch covid']),
            
        )
    },
}
    
