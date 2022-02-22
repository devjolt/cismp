from random import randint
from ._5_logic import *

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

questions = {
    'OSI model layers in order':osi_model_layers_in_order,
    'TCP IP model layers in order':tcp_ip_model_layers_in_order,
    'OSI model': {
        'question_with_0':'Which of the following describe the PLACEHOLDER layer in the OSI model?',
        'question_with_1':'Which layer of the OSI model is the PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('application', ['layer 7','first layer for a sending device', 'final layer for a recieving device', 'seventh layer for a recieving device', 'last layer for a recieving device', 'layer which shows what was used to create a message']),
            ('presentation', ['layer 6','second layer for a sending device', 'sixth layer for a recieving device', 'layer containing information about appearance of data']),
            ('session', ['layer 5','third layer for a sending device', 'fifth layer for a recieving device', 'layer which sets parameters for communication']),
            ('transport', ['layer 4','fourth layer for a sending device', 'fourth layer for a recieving device', 'layer which may use TCP', 'layer which may use UDP']),
            ('network', ['layer 3','fifth layer for a sending device', 'third layer for a recieving device', 'layer which uses IP', 'layer involved in routing', 'layer which routes data to an IP']),
            ('datalink', ['layer 2','sixth layer for a sending device', 'second layer for a recieving device', 'layer which converts IP to a MAC address', 'routes data to a device']),
            ('physical', ['layer 1','final layer for a sending device', 'seventh layer for a sending device','last layer for a sending device', 'first layer for a recieving device', 'layer which may use ethernet cable to get data to a device', 'layer which may use a wireless network to get data to a device']),
        ),
        'fillers': (
            ('multi-factor', ['layer 0', 'layer 1','eight layer for a sending device', 'eigth layer for a recieving device','the first, second and third layer for a sending device', 'the first, second and third layer for a recieving device']),
        )
    },
    'OSI model and IP TCP model': {
        'question_with_0':'Which IP TCP model layer contains the PLACEHOLDER OSI layer?',
        'question_with_1':'',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            (['application','presentation', 'session'], ['application']),
            ('transport', ['transport', 'host to host']),
            (['network','datalink'], ['internet']),
            ('physical', ['network interface']),
        ),
        'fillers': (
            (['firewall','b-router', 'security', 'perimeter'], ['layer 0', 'layer 5']),
        )
    },
    'Network devices': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            'a router is a layer 3 networking device',
            'a router routes network traffic between one IP subnet to another',
            'a router may route traffic from a private to a public network',
            'a switch connects using a physical mac address',
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
            f'a router is a layer {randint(1,2)} networking device',
            f'a router is a layer {randint(4,7)} networking device',
            'a router routes network traffic between one MAC address and another',
            'a router only routes traffic from a public to a private network',
            'a switch connects using IP address',
            'all switches are managed',
            'all switches are unmanaged',
            f'modern firewalls work only at layer {randint(1,2)} of the OSI model',
            'firewalls are only physical',
            'firewalls are only software based',
            'firewalls allow or deny traffic based on AUP',
            'firewall rules are always based on application protocols',
            'firewall rules are always based on port number',
            'firewall rules are always based on content',
            'firewall rules are always based on IP address',
            'firewall rules can not be based on content',
        ),
    },
    'acceptable use policy':{
        'question':'which of the following is PLACEHOLDER part of the process flow on building an acceptable usage policy?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'define the target audience, readership, buisness or organisation',
            'consider the impact of the policy',
            'establish rules, compliance and legal concerns',
            'gather feedback from shareholders and review previous policy',
            'review and update existing policy or set up a new template',
            'decide which devides and types of access should be included',
            'find a template',
            'download a template',
        ),
        'incorrect': (
            f'define punishments',
            f'implement the policy regardless of impact for safety',
            'consider how to enforce the policy on stakeholders',
            'generate your own template to avoid copyright concerns',
            'share template with GDPR',
            'share template with OSEC',
            'obtain template from GDPR',
            f'only desktops located on-site should be included'
        ),
    },
    'acceptable use policy':{
        'question':'which of the following is an example of PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'enabling',
        'negative':'authentication',
        'course_code':'',
        'correct':(
            'specifying user access rights to a folder',
            'specifying user access privileges to part of a system',
            'specifying user access rights to an application',
            'granting access rights to edit a web page',
        ),
        'incorrect': (
            f'using a password to access an application',
            f'using a smartcard to access a server room',
            'requiring a pin number and RFID tag to access data on a USB drive',
            'needing to complete a capcha and enter a secret phrase to access part of a system'
        ),
    },
}

"""
5 proceedural and people security controls

network is two or more computers which are connected in order to share data or communications
CIA is an essential elemnt of any network
AAA is an essential element of any netowork authentication,  authorisation, accountability
threat, risk and vulnerability is an essential elemnt in the design on any network

open systems interconnection model (OSI) - primary model for networks

7 layers

department of defence - TCP IP model


firewall after router
firewall in line
antivirus on each machine
firewall at gateway
"""