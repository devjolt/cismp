from random import randint

from ._1_logic import *

questions = {
    'terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('non-repudiation', ['the ability to prove that an event occurred']), 
            ('fail secure', ['disconnecting a system if an event occurs']),
            ('symmetric key encryption', ['the use of public key cryptography to prevent the republishing of keys']),
            (['defence in depth'], 'the concept used in information security in which multiple layers of security controls are placed within a system'),
            (['impact','likelihood'], ['one of the two terms used in combination to define levels of risk']),
            ('risk appetite', ['the amount and type of risk that an organisation is prepared to pursue, retain or take']),
            ('risk tolerance', ['the amount and type of risk that an organisation takes']),
            ('improved resilience against and recovery time from a harmful incident', ['the primary benefit of implementing appropriate information security within an organisation']),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['Open Source Intelligence', 'OSINT'], ['the collection andanalysis of information that is gathered from public sources']),
            (['the MOST IMPORTANT role of senior management in regard to information security'], ['Providing visible and material support for information security within the organisation']),
            (['Privacy'], ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            (['Intellectual Property', 'IP'], ['the legal rights which result from activity in the industrial, scientific, literary and artistic fields']),
            (['ISO/IEC 27001'], ['a specification for an Information Security Management System']),
            (['ISO/IEC 27002'], ['information Security Management System implementation guidance']),
            (['ISO/IEC 15408'], ['the standards relating to the certification of security products']),
            (['ISO/IEC 24762', 'BS2577'], ['the standards relating to disaster recovery']),
            (['ISO/IEC 22301'], ['the standards relating to business continuity']),
            (['NIST 800-53'], ['provides a catalog of security and privacy controls for all U.S. federal information systems except those related to national security']),
            (['ISACA', 'Information Systems Audit and Control Association'], [' international professional association focused on IT governance']),
            (['SABSA', 'Sherwood Applied Business Security Architecture'], ['a framework and methodology for enterprise security architecture and service management']),
            (['OWASP', 'The Open Web Application Security Project'], ['an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security']),
            (['DevSecOps'], ['an approach to culture, automation, and platform design that integrates security as a shared responsibility throughout the entire IT lifecyclemm']),
            (['BS25999-1'], ['general guidance on the processes, principles and terminology']),
            (['BS25999-2'], ['a set of requirements for implementing, operating and improving a BCM System']),
            (['BS25777'], ['the collection andanalysis of information that is gathered from public sources']),
            (['ISO/IEC 27017'], ['the standards relating to practice for information security controls for cloud sevices']),
            (['ISO 31000'], ['an information risk management standard for any industry']),
            (['ISO 9001'], ['a quality manament standard']),
            (['need to know basis'], ['preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable']),
            (['flow down'], ['the passing on of contractual obligations from a supplier to a third party organisation']),
            (['ISMS','information security management system'], 'defines and manages controls that an organization needs to implement to ensure that it is sensibly protecting the confidentiality, availability, and integrity of assets from threats and vulnerabilities'),
            (['CMBD','configuration management database'],'a list of information about all assets in a system'),
            (['Business continuity and disaster recovery'], ['a set of processes and techniques used to help an organization recover from a disaster and continue or resume routine business operations']),
            (['SIEM'], ['aggregates and analyses activity from many different entities on a network']),
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
    'steps in setting out an information classification strategy': {
       
    'question':'What is the first step you should take when setting out an information classification strategy?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'',
        'course_code':'',
        'correct':(
            'determine the classification programme objectives',
        ),
        'incorrect': (
            'identify relevant information and process owners',
            'agree the relevant information classification labels',
            'develop the information classification policy',    
        ),
    },

    'information management cycle important': {
        'question':'From a security viewpoint, why is the information management cycle important?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'',
        'course_code':'',
        'correct':(
            'It reduces risk',
        ),
        'incorrect': (
            'It reduces costs',
            'It improves compliance',
            'It improves service',    
        ),
    },
    'test_question': {
        'question':'From a security viewpoint, which of the following is PLACEHOLDERrelevant to the information management cycle?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'ir',
        'course_code':'',
        'correct':(
            'It reduces risk',
        ),
        'incorrect': (
            'It reduces costs',
            'It improves compliance',
            'It improves service',    
        ),
    },
    


}

"""
avoid
mitigate
transfer

statutory requirement and advisory requirement
A statutory requirement is prescribed by law, an advisory requirement is typically
a recommendatio

"""



