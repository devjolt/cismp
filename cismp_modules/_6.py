from cismp.utilities import utilities as utl
from ._6_logic import *


questions = {
    'rings of security':rings_of_security,
    'types of virus': {
        'question_with_0':'What best describes a PLACEHOLDER virus?',
        'question_with_1':'What type of virus PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('polymorphic', 'alter themselves to avoid detection'),
            ('macro',['exploits scripts to hide in documents', 'exploits scripts to hide in files']),
            ('stealth','masks or hides activity to avoid detection'),
            ('armoured','is difficult to detect or remove'),
            ('retrovirus', 'attacks anti virus systems'),
            ('phage', 'infectf mutliple parts of the system to regenerate more easilly'),
            ('companion',['takes root filename of an executable','tries to launch itself instead of a legitimate program']),
            (['mutlipart','multipartite'], 'infects your boot sector as well as files')
        ),
        'fillers': (
        )
    },
    'types of malware': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of malware PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('virus',['requires user interaction', 'doesn\'t self propogate', 'requires a host']),
            ('worm',['self replicates without a triggering event', 'propogates itself through a network', 'can be uses to distribute viruses', 'can be uses to distribute lobic bombs']),
            ('trojan',['downloaded by a user as part of a desired piece of code', 'disguised as something legitimate', f"is introduced through {utl.pick_one(['illegal downloads', 'games', 'screensavers','system softeware'])}", 'used to install DDoS Zombies/Bots']),
            ('rootkit',['works beneath the level at which tools used to detect viruses operate', 'operates at the kernel level', 'may be detected using heuristics']), 
            ('back door',['also called a trap door', 'may be installed legitaimnately into code', 'may be installed maliciously through trojan, virus, code download or manually', 'enables remote access clients']),
            ('spyware',['gathers data from your machine using your machine\'s resources', 'may be used in identity theft', 'associated with key logging']),
            ('adware',['promotes goods or services at the expecse of machine\'s resources', 'displays unwanted pop-up advertisements based on user activity']),
            ('ransomware',['files encrypted by bad actors', 'used to extort money']), 
            ('logic bomb',['maliscious code triggered by an action or a date', 'normally associated with insider attacks']), 
            (['bot','botnet'],['machine taken over using malicous code', 'controlled by a bot herder', 'are associated with DDoS attacks']),
            ('zero day exploit',['takes advantage of software which has just been launched', 'takes advantage of the lack of known attack signatures']),
        ),
        'fillers': (
        )
    },

    'types of attack': {
        'question_with_0':'What best describes a PLACEHOLDER attack?',
        'question_with_1':'What type of attack PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['man in the middle','MitM'],[f"involves {utl.pick_one(['spoofing', 'poisoning'])} name resolution systems", f"may involve {utl.pick_one(['spoofing', 'poisoning'])} {utl.pick_one(['DNS', 'domain name server', 'ARP', 'NetBios','WINS'])}"]),
            (['DoS', 'DDos'],['involves flooding an address with messages', 'overwhelming an address with requests']),
            ('spoofing', ['falsifying network data to undermine a system', f"may be used for {utl.pick_one(['replay attacks', 'SPAM', 'WAP attacks'])}"]),
            ('spam', 'sending unsolicited communication'),
            ('spim', 'using SMS services to get people to displose their data'),
            ('phishing', 'using emails to get people to displose their data'),
            ('spear phishing', 'targeting specific individuals with emails designed to get data'),
            ('whaling','targeting people in positions of respnonsibility with fake emails to get data'),
            ('vishing', 'using voice calls under false pretences to get users to disclose data'),
            ('pharming', 'malicious redirects of websites to fake sites in order to conduct Phishing attacks'),
            ('DNS poisoning', ['falsifying domain name service data', 'can be used to redirect to malicious sites']),
            ('ARP posoning', ['falsify IP-mac resolution', 'ommonly used in active sniffing attacks and matn in the middle attacks']),
            ('insider', f"can be protected against by {utl.pick_one(['policies', 'auditing', 'background checks', 'prhibiting external devices', 'application whitelisting'])}"),
            ('password', [f"can be protected against using {utl.pick_one(['longer', 'complex', 'regularly updated'])}",'passwords','brute force', 'dictionary attack', 'birthday attack', 'rainbow attack'] ),
            ('transitive access', 'sharing data with someone on the basis that they are trusted by someone you trust' ),
            (['url hacking','typo squatting'], 'using commonly misspelt urls to lure people onto a malicious site'),
            ('social engineering', ['exploiting human nature', f"using {utl.pick_one(['authority', 'intimidation', 'scarcity', 'urgency', 'familiarity', 'trust', 'flattery'])} to gain access or information"]),
            ('watering hole attack', 'observing users\' behaviour to lure them to a malicious site'),
    
        ),
        'fillers': (
        )
    },
    'types of DoS attack': {
        'question_with_0':'What best describes a PLACEHOLDER attack?',
        'question_with_1':'What type of attack PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('Smurf','uses ping packets agains the broadcast address so the replies return to the victim'),
            ('fraggle','uses UDP packets so the ICMP reply returns to the victum'),
            ('land ',['sends packets to a victim containing identical source and destination addresses','causes a victim to become stuck in a loop sending packets to themself']),
            ('ping of death',['sends large packets to a victim', 'sends packets too large for a victim to handle']), 
            ('syn flood',['sends TCP packets to a victim', 'exploits the three way handshake'])
        ),
        'fillers': (
        )
    },

    'types of password attacks': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of attack involves PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['brute force'],'attempting all valid combinations'),
            ('rainbow','using large pre-calculated databased of hashes to crack captured password hashes'),
            ('dictionary','attempts to break passwords based on a dictionary or list of words'),
            ('birthday attack','based on probability theory'), 
        ),
        'fillers': (
        )
    },
    

}


"""
DNS
exploits

Rogue DNS server
SND poisoning
IP configuration corruption
proxy corruption


shoulder surfing - looking over someone's shoulder
dumpster diving
hoax emails
impersonation

rogue access points
evil twin same ssid
interference - jamming with noise
war driving using monitoring software to look for the presence of wireless networks
war chalking
bluejacking
bluesnarfing


wireless attacks
xss/cross site scripting - exploits trust a browser has with the web server
may result in identity data theft
financial loss
key logging

sql injection
use unexpected input to gain unauthorised access
exploits vulnerabilities  between front and back end

protects against sql injection with 
input validation
limit account privileges

LDAP atacks directory services rather than SQL
directory traversal - tryig to get beyond web contect an dgain other parts of file system
buffer overflow
header manipulation - modify headers submitted to a web server to manipulate cookies

application attacjs

forms tampering - chaning hidden values
url tampering -chaning the paths in urls to gain access to unaun
cookie tampering - stealing or modifying cookies to gain session tokens to provide access

telephone systems WAR dialing

mitigation 

SCADA
supervisory control and data acquisition system
industrial control system

used for large scale DoS
state espionage
terrorism

mitigateion
segregation of business and real time networks
segregation from the internet
restricted access
VPN/remote access

CCTV feeds
cctv systems are extensively used in the security of industrial , government and domestic environments
unnauthorised access

risks from instant messaging



    'types of spoofing attacks': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of malware PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['DoS', 'DDoS'],'using packets agains the broadcast address so the replies return to the victim'),
            ('SPAM','UDP packets used so the ICMP reply returns to the victum'),
            ('WAP attack',[]),
            
        ),
        'fillers': (
        )
    },

"""


