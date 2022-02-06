from random import randint

from ._1_logic import *

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

questions = {
    'example':example,
}
    
    



