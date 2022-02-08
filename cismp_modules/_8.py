from random import randint
from cismp.utilities import utilities as utl
from ._8_logic import *



questions = {
    'true and false business recovery plan':{
    'question':'Regarding disaster recovery and business continuity management, which of the following is PLACEHOLDER?',
    'positive':'correct',
        'negative':'incorrect',
        'course_code':'8',
        'correct':(
            'business recovery plans are best developed in the way which suits the organisation',
            'disaster recovery plans are best developed in the way which suits the organisation', 
            'ensuring that a risk assessment has been completed effectively is essential',
            'considering the consequences of events is more important than comprehensively considering all possible events',
            'it is good practice to involve a number of key staff members in planning',
            'documentation is a vital part of DR',
            'involving professionals in testing documentation is recommended',
        ),
        'incorrect':(
            'business recovery plans are best developed following a strict framework',
            'disaster recovery plans are best developed following a strict framework', 
            'a risk assessment can be completing following completion of the BRP',
            'a risk assessment can be completing following completion of the DR plan',
            'a risk assessment can be completing following completion of the BRP and DR plan',
            'comprehensively considering all possible events is essential',
            'it is good practice for company leaders to make executive decision on the content of the BRP',
            'it is good practice for company leaders to make executive decision on the content of the DR plan'
        )
        
    },


    'Business continuity plan, disaster recovery': {
        'question_with_0':'Which of the following describes a PLACEHOLDER?',
        'question_with_1':'What is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            (['BCP','business continuity plan'], ['thinking through events which might adversely impact a business, and writing down a method of continuing','plan to maintain continuity of business operations', 'plan to enable a business to keep running despite problems','planning for relatively small changes in normal operations']),
            (['DR', 'disaster recovery'], 'continuing to operate and attempting to get back to normal'),
            (['BIA','business impact analysis'], ['considering the implications of possible threats to a business', 'derived from a risk assessment']),
        ),
        'fillers': (
            (['CIA','BCS','ISO', 'GDPR', 'NCSC', 'BLA'], ['security patrolling a sensitive building', 'working from home to not catch covid', 'providing fruit for employees', 'planning to clse the office on Sundays', 'enforced vacations']),
        )
    },
    'resilience and redundancy': {
        'question_with_0':'Which of the following is an example of PLACEHOLDER?',
        'question_with_1':'Which of the following describes PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            ('warm standby', ['a duplicate system requiring some configuration','a duplicate system which may have some data pre-loaded','a duplicate system which may have data loaded to a known backup point']),
            ('cold standby', ['a duplicate sytem requiring configuration from scratch', 'a duplicate system which may be in a remote location']),
            ('hot standby', ['the most costly form of duplicate system','a duplicate system which is fully loaded with with up to date data', 'a duplicate system which is fully configured', 'a duplicate system which can be brought into service quickly']),
            ('synchronous replication', 'duplicating a system, waiting for acknowledgement of reciept'),
            ('asynchronous replication', 'duplicating a system, without for acknowledgement of reciept'),
        ),
        'fillers': (
            (['steady standby','amorphous replication'], ['duplicating your operating system in a partition', 'keeping your system on all the time']),
        )       
    },
    'cold, warm hot and high availability': {        
        'type':'correct incorrect',
        'question':'Which of the following is an example of PLACEHOLDER?',
        'positive':'resilience',
        'negative':'redundancy',
        'course_code':'8',
        'correct':(
            'ensuring that there are no single points of failure',
            'ensuring that failure in one part of a system cannot bring everything to a standstill',
            'using multiple webservers with load balancing',
            'cross-training employees in vital skillsets', 
        ),
        'incorrect':(
            'having a duplicate system on cold standby',
            'having a duplicate system on warm standby',
            'having a duplicate system on hot standby',
            'having a high availability duplicate system',
        )        
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


"""