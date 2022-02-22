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
            ('seperation of duties', 'the principle that no user should be given enough privileges to misuse the system on their own'),
            ('assurance', 'the amount of confidence that an organisation has that its controls satisfy necessary security requirements'),
            ('non-repudiation', ['the ability to prove that an event occurred']), 
            ('fail secure', ['disconnecting a system if an event occurs']),
            (['impact','likelihood'], ['one of the two terms used in combination to define levels of risk']),
            ('risk appetite', ['the amount and type of risk that an organisation is prepared to pursue, retain or take']),
            ('risk tolerance', ['the amount and type of risk that an organisation takes']),
            ('improved resilience against and recovery time from a harmful incident', ['the primary benefit of implementing appropriate information security within an organisation']),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['Open Source Intelligence', 'OSINT'], ['the collection andanalysis of information that is gathered from public sources']),
            (['the MOST IMPORTANT role of senior management in regard to information security'], ['Providing visible and material support for information security within the organisation']),
            (['Privacy'], ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            (['need to know basis'], ['preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable']),
            (['ISMS','information security management system'], 'defines and manages controls that an organization needs to implement to ensure that it is sensibly protecting the confidentiality, availability, and integrity of assets from threats and vulnerabilities'),
            (['Business continuity and disaster recovery'], ['a set of processes and techniques used to help an organization recover from a disaster and continue or resume routine business operations']),
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
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
    'integrity availability': {
        'question':'Which of the following can be described as a PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'threat',
        'negative':'vulnerability',
        'course_code':'',
        'correct':(
            'malware',
            'phishing',
            'malicious code',
            'earthquake', 
            'power outage', 
            'terrorist attack',
            'loss of a laptop',
        ),
        'incorrect': (
            'system misconfiguration',
            'incorrect file system structures',
            'a firedoor which can be opened from the outside',
            'an easilly replicable smart car entry system', 
            'a common password',
            'out of date software'

        ),
    },
    'integrity availability': {
        'question':'Which of the following can be described as PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'mitigation',
        'negative':'acceptance',
        'course_code':'',
        'correct':(
            'installing new anti virus software',
            'implementing a clean desk policy',
            'purchasing a new firewall',
            'installing a man trap'
        ),
        'incorrect': (
            'leaving earthquake out of a risk assessment',
            'considering the risk of a terrorist attack as being insignificant and taking no action',
            'leaving an old firewall in place',
        ),
    },
}