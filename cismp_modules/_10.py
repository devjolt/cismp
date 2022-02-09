from random import randint
from cismp.utilities import utilities as utl
from ._10_logic import *

questions = {
    
    'cloud computing': {
        'question_with_0':'Which of the following describes PLACEHOLDER cloud use?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('public', ['on-demand computing services and infrastructure are managed by a third-party provider and shared with multiple organizations', 'on-demand computing services and infrastructure using the public Internet']),
            ('private', ['a cloud computing environment in which all hardware and software resources are dedicated exclusively to, and accessible only by, a single customer']),
            ('community', ['used and paid for a group of users','used by a group of users for shared benefit','suitabile for data exchange']),
            ('hybrid', ['combination of cloud and on-site infrastructure']),
        ),
        'fillers': (
            (),           
        )
   
    },
    
    'cloud computing': {
        'question_with_0':'Which of the following describes PLACEHOLDER as a service?',
        'question_with_1':'Which is the term given used to describe providing PLACEHOLDER?',
        'type':'pairs',
        'course_code':'10',
        'pairs':(
            ('sofware as a service', 'software is accessed online via a subscription','software does not need to be bought and installed on individual computers'),
            ('platform as a service', ['provision of an environment in which to develop code', 'provision of a computing environment and some applications']),
            ('storage as a service', ['storage is provide on a rental basis by a provider']),
            ('security as a service', ['security is provided on a subscription model']),
            ('monitoring as a service', ['monitoring is provided on a subscription model']),
            ('infrastructure as a service', ['cloud computing service that offers essential compute, storage and networking resources on demand']),
        ),
        'fillers': (
            (['network as a service', 'prevention as a service', 'elasticity as a service', 'scalability as a service'], [
                'purchasing software to download and install locally',
                'buying computers with a pre-installed development platform',
                'installing custom-made architecture on site',
                'training staff to provide local security',
                'purchasing monitoring software and hardware and training staff to use them',
                ]),
            
        )
    }
    
}

"""
how is data stores for GDPR
where is data stored
responsibilities 
availability
data retention and destruction
backups/replication
auditing
exit strategy


CSA

cloud control matric and caiq
"""